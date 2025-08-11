from .types import (
    RunOptions, VALID_RUN_OPTIONS, VALID_SOLVER_MODEL_LIST, VALID_SYMMETRY_LIST
)
from typing import Union, List, Tuple
from .script import script
from .utils import *

def initialize_solver(
    solver_model: str,
    surfaces: Union[int, List[Union[int, Tuple[int, RunOptions]]]],
    wake_termination_x: Union[str, float] = 'DEFAULT',
    symmetry: str = 'NONE',
    symmetry_periodicity: int = 1,
    wall_collision_avoidance: RunOptions = 'ENABLE',
    stabilization: RunOptions = 'ENABLE',
    stabilization_strength: float = 1.0
) -> None:
    """
    Initialize the solver with specified parameters.

    This function appends a command to the script state to set up the solver
    with a chosen model and configuration.

    Parameters
    ----------
    solver_model : str
        The solver model to use. Must be one of `VALID_SOLVER_MODEL_LIST`.
    surfaces : Union[int, List[Union[int, Tuple[int, RunOptions]]]]
        Specifies the surfaces to be included in the simulation.
        - Use -1 to include all boundaries.
        - Provide a list of integers to specify surface indices (quad mesher enabled by default).
        - Provide a list of tuples, where each tuple contains the surface index
          and the quad mesher status ('ENABLE' or 'DISABLE').
    wake_termination_x : Union[str, float], optional
        The wake termination plane location downstream. Use 'DEFAULT' for
        auto-computation, by default 'DEFAULT'.
    symmetry : str, optional
        The symmetry condition, by default 'NONE'. Must be one of
        `VALID_SYMMETRY_LIST`.
    symmetry_periodicity : int, optional
        The number of periodic symmetry transforms, required if symmetry is
        'PERIODIC', by default 1.
    wall_collision_avoidance : RunOptions, optional
        Enable or disable wall collision avoidance for wake strands, by default
        'ENABLE'. Must be one of `VALID_RUN_OPTIONS`.
    stabilization : RunOptions, optional
        Enable or disable solver stabilization, by default 'ENABLE'. Must be
        one of `VALID_RUN_OPTIONS`.
    stabilization_strength : float, optional
        The stabilization strength (0.0 < value < 5.0), by default 1.0.

    Examples
    --------
    >>> # Initialize an incompressible solver with specific surfaces
    >>> initialize_solver(
    ...     'INCOMPRESSIBLE', [(1, 'ENABLE'), (2, 'ENABLE')],
    ...     wake_termination_x=3.5, symmetry='MIRROR'
    ... )

    >>> # Initialize a tangent cone solver with all surfaces
    >>> initialize_solver('TANGENT_CONE', -1)
    """
    if solver_model not in VALID_SOLVER_MODEL_LIST:
        raise ValueError(f"`solver_model` must be one of {VALID_SOLVER_MODEL_LIST}")

    if surfaces != -1:
        if not isinstance(surfaces, list):
            raise ValueError("`surfaces` must be a list of integers, a list of tuples, or -1.")
        if surfaces and all(isinstance(s, int) for s in surfaces):
            surfaces = [(s, 'ENABLE') for s in surfaces]
        for surface in surfaces:
            if not (isinstance(surface, tuple) and len(surface) == 2 and
                    isinstance(surface[0], int) and surface[1] in VALID_RUN_OPTIONS):
                raise ValueError("Each entry in `surfaces` must be a tuple of (index, 'ENABLE'/'DISABLE').")

    if symmetry not in ["NONE", "MIRROR", "PERIODIC"]:
        raise ValueError(f"`symmetry` must be one of NONE, MIRROR, or PERIODIC")
    if symmetry == 'PERIODIC' and (not isinstance(symmetry_periodicity, int) or symmetry_periodicity <= 0):
        raise ValueError("`symmetry_periodicity` must be a positive integer for 'PERIODIC' symmetry.")

    if solver_model in ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL']:
        if wake_termination_x != 'DEFAULT' and not isinstance(wake_termination_x, (int, float)):
            raise ValueError("`wake_termination_x` must be 'DEFAULT' or a number.")
        if wall_collision_avoidance not in VALID_RUN_OPTIONS:
            raise ValueError(f"`wall_collision_avoidance` must be one of {VALID_RUN_OPTIONS}")
        if stabilization not in VALID_RUN_OPTIONS:
            raise ValueError(f"`stabilization` must be one of {VALID_RUN_OPTIONS}")
        if stabilization == 'ENABLE' and not (0.0 < stabilization_strength < 5.0):
            raise ValueError("`stabilization_strength` must be between 0.0 and 5.0.")

    lines = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        f"SOLVER_MODEL {solver_model}",
    ]

    if surfaces == -1:
        lines.append("SURFACES -1")
    else:
        lines.append(f"SURFACES {len(surfaces)}")
        for surface in surfaces:
            lines.append(f"{surface[0]},{surface[1]}")

    if solver_model in ['INCOMPRESSIBLE', 'SUBSONIC_PRANDTL_GLAUERT', 'TRANSONIC_FIELD_PANEL']:
        lines.append(f"WAKE_TERMINATION_X {wake_termination_x}")

    # Emit symmetry in a single line per manual: "SYMMETRY MIRROR|NONE" or
    # "SYMMETRY PERIODIC <COPIES>"
    if symmetry == 'PERIODIC':
        lines.append(f"SYMMETRY PERIODIC {symmetry_periodicity}")
    else:
        lines.append(f"SYMMETRY {symmetry}")

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
    Enable solver proximity checking for specified boundaries.

    This function appends a command to the script state to enable proximity
    checking for the given boundary indices. This is used to prevent wake
    strands from penetrating certain boundaries.

    Parameters
    ----------
    *boundaries : int
        Variable length argument list of geometry boundary indices for which 
        proximity checking is to be enabled.

    Examples
    --------
    >>> # Enable proximity checking for boundaries 1, 4, and 5
    >>> solver_proximal_boundaries(1, 4, 5)

    >>> # Enable proximity checking for a single boundary
    >>> solver_proximal_boundaries(2)
    """
    if not boundaries:
        raise ValueError("At least one boundary index must be provided.")
    if not all(isinstance(b, int) for b in boundaries):
        raise ValueError("All `boundaries` must be integers.")

    lines = [
        "#************************************************************************",
        "#********* Enable solver proximity checking for specified boundaries ****",
        "#************************************************************************",
        "#",
        f"SOLVER_PROXIMAL_BOUNDARIES {len(boundaries)}"
    ]
    lines.extend(map(str, boundaries))
    script.append_lines(lines)
    return

def solver_remove_initialization() -> None:
    """
    Remove the solver initialization.

    This function appends a command to the script state to clear the current
    solver initialization.

    Examples
    --------
    >>> # Remove the solver initialization
    >>> solver_remove_initialization()
    """
    lines = [
        "#************************************************************************",
        "#********* Remove the solver initialization *****************************",
        "#************************************************************************",
        "#",
        "REMOVE_INITIALIZATION"
    ]
    script.append_lines(lines)
    return
