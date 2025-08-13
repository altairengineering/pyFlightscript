from typing import List, Union, Literal, Optional
from .script import script
from .types import (
    RunOptions, VALID_RUN_OPTIONS, VALID_STABILITY_UNITS_LIST,
    VALID_FORCE_UNITS_LIST, VALID_STABILITY_NUMERATOR_LIST,
    VALID_STABILITY_DENOMINATOR_LIST
)

# Valid export surface data options
ExportSurfaceDataOptions = Literal['DISABLE', 'TXT', 'CSV', 'DAT', 'VTK']
VALID_EXPORT_SURFACE_DATA_OPTIONS = ['DISABLE', 'TXT', 'CSV', 'DAT', 'VTK']

def execute_solver_sweeper(
    results_filename: str,
    angle_of_attack: RunOptions = 'ENABLE',
    side_slip_angle: RunOptions = 'DISABLE',
    velocity: RunOptions = 'DISABLE',
    velocity_mode: Literal['VELOCITY', 'MACH'] = 'VELOCITY',
    angle_of_attack_start: float = 0.0,
    angle_of_attack_stop: float = 0.0,
    angle_of_attack_delta: float = 1.0,
    side_slip_angle_start: float = 0.0,
    side_slip_angle_stop: float = 0.0,
    side_slip_angle_delta: float = 1.0,
    velocity_start: float = 0.0,
    velocity_stop: float = 0.0,
    velocity_delta: float = 1.0,
    export_surface_data_per_step: ExportSurfaceDataOptions = 'DISABLE',
    surface_results_path: Optional[str] = None,
    clear_solution_after_each_run: RunOptions = 'ENABLE',
    reference_velocity_equals_freestream: RunOptions = 'ENABLE',
    append_to_existing_sweep: RunOptions = 'DISABLE'
) -> None:
    """
    Execute the solver sweeper.

    This function appends a command to the script state to perform a parameter
    sweep with the solver.

    Parameters
    ----------
    results_filename : str
        The full file path for the sweep results file.
    angle_of_attack : RunOptions, optional
        Enable or disable angle of attack sweep, by default 'ENABLE'.
    side_slip_angle : RunOptions, optional
        Enable or disable side slip angle sweep, by default 'DISABLE'.
    velocity : RunOptions, optional
        Enable or disable velocity/Mach sweep, by default 'DISABLE'.
    velocity_mode : Literal['VELOCITY', 'MACH'], optional
        Specify whether to use VELOCITY or MACH parameter names, by default 'VELOCITY'.
    angle_of_attack_start : float, optional
        Start value for angle of attack sweep, by default 0.0.
    angle_of_attack_stop : float, optional
        Stop value for angle of attack sweep, by default 0.0.
    angle_of_attack_delta : float, optional
        Increment for angle of attack sweep, by default 1.0.
    side_slip_angle_start : float, optional
        Start value for side slip angle sweep, by default 0.0.
    side_slip_angle_stop : float, optional
        Stop value for side slip angle sweep, by default 0.0.
    side_slip_angle_delta : float, optional
        Increment for side slip angle sweep, by default 1.0.
    velocity_start : float, optional
        Start value for velocity/Mach sweep, by default 0.0.
    velocity_stop : float, optional
        Stop value for velocity/Mach sweep, by default 0.0.
    velocity_delta : float, optional
        Increment for velocity/Mach sweep, by default 1.0.
    export_surface_data_per_step : ExportSurfaceDataOptions, optional
        Type of boundary data to export per sweep run, by default 'DISABLE'.
        Options: 'DISABLE', 'TXT', 'CSV', 'DAT', 'VTK'.
    surface_results_path : Optional[str], optional
        Path for exporting surface data. Required if export_surface_data_per_step is not 'DISABLE'.
    clear_solution_after_each_run : RunOptions, optional
        Enable or disable clearing the solution after each run, by default 'ENABLE'.
    reference_velocity_equals_freestream : RunOptions, optional
        Set reference velocity equal to freestream velocity, by default 'ENABLE'.
    append_to_existing_sweep : RunOptions, optional
        Enable or disable appending to an existing sweep file, by default 'DISABLE'.
    """
    # Validate options
    for option in [angle_of_attack, side_slip_angle, velocity, clear_solution_after_each_run, 
                   reference_velocity_equals_freestream, append_to_existing_sweep]:
        if option not in VALID_RUN_OPTIONS:
            raise ValueError(f"Invalid option '{option}'. Must be one of {VALID_RUN_OPTIONS}")
    
    if export_surface_data_per_step not in VALID_EXPORT_SURFACE_DATA_OPTIONS:
        raise ValueError(f"Invalid export_surface_data_per_step '{export_surface_data_per_step}'. Must be one of {VALID_EXPORT_SURFACE_DATA_OPTIONS}")
    
    if export_surface_data_per_step != 'DISABLE' and surface_results_path is None:
        raise ValueError("surface_results_path is required when export_surface_data_per_step is not 'DISABLE'")

    # Build the script lines according to FlightStream documentation format
    lines = [
        "#************************************************************************",
        "#****************** Initialize and execute the solver sweeper ***********",
        "#************************************************************************",
        "EXECUTE_SOLVER_SWEEPER",
        f"ANGLE_OF_ATTACK {angle_of_attack}",
        f"SIDE_SLIP_ANGLE {side_slip_angle}",
        f"VELOCITY {velocity}",
        f"ANGLE_OF_ATTACK_START {angle_of_attack_start}",
        f"ANGLE_OF_ATTACK_STOP {angle_of_attack_stop}",
        f"ANGLE_OF_ATTACK_DELTA {angle_of_attack_delta}",
        f"SIDE_SLIP_ANGLE_START {side_slip_angle_start}",
        f"SIDE_SLIP_ANGLE_STOP {side_slip_angle_stop}",
        f"SIDE_SLIP_ANGLE_DELTA {side_slip_angle_delta}",
    ]
    
    # Add velocity parameters with correct naming based on velocity_mode
    if velocity_mode == 'MACH':
        lines.extend([
            f"MACH_START {velocity_start}",
            f"MACH_STOP {velocity_stop}",
            f"MACH_DELTA {velocity_delta}",
        ])
    else:
        lines.extend([
            f"VELOCITY_START {velocity_start}",
            f"VELOCITY_STOP {velocity_stop}",
            f"VELOCITY_DELTA {velocity_delta}",
        ])
    
    lines.append(f"EXPORT_SURFACE_DATA_PER_STEP {export_surface_data_per_step}")
    
    # Add surface results path only if export is not disabled
    if export_surface_data_per_step != 'DISABLE':
        lines.append(surface_results_path)
    
    lines.extend([
        f"CLEAR_SOLUTION_AFTER_EACH_RUN {clear_solution_after_each_run}",
        f"REFERENCE_VELOCITY_EQUALS_FREESTREAM {reference_velocity_equals_freestream}",
        f"APPEND_TO_EXISTING_SWEEP {append_to_existing_sweep}",
        results_filename
    ])
    
    script.append_lines(lines)
    return

