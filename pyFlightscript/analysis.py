from .utils import *    
from .script import script    
from .types import *
from typing import Union, Optional, Literal, List

def scene_contour(variable: int = 4) -> None:
    """
    Set the scene contour parameter for visualization.

    This function appends a command to the script state to change the contour
    parameter displayed in the scene.

    Parameters
    ----------
    variable : int, optional
        The value corresponding to the desired contour parameter.
        Defaults to 4 (Vorticity).

        - 0: No contour
        - 1: X
        - 2: Y
        - 3: Z
        - 4: Vorticity
        - 5: Skin friction coefficient
        - 6: Area
        - 7: Boundary Mach Number
        - 8: Coefficient of pressure (Free-stream velocity)
        - 9: Mach Number
        - 10: Solver partition ID
        - 11: Separation marker
        - 12: Velocity X component
        - 13: Velocity Y component
        - 14: Velocity Z component
        - 15: Velocity magnitude
        - 16: Boundary layer displacement thickness
        - 17: Boundary layer streamline length
        - 18: Coefficient of pressure (reference velocity)
        - 19: Solver mesh quality
        - 20: Boundary layer transition marker
        - 21: Solver mesh stabilization
        - 22: Boundary layer momentum thickness
        - 23: Boundary layer momentum gradient
        - 24: Boundary layer shape factor
        - 25: Boundary layer stagnation marker

    Raises
    ------
    ValueError
        If `variable` is not a valid integer between 0 and 25.

    Examples
    --------
    >>> # Set the scene contour to display Mach Number
    >>> scene_contour(variable=9)

    >>> # Set the scene contour to display skin friction
    >>> scene_contour(variable=5)
    """
    
    # Type and value checking
    valid_variables = list(range(26))  # 0 to 25
    if variable not in valid_variables:
        raise ValueError(f"`variable` should be one of {valid_variables}")
    
    lines = [
        "#************************************************************************",
        "#****************** Change scene contour parameter **********************",
        "#************************************************************************",
        "#",
        "SET_SCENE_CONTOUR",
        f"VARIABLE {variable}"
    ]

    script.append_lines(lines)
    return

