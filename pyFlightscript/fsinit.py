from .utils import *    
from .script import script
from .types import RunOptions, ValidUnits, VALID_RUN_OPTIONS, VALID_UNITS_LIST, VALID_FORCE_UNITS_LIST

def open_fsm(fsm_filepath: str, reset_parallel_cores: RunOptions = 'DISABLE', load_solver_initialization: RunOptions = 'ENABLE') -> None:
    """
    Opens a FlightStream file with specified settings.
    
    Args:
        fsm_filepath (str): Path to the FlightStream file to open
        reset_parallel_cores (str): 'ENABLE' to reset parallel core count, 'DISABLE' to use existing. Defaults to 'DISABLE'.
        load_solver_initialization (str): 'ENABLE' to load solver initialization from file, 'DISABLE' to skip. Defaults to 'ENABLE'.
    """
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
        fsm_filepath,  # File path and name
        f"LOAD_SOLVER_INITIALIZATION {load_solver_initialization}"
    ]

    script.append_lines(lines)
    return

def stop_script():
    """
    Writes specific lines indicating a script stop.
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

def print(message: str = "Hello from FlightStream!"):
    """
    Print a user-defined message to the log.
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

def save_as_fsm(fsm_filepath: str):
    """
    Appends lines to script state to save an existing simulation file,
    using the path from 'fsm_filepath'.
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

def new_simulation():
    """
    Appends lines to script state to create a new simulation.
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

def set_significant_digits(digits: int = 5):
    """
    Appends lines to script state to set the number of significant digits.
    
    :param : Path to the script file.
    :param digits: Number of significant digits.
    """
    lines = [
        "#************************************************************************",
        "#****************** Set significant digits ******************************",
        "#************************************************************************",
        "#",
        f"SET_SIGNIFICANT_DIGITS {digits}"
    ]

    script.append_lines(lines)
    return

def set_vertex_merge_tolerance(tolerance: float = 1e-5):
    """
    Appends lines to script state to set the vertex merge tolerance.
    
    :param : Path to the script file.
    :param tolerance: Vertex merge tolerance value.
    """
    lines = [
        "#************************************************************************",
        "#****************** Set vertex merge tolerance **************************",
        "#************************************************************************",
        "#",
        f"SET_VERTEX_MERGE_TOLERANCE {tolerance}"
    ]

    script.append_lines(lines)
    return

def set_simulation_length_units(units: ValidUnits = 'METER'):
    """
    Appends lines to script state to set the simulation length scale units.
    Checks if the provided unit is valid.
    
    :param : Path to the script file.
    :param units: Desired simulation length unit.
    :raises ValueError: If the provided unit is not valid.
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

def set_trailing_edge_sweep_angle(angle: float = 45.):
    """
    Appends lines to script state to set the trailing edge sweep angle.
    Checks if the provided angle is within the valid range.
    
    :param : Path to the script file.
    :param angle: Desired trailing edge sweep angle in degrees.
    :raises ValueError: If the provided angle is not within [0, 90].
    """
    if not (0 <= angle <= 90):
        raise ValueError("Invalid angle: {}. Must be in the range [0, 90].".format(angle))

    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set trailing edge sweep angle ***********************",
        "#************************************************************************",
        "#",
        f"SET_TRAILING_EDGE_SWEEP_ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def set_trailing_edge_bluntness_angle(angle: float = 85.):
    """
    Appends lines to script state to set the trailing edge bluntness angle.
    Checks if the provided angle is within the valid range.
    
    :param : Path to the script file.
    :param angle: Desired trailing edge bluntness angle in degrees.
    :raises ValueError: If the provided angle is not within [45, 179].
    """
    if not (45 <= angle <= 179):
        raise ValueError("Invalid angle: {}. Must be in the range [45, 179].".format(angle))

    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set trailing edge bluntness angle *******************",
        "#************************************************************************",
        "#",
        f"SET_TRAILING_EDGE_BLUNTNESS_ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def set_base_region_bending_angle(angle: float = 25.):
    """
    Appends lines to script state to set the base region bending angle.
    Checks if the provided angle is within the valid range.
    
    :param : Path to the script file.
    :param angle: Desired base region bending angle in degrees.
    :raises ValueError: If the provided angle is not within [0, 90].
    """
    if not (0 <= angle <= 90):
        raise ValueError("Invalid angle: {}. Must be in the range [0, 90].".format(angle))

    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set base region bending angle ***********************",
        "#************************************************************************",
        "#",
        f"SET_BASE_REGION_BENDING_ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def run_script(script_filepath: str):
    """
    Appends lines to script state to run a script from within another script.
    
    Args:
        script_filepath (str): Path to the script file to run.
    """
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
