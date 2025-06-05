from .utils import *    
from .script import script
from typing import Union, List, Tuple, Optional, Any, Literal

def initialize_solver(
    solver_model: Literal['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL', 
                         'SUPERSONIC_LINEAR_DOUBLET', 'TANGENT_CONE', 'MODIFIED_NEWTONIAN'],
    surfaces: Union[int, List[Union[int, Tuple[int, Literal['ENABLE', 'DISABLE']]]]],
    wake_termination_x: Union[str, float] = 'DEFAULT',
    symmetry: Literal['NONE', 'MIRROR', 'PERIODIC'] = 'NONE',
    symmetry_periodicity: int = 1,
    wall_collision_avoidance: Literal['ENABLE', 'DISABLE'] = 'ENABLE',
    stabilization: Literal['ENABLE', 'DISABLE'] = 'ENABLE',
    stabilization_strength: float = 1.0
) -> None:
    """
    Appends lines to script state to initialize the solver.
    
    Args:
        solver_model (str): One of: 'INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL', 
                           'SUPERSONIC_LINEAR_DOUBLET', 'TANGENT_CONE', 'MODIFIED_NEWTONIAN'
        surfaces (int or list): Number of surfaces being initialized in the solver (> 0 and < total surfaces).
                               Value can be -1 to specify all boundaries. If a list is provided, each item should
                               be a tuple of (surface_index, quad_mesher_enabled) where quad_mesher_enabled is 'ENABLE' or 'DISABLE'.
                               Alternatively, a list of integers can be provided, in which case quad_mesher_enabled will default to 'ENABLE'.
        wake_termination_x (str or float): Wake termination plane location downstream of the geometry. X axis value 
                                         measured relative to the Reference coordinate system. Use value of 'DEFAULT' 
                                         if you require this value to be auto-computed. Required for solvers 1-3.
        symmetry (str): One of: 'NONE', 'MIRROR', 'PERIODIC'. If 'PERIODIC', symmetry_periodicity must be provided. Default is 'NONE'.
        symmetry_periodicity (int): Integer value for number of periodic symmetry transforms about the Reference frame X axis.
        wall_collision_avoidance (str): 'ENABLE' or 'DISABLE' wall collision avoidance for the wake strands. Required for solvers 1-3. Default is 'Enable'
        stabilization (str): 'ENABLE' or 'DISABLE' solver stabilization. Required for models 1-3.
        stabilization_strength (float): Stabilization strength value (0.0 < Value < 5.0). Only used when stabilization is 'ENABLE'.
    
    Example usage:
    # For INCOMPRESSIBLE solver with specific surfaces
    initialize_solver('INCOMPRESSIBLE', [(1, 'ENABLE'), (2, 'ENABLE')], '3.5', 'MIRROR', 1, 'DISABLE', 'ENABLE', 1.0)
    
    # For SUBSONIC_PRANDTL_GLAUERT solver with all surfaces
    initialize_solver('SUBSONIC_PRANDTL_GLAUERT', -1, '3.5', 'PERIODIC', 4, 'DISABLE', 'ENABLE', 1.0)
    
    # For TANGENT_CONE solver
    initialize_solver('TANGENT_CONE', [(1, 'ENABLE'), (2, 'ENABLE')], symmetry='NONE')
    """
    
    # Validate solver_model
    valid_models = ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL', 
                   'SUPERSONIC_LINEAR_DOUBLET', 'TANGENT_CONE', 'MODIFIED_NEWTONIAN']
    if solver_model not in valid_models:
        raise ValueError(f"`solver_model` must be one of {valid_models}")
    
    # Validate surfaces
    if surfaces != -1:
        if not isinstance(surfaces, list):
            raise ValueError("`surfaces` should be a list of integers, a list of tuples, or -1.")
        
        # Convert list of integers to list of tuples with 'ENABLE' as default
        if surfaces and all(isinstance(surface, int) for surface in surfaces):
            surfaces = [(surface, 'ENABLE') for surface in surfaces]
        
        for surface in surfaces:
            if not isinstance(surface, tuple) or len(surface) != 2:
                raise ValueError("Each entry in `surfaces` should be a tuple of (surface_index, quad_mesher_enabled).")
            
            if not isinstance(surface[1], str) or surface[1] not in ['ENABLE', 'DISABLE']:
                raise ValueError("Second element in each tuple should be 'ENABLE' or 'DISABLE'.")
    
    # Validate symmetry
    valid_symmetry = ['NONE', 'MIRROR', 'PERIODIC']
    if symmetry not in valid_symmetry:
        raise ValueError(f"`symmetry` must be one of {valid_symmetry}")
    
    # If symmetry is PERIODIC, validate symmetry_periodicity
    if symmetry == 'PERIODIC':
        if not isinstance(symmetry_periodicity, int) or symmetry_periodicity <= 0:
            raise ValueError("`symmetry_periodicity` should be a positive integer when symmetry is 'PERIODIC'.")
    
    # Validate wake_termination_x for solvers 1-3
    if solver_model in ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL']:
        if wake_termination_x != 'DEFAULT' and not isinstance(wake_termination_x, (int, float)):
            raise ValueError("`wake_termination_x` should be either 'DEFAULT' or a number.")
    
    # Validate wall_collision_avoidance and stabilization for solvers 1-3
    if solver_model in ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL']:
        for param, value in {'wall_collision_avoidance': wall_collision_avoidance, 'stabilization': stabilization}.items():
            if value not in ['ENABLE', 'DISABLE']:
                raise ValueError(f"`{param}` should be either 'ENABLE' or 'DISABLE'.")
        
        # Validate stabilization_strength if stabilization is ENABLE
        if stabilization == 'ENABLE':
            if not isinstance(stabilization_strength, (int, float)) or not (0.0 < stabilization_strength < 5.0):
                raise ValueError("`stabilization_strength` should be a number between 0.0 and 5.0.")
    
    # Create the command lines
    lines = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        f"SOLVER_MODEL {solver_model}",
    ]
    
    # Add symmetry periodicity if needed
    if symmetry == 'PERIODIC':
        lines.append(f"SYMMETRY_PERIODICITY {symmetry_periodicity}")
    
    # Add surfaces
    if surfaces == -1:
        lines.append("SURFACES -1")
    else:
        lines.append(f"SURFACES {len(surfaces)}")
        
        for surface in surfaces:
            lines.append(f"{surface[0]},{surface[1]}")
    
    # Add wake termination for solvers 1-3
    if solver_model in ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL']:
        lines.append(f"WAKE_TERMINATION_X {wake_termination_x}")
    
    # Add symmetry
    if symmetry == 'PERIODIC':
        lines.append(f"SYMMETRY {symmetry} {symmetry_periodicity}")
    else:
        lines.append(f"SYMMETRY {symmetry}")
    
    # Add wall collision avoidance and stabilization for solvers 1-3
    if solver_model in ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL']:
        lines.append(f"WALL_COLLISION_AVOIDANCE {wall_collision_avoidance}")
        
        if stabilization == 'ENABLE':
            lines.append(f"STABILIZATION {stabilization} {stabilization_strength}")
        else:
            lines.append(f"STABILIZATION {stabilization}")

    script.append_lines(lines)
    return

def solver_proximal_boundaries(*boundaries: int) -> None:
    """
    Appends lines to script state to enable solver proximity checking for specified boundaries.
    

    :param boundaries: Indices of the geometry boundaries for which solver proximity checking is being enabled.
    
    Example usage:
    solver_proximal_boundaries(, 1, 4, 5)
    """
    
    # Type and value checking
    for boundary in boundaries:
        if not isinstance(boundary, int):
            raise ValueError("`boundaries` should be a list/tuple of integer values.")
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver proximity checking for specified boundaries ****",
        "#************************************************************************",
        "#",
        f"SOLVER_PROXIMAL_BOUNDARIES {len(boundaries)}"
    ]

    for boundary in boundaries:
        lines.append(str(boundary))
        
    script.append_lines(lines)
    return

def solver_remove_initialization() -> None:
    """
    Appends lines to script state to remove the solver initialization.
    

    
    Example usage:
    >>> solver_remove_initialization()
    """
    
    lines = [
        "#************************************************************************",
        "#********* Remove the solver initialization *****************************",
        "#************************************************************************",
        "#",
        "SOLVER_REMOVE_INITIALIZATION"
    ]
    
    script.append_lines(lines)
    return