def set_vorticity_drag_boundaries(
    num_boundaries: int,
    boundary_indices: Optional[List[int]] = None
) -> None:
    """
    Set vorticity-based induced drag boundaries.

    This function appends a command to the script state to define which
    boundaries are used for calculating vorticity-based induced drag.

    Parameters
    ----------
    num_boundaries : int
        The number of boundaries to be added to the list. If -1, all boundaries
        are used.
    boundary_indices : Optional[List[int]], optional
        A list of boundary indices to be used. This parameter is ignored if
        `num_boundaries` is -1. Defaults to None.

    Raises
    ------
    ValueError
        If `num_boundaries` is not an integer, or if `boundary_indices` is not
        a list of integers when required, or if its length does not match
        `num_boundaries`.

    Examples
    --------
    >>> # Set all boundaries for vorticity drag calculation
    >>> set_vorticity_drag_boundaries(num_boundaries=-1)

    >>> # Set specific boundaries for vorticity drag calculation
    >>> set_vorticity_drag_boundaries(num_boundaries=3, boundary_indices=[1, 3, 5])
    """
    
    # Type and value checking for num_boundaries
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` should be an integer value.")
    
    # Prepare script lines
    lines = [
        "#************************************************************************",
        "#****** Set a custom vorticity induced-drag boundary list ***************",
        "#************************************************************************",
        "#"
    ]
    
    if num_boundaries == -1:
        # Setting all mesh boundaries
        lines.append("SET_VORTICITY_DRAG_BOUNDARIES -1")
        lines.append("# All mesh boundaries set as vorticity induced-drag boundaries.")
    else:
        # Validate boundary_indices if num_boundaries is not -1
        if not isinstance(boundary_indices, list) or not all(isinstance(idx, int) for idx in boundary_indices):
            raise ValueError("When `num_boundaries` is not -1, `boundary_indices` should be a list of integers.")
        
        if len(boundary_indices) != num_boundaries:
            raise ValueError("`boundary_indices` length must match `num_boundaries`.")
        
        # Setting specified boundaries
        lines.append(f"SET_VORTICITY_DRAG_BOUNDARIES {num_boundaries}")
        lines.append(",".join(map(str, boundary_indices)))

    # Assuming script.append_lines is a function to append lines to a global script context
    script.append_lines(lines)
    return

def delete_vorticity_drag_boundaries():
    """
    Clears the vorticity induced-drag boundaries from the script state.
    """
    lines = [
        "#************************************************************************",
        "#************** Clear the vorticity induced-drag boundaries *************",
        "#************************************************************************",
        "#",
        "DELETE_VORTICITY_DRAG_BOUNDARIES"
    ]

    script.append_lines(lines)
    return

def set_analysis_moments_model(model: str = "PRESSURE") -> None:
    """
    Set the moments model used in the analysis.

    This function appends a command to the script state to set the moments
    model to either 'PRESSURE' or 'VORTICITY'.

    Parameters
    ----------
    model : str, optional
        The moments model to be used. Must be either 'PRESSURE' or 'VORTICITY'.
        Defaults to 'PRESSURE'.

    Raises
    ------
    ValueError
        If `model` is not 'PRESSURE' or 'VORTICITY'.

    Examples
    --------
    >>> # Set the moments model to VORTICITY
    >>> set_analysis_moments_model(model='VORTICITY')

    >>> # Set the moments model to PRESSURE (default)
    >>> set_analysis_moments_model(model='PRESSURE')
    """
    
    # Type and value checking
    if model not in ['PRESSURE', 'VORTICITY']:
        raise ValueError("`model` must be either 'PRESSURE' or 'VORTICITY'.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the moments model used in the analysis **********",
        "#************************************************************************",
        "#",
        f"SET_ANALYSIS_MOMENTS_MODEL {model}"
    ]

    script.append_lines(lines)
    return

def set_analysis_symmetry_loads(enable: bool) -> None:
    """
    Enable or disable including loads from symmetry boundaries in the analysis.

    This function appends a command to the script state to control whether
    loads from symmetry boundaries are included in the analysis calculations.

    Parameters
    ----------
    enable : bool
        If True, enables the inclusion of symmetry loads. If False, disables it.

    Raises
    ------
    ValueError
        If `enable` is not a boolean value.

    Examples
    --------
    >>> # Enable symmetry loads in the analysis
    >>> set_analysis_symmetry_loads(enable=True)

    >>> # Disable symmetry loads in the analysis
    >>> set_analysis_symmetry_loads(enable=False)
    """
    
    # Type checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value.")
    
    action = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#**** Enable the analysis to include loads from symmetry boundaries *****" if enable else "#**** Disable the analysis to include loads from symmetry boundaries ****",
        "#************************************************************************",
        "#",
        f"SET_ANALYSIS_SYMMETRY_LOADS {action}"
    ]

    script.append_lines(lines)
    return

def analysis_loads_frame(load_frame: int = 1) -> None:
    """
    Set the loads frame for analysis.

    This function appends a command to the script state to specify the
    coordinate system frame used for evaluating aerodynamic loads and moments.

    Parameters
    ----------
    load_frame : int, optional
        The index of the coordinate system to be used for evaluating loads
        and moments. Defaults to 1.

    Raises
    ------
    ValueError
        If `load_frame` is not an integer.

    Examples
    --------
    >>> # Set the analysis loads frame to coordinate system 2
    >>> analysis_loads_frame(load_frame=2)

    >>> # Use the default loads frame
    >>> analysis_loads_frame()
    """
    
    # Type and value checking
    if not isinstance(load_frame, int):
        raise ValueError("`load_frame` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the loads frame in the analysis tab *************",
        "#************************************************************************",
        "#",
        f"SET_SOLVER_ANALYSIS_LOADS_FRAME {load_frame}"
    ]

    script.append_lines(lines)
    return

def vorticity_lift_model(enable: bool = True) -> None:
    """
    Enable or disable the vorticity lift model.

    This function appends a command to the script state to set the lift model
    to vorticity mode.

    Parameters
    ----------
    enable : bool, optional
        If True, enables the vorticity lift model. If False, disables it.
        Defaults to True.

    Raises
    ------
    ValueError
        If `enable` is not a boolean value.

    Examples
    --------
    >>> # Enable the vorticity lift model
    >>> vorticity_lift_model(enable=True)

    >>> # Disable the vorticity lift model
    >>> vorticity_lift_model(enable=False)
    """
    
    # Type and value checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value (True/False).")
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#****************** Set the lift model to vorticity mode ****************",
        "#************************************************************************",
        "#",
        f"SET_VORTICITY_LIFT_MODEL {status}"
    ]

    script.append_lines(lines)
    return

def loads_and_moments_units(unit_type: ValidForceUnits = 'NEWTONS') -> None:
    """
    Set the units for loads and moments in the analysis.

    This function appends a command to the script state to specify the
    units used for evaluating aerodynamic loads and moments.

    Parameters
    ----------
    unit_type : ValidForceUnits, optional
        The unit type for loads and moments. Can be one of 'COEFFICIENTS',
        'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', or 'KILOGRAM-FORCE'.
        Defaults to 'NEWTONS'.

    Raises
    ------
    ValueError
        If `unit_type` is not a valid force unit.

    Examples
    --------
    >>> # Set the loads and moments units to pound-force
    >>> loads_and_moments_units(unit_type='POUND-FORCE')

    >>> # Use the default units (Newtons)
    >>> loads_and_moments_units()
    """
    
    if unit_type not in VALID_FORCE_UNITS_LIST:
        raise ValueError(f"`unit_type` must be one of {VALID_FORCE_UNITS_LIST}")

    lines = [
        "#************************************************************************",
        "#****************** Set the solver analysis units selection *************",
        "#************************************************************************",
        "#",
        f"SET_LOADS_AND_MOMENTS_UNITS {unit_type}"
    ]
    script.append_lines(lines)
    return

def analysis_boundaries(num_boundaries: int, boundaries_list: List[int]) -> None:
    """
    Set the solver analysis boundaries.

    This function appends a command to the script state to specify which
    boundaries are used in the solver analysis.

    Parameters
    ----------
    num_boundaries : int
        The number of solver boundaries being enabled. Must be a positive integer.
    boundaries_list : List[int]
        A list of solver boundary indices to be enabled. The length of this list
        must match `num_boundaries`.

    Raises
    ------
    ValueError
        If `num_boundaries` is not a positive integer, if `boundaries_list` is
        not a list of integers, or if the length of `boundaries_list` does not
        match `num_boundaries`.

    Examples
    --------
    >>> # Set boundaries 1, 2, 4, 5, and 7 for the analysis.
    >>> analysis_boundaries(num_boundaries=5, boundaries_list=[1, 2, 4, 5, 7])
    """
    
    if not isinstance(num_boundaries, int) or num_boundaries <= 0:
        raise ValueError("`num_boundaries` should be a positive integer value.")

    if not isinstance(boundaries_list, list) or not all(isinstance(i, int) for i in boundaries_list):
        raise ValueError("`boundaries_list` must be a list of integers.")

    if len(boundaries_list) != num_boundaries:
        raise ValueError("The length of `boundaries_list` must match `num_boundaries`.")

    boundaries_str = ','.join(map(str, boundaries_list))
    lines = [
        "#************************************************************************",
        "#****************** Set the solver analysis boundaries ******************",
        "#************************************************************************",
        "#",
        f"SET_SOLVER_ANALYSIS_BOUNDARIES {num_boundaries}",
        boundaries_str
    ]

    script.append_lines(lines)
    return

def set_inviscid_loads(enable: bool) -> None:
    """
    Enable or disable the computation of inviscid loads and moments only.

    This function appends a command to the script state to control whether
    the analysis should compute only inviscid loads and moments.

    Parameters
    ----------
    enable : bool
        If True, enables the computation of inviscid loads and moments only.
        If False, disables it.

    Raises
    ------
    ValueError
        If `enable` is not a boolean value.

    Examples
    --------
    >>> # Enable inviscid loads and moments only
    >>> set_inviscid_loads(enable=True)

    >>> # Disable inviscid loads and moments only
    >>> set_inviscid_loads(enable=False)
    """
    
    # Type checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value.")

    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Set the Analysis to be inviscid loads & moments only *********",
        "#************************************************************************",
        "#",
        f"SET_INVISCID_LOADS {status}"
    ]

    script.append_lines(lines)
    return