def stability_toolbox_settings(
    rotation_frame: int = 1,
    units: str = 'PER_RADIAN',
    clear_solver_per_run: RunOptions = 'DISABLE',
    angular_rate_increment: float = 0.1
) -> None:
    """
    Set the Stability & Control (S&C) toolbox parameters.

    This function appends a command to the script state to configure the
    stability and control toolbox.

    Parameters
    ----------
    rotation_frame : int, optional
        Index of the coordinate system for rotation rates, by default 1.
    units : str, optional
        Units for dynamic stability coefficients, by default 'PER_RADIAN'.
        Must be one of `VALID_STABILITY_UNITS_LIST`.
    clear_solver_per_run : RunOptions, optional
        Enable or disable clearing the solution before each run, by default 'DISABLE'.
        Must be one of `VALID_RUN_OPTIONS`.
    angular_rate_increment : float, optional
        Incremental angular rate in rad/sec for dynamic coefficients, by default 0.1.
    """
    if not isinstance(rotation_frame, int):
        raise ValueError("`rotation_frame` must be an integer.")
    if units not in VALID_STABILITY_UNITS_LIST:
        raise ValueError(f"`units` must be one of {VALID_STABILITY_UNITS_LIST}")
    if clear_solver_per_run not in VALID_RUN_OPTIONS:
        raise ValueError(f"`clear_solver_per_run` must be one of {VALID_RUN_OPTIONS}")
    if not isinstance(angular_rate_increment, (int, float)):
        raise ValueError("`angular_rate_increment` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#****************** Set the S&C toolbox parameters here *****************",
        "#************************************************************************",
        "#",
        "STABILITY_TOOLBOX_SETTINGS",
        f"ROTATION_FRAME {rotation_frame}",
        f"UNITS {units}",
        f"CLEAR_SOLVER_PER_RUN {clear_solver_per_run}",
        f"ANGULAR_RATE_INCREMENT {angular_rate_increment}"
    ]
    script.append_lines(lines)
    return

