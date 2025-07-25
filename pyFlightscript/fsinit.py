from .utils import *    
from .script import script
from .types import *
from .types import RunOptions, ValidUnits, VALID_RUN_OPTIONS, VALID_UNITS_LIST, VALID_FORCE_UNITS_LIST

def open_fsm(
    fsm_filepath: str,
    reset_parallel_cores: RunOptions = 'DISABLE',
    load_solver_initialization: RunOptions = 'ENABLE'
) -> None:
    """
    Open a FlightStream file.

    This function appends a command to the script state to open a
    FlightStream (`.fsm`) file with specified options.

    Parameters
    ----------
    fsm_filepath : str
        The absolute path to the FlightStream file to open.
    reset_parallel_cores : RunOptions, optional
        'ENABLE' to reset the parallel core count, 'DISABLE' to use the
        existing setting. Defaults to 'DISABLE'.
    load_solver_initialization : RunOptions, optional
        'ENABLE' to load solver initialization data from the file,
        'DISABLE' to skip. Defaults to 'ENABLE'.

    Raises
    ------
    FileNotFoundError
        If `fsm_filepath` does not exist.
    ValueError
        If `reset_parallel_cores` or `load_solver_initialization` are not
        valid `RunOptions`.

    Examples
    --------
    >>> # Open a FlightStream file with default settings
    >>> open_fsm(fsm_filepath='C:/path/to/simulation.fsm')

    >>> # Open a file and reset the parallel core count
    >>> open_fsm(
    ...     fsm_filepath='C:/path/to/simulation.fsm',
    ...     reset_parallel_cores='ENABLE'
    ... )
    """
    check_file_existence(fsm_filepath)
    
    if reset_parallel_cores not in VALID_RUN_OPTIONS:
        raise ValueError(f"`reset_parallel_cores` should be one of {VALID_RUN_OPTIONS}")

    if load_solver_initialization not in VALID_RUN_OPTIONS:
        raise ValueError(f"`load_solver_initialization` should be one of {VALID_RUN_OPTIONS}")
        
    lines = [
        "#************************************************************************",
        "#****************** Open an existing simulation file ********************",
        "#************************************************************************",
        "#",
        "OPEN",
        fsm_filepath,
        f"LOAD_SOLVER_INITIALIZATION {load_solver_initialization}"
    ]

    script.append_lines(lines)
    return

def stop_script() -> None:
    """
    Stop the script at the current location.

    This function appends a command to the script state that halts the
    execution of the script at the point where this function is called.

    Examples
    --------
    >>> # Stop the script execution
    >>> stop_script()
    """
    lines = [
        "#************************************************************************",
        "#*********** Stop a script at this location in the script file **********",
        "#************************************************************************",
        "#",
        "STOP"
    ]

    script.append_lines(lines)
    return

def print_message(message: str = "Hello from FlightStream!") -> None:
    """
    Print a user-defined message to the log.

    This function appends a command to the script state to print a specified
    message to the FlightStream log file.

    Parameters
    ----------
    message : str, optional
        The message to be printed in the log. Defaults to "Hello from
        FlightStream!".

    Examples
    --------
    >>> # Print a custom message to the log
    >>> print_message(message="Starting simulation phase 1.")
    """
    lines = [
        "#************************************************************************",
        "#**************** Print a user-defined message to the log ***************",
        "#************************************************************************",
        "#",
        f"PRINT {message}"
    ]

    script.append_lines(lines)
    return

def save_as_fsm(fsm_filepath: str) -> None:
    """
    Save the current simulation to a FlightStream file.

    This function appends a command to the script state to save the current
    simulation state to a specified `.fsm` file.

    Parameters
    ----------
    fsm_filepath : str
        The absolute path where the simulation file will be saved.

    Examples
    --------
    >>> # Save the simulation to a file
    >>> save_as_fsm(fsm_filepath='C:/path/to/new_simulation.fsm')
    """
    lines = [
        "#************************************************************************",
        "#****************** Save an existing simulation file ********************",
        "#************************************************************************",
        "#",
        "SAVEAS",
        fsm_filepath
    ]

    script.append_lines(lines)
    return

def new_simulation() -> None:
    """
    Create a new simulation.

    This function appends a command to the script state to initialize a new,
    empty simulation.

    Examples
    --------
    >>> # Start a new simulation
    >>> new_simulation()
    """
    lines = [
        "#************************************************************************",
        "#****************** Create a new simulation *****************************",
        "#************************************************************************",
        "#",
        "NEW_SIMULATION"
    ]

    script.append_lines(lines)
    return

def set_significant_digits(digits: int = 5) -> None:
    """
    Set the number of significant digits for output.

    This function appends a command to the script state to set the number
    of significant digits used in output files.

    Parameters
    ----------
    digits : int, optional
        The number of significant digits. Defaults to 5.

    Raises
    ------
    ValueError
        If `digits` is not a positive integer.

    Examples
    --------
    >>> # Set the significant digits to 7
    >>> set_significant_digits(digits=7)
    """
    if not isinstance(digits, int) or digits <= 0:
        raise ValueError("`digits` must be a positive integer.")
        
    lines = [
        "#************************************************************************",
        "#****************** Set significant digits ******************************",
        "#************************************************************************",
        "#",
        f"SET_SIGNIFICANT_DIGITS {digits}"
    ]

    script.append_lines(lines)
    return

