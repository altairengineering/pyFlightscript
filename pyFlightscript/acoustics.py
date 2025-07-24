from .utils import *    
from .script import script    
from .types import *

def acoustic_sources(enable: bool = True) -> None:
    """
    Enable or disable acoustic sources during solver initialization.

    This function appends a command to the script state to control whether
    acoustic sources are enabled or disabled when the solver is initialized.

    Parameters
    ----------
    enable : bool, optional
        The desired enable for the acoustic sources. Must be either 'ENABLE' or
        'DISABLE'. The default is True.

    Raises
    ------
    ValueError
        If `enable` is not a boolean value.

    Examples
    --------
    >>> # Enable acoustic sources
    >>> acoustic_sources(enable=True)

    >>> # Disable acoustic sources
    >>> acoustic_sources(enable=False)
    """
    
    # Type and value checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value.")
    
    lines = [
        "#************************************************************************",
        "#******** Enable acoustic sources during solver initialization **********",
        "#************************************************************************",
        "#",
        f"ACOUSTIC_SOURCES {enable}"
    ]

    script.append_lines(lines)
    return

def create_new_acoustic_observer(name: str, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
    """
    Create a new acoustic observer.

    This function appends a command to the script state to create a new
    acoustic observer with a specified name and coordinates.

    Parameters
    ----------
    name : str
        The name for the new acoustic observer.
    x : float, optional
        The x-coordinate of the observer. The default is 0.0.
    y : float, optional
        The y-coordinate of the observer. The default is 0.0.
    z : float, optional
        The z-coordinate of the observer. The default is 0.0.

    Raises
    ------
    ValueError
        If `name` is not a string or if `x`, `y`, or `z` are not numeric.

    Examples
    --------
    >>> # Create an observer at a specific location
    >>> create_new_acoustic_observer(name='Observer-1', x=10.0, y=5.0, z=2.0)

    >>> # Create an observer at the origin
    >>> create_new_acoustic_observer(name='OriginObserver')
    """
    
    # Type and value checking
    if not isinstance(name, str):
        raise ValueError("`name` should be a string.")
    
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise ValueError("Coordinates `x`, `y`, and `z` should be numeric values (int or float).")
    
    lines = [
        "#************************************************************************",
        "#******************* Create new acoustic observer ***********************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_ACOUSTIC_OBSERVER {name} {x} {y} {z}"
    ]

    script.append_lines(lines)
    return

def acoustic_observers_import(file_path: str) -> None:
    """
    Import acoustic observers from a file.

    This function appends a command to the script state to import a list of
    acoustic observers from a specified file.

    Parameters
    ----------
    file_path : str
        The absolute path to the file containing the observer data.

    Raises
    ------
    ValueError
        If `file_path` is not a string.

    Examples
    --------
    >>> # Import observers from a text file
    >>> acoustic_observers_import(file_path='C:/path/to/Observers.txt')
    """
    
    # Type and value checking
    if not isinstance(file_path, str):
        raise ValueError("`file_path` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#****************** Import acoustic observers from file *****************",
        "#************************************************************************",
        "#",
        "ACOUSTIC_OBSERVERS_IMPORT",
        file_path
    ]
    
    script.append_lines(lines)
    return

def delete_acoustic_observer(observer_index: int) -> None:
    """
    Delete an acoustic observer by its index.

    This function appends a command to the script state to delete an existing
    acoustic observer based on its index in the acoustic toolbox UI tree.

    Parameters
    ----------
    observer_index : int
        The index of the observer to be deleted.

    Raises
    ------
    ValueError
        If `observer_index` is not an integer.

    Examples
    --------
    >>> # Delete the observer at index 2
    >>> delete_acoustic_observer(observer_index=2)
    """
    
    # Type and value checking
    if not isinstance(observer_index, int):
        raise ValueError("`observer_index` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#******************* Delete acoustic observer ***************************",
        "#************************************************************************",
        "#",
        "DELETE_ACOUSTIC_OBSERVER",
        str(observer_index)
    ]
    
    script.append_lines(lines)
    return

def delete_all_acoustic_observers():
    """
    Appends lines to script state to delete all acoustic observers.
    


    Example usage:
    >>> delete_all_acoustic_observers()
    """
    
    lines = [
        "#************************************************************************",
        "#******************* Delete all acoustic observers **********************",
        "#************************************************************************",
        "#",
        "DELETE_ALL_ACOUSTIC_OBSERVERS"
    ]

    script.append_lines(lines)
    return

def set_acoustic_observer_time(initial_time: float = 0.0, final_time: float = 0.2, time_steps: int = 300) -> None:
    """
    Set the time parameters for acoustic observers.

    This function appends a command to the script state to define the time
    range and resolution for the acoustic signal computation.

    Parameters
    ----------
    initial_time : float, optional
        The initial time for the observer signal in seconds. The default is 0.0.
    final_time : float, optional
        The final time for the observer signal in seconds. The default is 0.2.
    time_steps : int, optional
        The total number of time steps between the initial and final times.
        The default is 300.

    Raises
    ------
    ValueError
        If `initial_time` or `final_time` are not numeric, or if `time_steps`
        is not an integer.

    Examples
    --------
    >>> # Use default time parameters
    >>> set_acoustic_observer_time()

    >>> # Set a custom time range and number of steps
    >>> set_acoustic_observer_time(initial_time=0.1, final_time=0.5, time_steps=500)
    """
    
    # Type and value checking
    if not isinstance(initial_time, (int, float)):
        raise ValueError("`initial_time` should be an integer or float value.")
    
    if not isinstance(final_time, (int, float)):
        raise ValueError("`final_time` should be an integer or float value.")
    
    if not isinstance(time_steps, int):
        raise ValueError("`time_steps` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#******************* Set acoustic observer time parameters **************",
        "#************************************************************************",
        "#",
        f"SET_ACOUSTIC_OBSERVER_TIME {initial_time} {final_time} {time_steps}"
    ]

    script.append_lines(lines)
    return

def compute_acoustic_signals() -> None:
    """
    Compute acoustic signals at all observers.

    This function appends a command to the script state to trigger the computation
    of acoustic signals for all configured observers.

    Examples
    --------
    >>> # Compute acoustic signals
    >>> compute_acoustic_signals()
    """
    
    lines = [
        "#************************************************************************",
        "#******************* Compute acoustic signals at all observers **********",
        "#************************************************************************",
        "#",
        "COMPUTE_ACOUSTIC_SIGNALS"
    ]
    
    script.append_lines(lines)
    return

def export_acoustic_signals(filename: str) -> None:
    """
    Export acoustic signals at all observers to an external file.

    This function appends a command to the script state to save the computed
    acoustic signals for all configured observers to a specified file.

    Parameters
    ----------
    filename : str
        The absolute path to the file where the acoustic signals will be saved.

    Raises
    ------
    ValueError
        If `filename` is not a string.

    Examples
    --------
    >>> # Export acoustic signals to a file
    >>> export_acoustic_signals(filename='C:/path/to/output.txt')
    """
    
    # Type checking
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#******* Export acoustic signals at all observers to external file ******",
        "#************************************************************************",
        "#",
        "EXPORT_ACOUSTIC_SIGNALS",
        f"{filename}"
    ]
    
    script.append_lines(lines)
    return