def stability_toolbox_new_coefficient(
    frame: int,
    units: str,
    numerator: str,
    denominator: str,
    constant: float,
    name: str,
    boundaries: Union[int, List[int]]
) -> None:
    """
    Define a new Stability & Control (S&C) coefficient.

    This function appends a command to the script state to create a new
    user-defined stability and control coefficient.

    Parameters
    ----------
    frame : int
        Index of the coordinate system for the numerator variable.
    units : str
        Units of the coefficient. Must be one of `VALID_FORCE_UNITS_LIST`.
    numerator : str
        The numerator of the coefficient derivative. Must be one of
        `VALID_STABILITY_NUMERATOR_LIST`.
    denominator : str
        The denominator of the coefficient derivative. Must be one of
        `VALID_STABILITY_DENOMINATOR_LIST`.
    constant : float
        A constant multiplier for the derivative term.
    name : str
        The name of the user-defined coefficient.
    boundaries : Union[int, List[int]]
        The geometry boundaries linked to the numerator. Use -1 for all.
    """
    if units not in VALID_FORCE_UNITS_LIST:
        raise ValueError(f"`units` must be one of {VALID_FORCE_UNITS_LIST}")
    if numerator not in VALID_STABILITY_NUMERATOR_LIST:
        raise ValueError(f"`numerator` must be one of {VALID_STABILITY_NUMERATOR_LIST}")
    if denominator not in VALID_STABILITY_DENOMINATOR_LIST:
        raise ValueError(f"`denominator` must be one of {VALID_STABILITY_DENOMINATOR_LIST}")
    if not isinstance(constant, (int, float)):
        raise ValueError("`constant` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#********* Create a new S&C Coefficient *********************************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_NEW_COEFFICIENT",
        f"NAME {name}",
        f"NUMERATOR {numerator}",
        f"DENOMINATOR {denominator}",
        f"FRAME {frame}",
        f"CONSTANT {constant}",
    ]

    if isinstance(boundaries, int) and boundaries == -1:
        lines.append("BOUNDARIES -1")
    elif isinstance(boundaries, list):
        lines.append(f"BOUNDARIES {len(boundaries)}")
        lines.append(",".join(map(str, boundaries)))
    else:
        raise ValueError("`boundaries` must be -1 or a list of integers.")

    script.append_lines(lines)
    return

def stability_toolbox_delete_all() -> None:
    """
    Delete all S&C toolbox coefficients.

    This function appends a command to the script state to remove all
    user-defined stability and control coefficients.
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all S&C Toolbox coefficients *****************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_DELETE_ALL"
    ]
    script.append_lines(lines)
    return

def compute_stability_coefficients() -> None:
    """
    Compute the stability coefficients.

    This function appends a command to the script state to trigger the
    computation of all defined stability and control coefficients.
    """
    lines = [
        "#************************************************************************",
        "#****************** Compute the stability coefficients ******************",
        "#************************************************************************",
        "COMPUTE_STABILITY_COEFFICIENTS"
    ]
    script.append_lines(lines)
    return

def stability_toolbox_export(filename: str) -> None:
    """
    Export the S&C toolbox results to an external file.

    This function appends a command to the script state to save the results
    of the stability and control analysis to a file.

    Parameters
    ----------
    filename : str
        The absolute path of the file to export the results to.
    """
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string.")

    lines = [
        "#************************************************************************",
        "#*********** Export the S&C toolbox results to external file ************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_EXPORT",
        filename
    ]
    script.append_lines(lines)
    return