def set_vertex_merge_tolerance(tolerance: float = 1e-5) -> None:
    """
    Set the vertex merge tolerance.

    This function appends a command to the script state to set the tolerance
    used for merging vertices.

    Parameters
    ----------
    tolerance : float, optional
        The vertex merge tolerance value. Defaults to 1e-5.

    Raises
    ------
    ValueError
        If `tolerance` is not a numeric value.

    Examples
    --------
    >>> # Set the vertex merge tolerance to 1e-6
    >>> set_vertex_merge_tolerance(tolerance=1e-6)
    """
    if not isinstance(tolerance, (int, float)):
        raise ValueError("`tolerance` must be a numeric value.")
        
    lines = [
        "#************************************************************************",
        "#****************** Set vertex merge tolerance **************************",
        "#************************************************************************",
        "#",
        f"SET_VERTEX_MERGE_TOLERANCE {tolerance}"
    ]

    script.append_lines(lines)
    return

def set_simulation_length_units(units: ValidUnits = 'METER') -> None:
    """
    Set the simulation length scale units.

    This function appends a command to the script state to set the length
    units for the entire simulation.

    Parameters
    ----------
    units : ValidUnits, optional
        The desired simulation length unit. Defaults to 'METER'.

    Raises
    ------
    ValueError
        If the provided `units` is not a valid unit type.

    Examples
    --------
    >>> # Set simulation length units to inches
    >>> set_simulation_length_units(units='INCH')
    """
    if units not in VALID_UNITS_LIST:
        raise ValueError(f"`units` should be one of {VALID_UNITS_LIST}")

    lines = [
        "#************************************************************************",
        "#****************** Set simulation length scale units *******************",
        "#************************************************************************",
        "#",
        f"SET_SIMULATION_LENGTH_UNITS {units}"
    ]

    script.append_lines(lines)
    return

def set_trailing_edge_sweep_angle(angle: float = 45.0) -> None:
    """
    Set the trailing edge sweep angle.

    This function appends a command to the script state to set the trailing
    edge sweep angle used for identifying trailing edges.

    Parameters
    ----------
    angle : float, optional
        The desired trailing edge sweep angle in degrees. Must be between
        0 and 90. Defaults to 45.0.

    Raises
    ------
    ValueError
        If the `angle` is not a numeric value or is outside the valid
        range [0, 90].

    Examples
    --------
    >>> # Set the trailing edge sweep angle to 60 degrees
    >>> set_trailing_edge_sweep_angle(angle=60.0)
    """
    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    if not (0 <= angle <= 90):
        raise ValueError(f"Invalid angle: {angle}. Must be in the range [0, 90].")

    lines = [
        "#************************************************************************",
        "#****************** Set trailing edge sweep angle ***********************",
        "#************************************************************************",
        "#",
        f"SET_TRAILING_EDGE_SWEEP_ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def set_trailing_edge_bluntness_angle(angle: float = 85.0) -> None:
    """
    Set the trailing edge bluntness angle.

    This function appends a command to the script state to set the angle
    used for identifying blunt trailing edges.

    Parameters
    ----------
    angle : float, optional
        The desired trailing edge bluntness angle in degrees. Must be
        between 45 and 179. Defaults to 85.0.

    Raises
    ------
    ValueError
        If the `angle` is not a numeric value or is outside the valid
        range [45, 179].

    Examples
    --------
    >>> # Set the trailing edge bluntness angle to 90 degrees
    >>> set_trailing_edge_bluntness_angle(angle=90.0)
    """
    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    if not (45 <= angle <= 179):
        raise ValueError(f"Invalid angle: {angle}. Must be in the range [45, 179].")

    lines = [
        "#************************************************************************",
        "#****************** Set trailing edge bluntness angle *******************",
        "#************************************************************************",
        "#",
        f"SET_TRAILING_EDGE_BLUNTNESS_ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def set_base_region_bending_angle(angle: float = 25.0) -> None:
    """
    Set the base region bending angle.

    This function appends a command to the script state to set the bending
    angle used for identifying base regions.

    Parameters
    ----------
    angle : float, optional
        The desired base region bending angle in degrees. Must be between
        0 and 90. Defaults to 25.0.

    Raises
    ------
    ValueError
        If the `angle` is not a numeric value or is outside the valid
        range [0, 90].

    Examples
    --------
    >>> # Set the base region bending angle to 30 degrees
    >>> set_base_region_bending_angle(angle=30.0)
    """
    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    if not (0 <= angle <= 90):
        raise ValueError(f"Invalid angle: {angle}. Must be in the range [0, 90].")

    lines = [
        "#************************************************************************",
        "#****************** Set base region bending angle ***********************",
        "#************************************************************************",
        "#",
        f"SET_BASE_REGION_BENDING_ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def run_script(script_filepath: str) -> None:
    """
    Run a script from within another script.

    This function appends a command to the script state to execute another
    script file.

    Parameters
    ----------
    script_filepath : str
        The absolute path to the script file to be executed.

    Raises
    ------
    FileNotFoundError
        If `script_filepath` does not exist.

    Examples
    --------
    >>> # Run another script
    >>> run_script(script_filepath='C:/path/to/another_script.txt')
    """
    check_file_existence(script_filepath)
    
    lines = [
        "#************************************************************************",
        "#**************** Call a script from within another script **************",
        "#************************************************************************",
        "#",
        "RUN_SCRIPT",
        script_filepath
    ]

    script.append_lines(lines)
    return