def create_acoustic_section(frame: int = 1, plane: str = 'XZ', offset: float = -2.0,
                            radial_observers: int = 20, azimuth_observers: int = 40, inner_radius: float = 0.0,
                            outer_radius: float = 3.0, storage_path: str = "C:\\...\\Acoustic_Output\\") -> None:
    """
    Create and export acoustic section signals.
    

    This function appends a command to the script state to create an acoustic
    section with specified parameters and export the computed signals to a
    specified folder.
    
    Examples
    --------
    >>> # Create an acoustic section with default parameters
    >>> create_acoustic_section()

    >>> # Create an acoustic section with custom parameters
    >>> create_acoustic_section(frame=2, plane='XY', offset=-1.0, radial_observers=15, azimuth_observers=30, inner_radius=0.5, outer_radius=2.5, storage_path='C:/path/to/Acoustic_Output/')
    """

    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}")
    
    if not all(isinstance(x, (int, float)) for x in [offset, inner_radius, outer_radius]):
        raise ValueError("`offset`, `inner_radius` and `outer_radius` should be numeric values.")
    
    if not all(isinstance(x, int) for x in [radial_observers, azimuth_observers]):
        raise ValueError("`radial_observers` and `azimuth_observers` should be integer values.")
    
    lines = [
        "#************************************************************************",
        "#******************* Create & export acoustic section signals ***********",
        "#************************************************************************",
        "#",
        "CREATE_ACOUSTIC_SECTION",
        f"FRAME {frame}",
        f"PLANE {plane}",
        f"OFFSET {offset}",
        f"RADIAL_OBSERVERS {radial_observers}",
        f"AZIMUTH_OBSERVERS {azimuth_observers}",
        f"INNER_RADIUS {inner_radius}",
        f"OUTER_RADIUS {outer_radius}",
        f"STORAGE_PATH {storage_path}"
    ]

    script.append_lines(lines)
    return
