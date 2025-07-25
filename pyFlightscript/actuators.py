import os
from .utils import *    
from .script import script
from .types import *
from .types import *
from typing import Union, Optional, Literal

ValidActuatorTypes = Literal['PROPELLER', 'JET_EXHAUST']
VALID_ACTUATOR_TYPES = ['PROPELLER', 'JET_EXHAUST']

def create_new_actuator(actuator_type: ValidActuatorTypes = 'PROPELLER') -> None:
    """
    Create a new actuator.

    This function appends a command to the script state to create a new
    actuator of a specified type.

    Parameters
    ----------
    actuator_type : ValidActuatorTypes, optional
        The type of actuator to create. Must be either 'PROPELLER' or
        'JET_EXHAUST'. The default is 'PROPELLER'.

    Raises
    ------
    ValueError
        If `actuator_type` is not 'PROPELLER' or 'JET_EXHAUST'.

    Examples
    --------
    >>> # Create a propeller actuator
    >>> create_new_actuator(actuator_type='PROPELLER')

    >>> # Create a jet exhaust actuator
    >>> create_new_actuator(actuator_type='JET_EXHAUST')
    """
    
    # Type and value checking
    if actuator_type not in VALID_ACTUATOR_TYPES:
        raise ValueError(f"`actuator_type` should be one of {VALID_ACTUATOR_TYPES}")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new propeller actuator ********************",
        "#************************************************************************",
        "#",
        "CREATE_NEW_ACTUATOR",
        f"TYPE {actuator_type}"
    ]

    script.append_lines(lines)
    return

def edit_actuator(
    actuator: int,
    name: str,
    actuator_type: ValidActuatorTypes,
    frame: int,
    axis: int,
    offset: Union[int, float],
    radius: Union[int, float],
    ct: Optional[Union[int, float]] = None,
    rpm: Optional[Union[int, float]] = None,
    swirl_velocity: Optional[str] = None,
    velocity: Optional[Union[int, float]] = None,
    density: Optional[Union[int, float]] = None,
    cm: Optional[Union[int, float]] = None,
) -> None:
    """
    Edit an existing actuator's properties.

    This function appends a command to the script state to modify the parameters
    of a specified actuator. The available parameters depend on the actuator type.

    Parameters
    ----------
    actuator : int
        The index of the actuator to be edited.
    name : str
        The new name to be assigned to the actuator.
    actuator_type : ValidActuatorTypes
        The type of the actuator, either 'PROPELLER' or 'JET_EXHAUST'.
    frame : int
        The index of the coordinate system for the actuator.
    axis : int
        The directional axis for the actuator disc (1 for X, 2 for Y, 3 for Z).
    offset : Union[int, float]
        The offset distance along the axis for the actuator disc.
    radius : Union[int, float]
        The radius of the actuator disc.
    ct : Optional[Union[int, float]], optional
        The thrust coefficient of the propeller (for 'PROPELLER' type only).
        Defaults to None.
    rpm : Optional[Union[int, float]], optional
        The RPM of the propeller (for 'PROPELLER' type only). Defaults to None.
    swirl_velocity : Optional[str], optional
        Enables or disables swirl velocity ('ENABLE' or 'DISABLE')
        (for 'PROPELLER' type only). Defaults to None.
    velocity : Optional[Union[int, float]], optional
        The exhaust velocity (for 'JET_EXHAUST' type only). Defaults to None.
    density : Optional[Union[int, float]], optional
        The density of the exhaust jet (for 'JET_EXHAUST' type only).
        Defaults to None.
    cm : Optional[Union[int, float]], optional
        The jet spreading coefficient (for 'JET_EXHAUST' type only).
        Defaults to None.

    Raises
    ------
    ValueError
        If input parameters have invalid types or values.

    Examples
    --------
    >>> # Edit a propeller actuator
    >>> edit_actuator(
    ...     actuator=1,
    ...     name="Prop-1",
    ...     actuator_type="PROPELLER",
    ...     frame=2,
    ...     axis=1,
    ...     offset=0.5,
    ...     radius=1.2,
    ...     ct=0.013,
    ...     rpm=7000,
    ...     swirl_velocity="ENABLE"
    ... )
    """
    
    # Type and value checking
    if not isinstance(actuator, int) or actuator <= 0:
        raise ValueError("`actuator` should be an integer greater than 0.")
    
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer greater than 0.")
    
    if actuator_type not in VALID_ACTUATOR_TYPES:
        raise ValueError(f"`actuator_type` should be one of {VALID_ACTUATOR_TYPES}")
    
    if axis not in [1, 2, 3]:
        raise ValueError("`axis` should be one of [1, 2, 3] corresponding to X, Y, Z axes.")
    
    lines = [
        "#************************************************************************",
        "#****************** Edit a propeller actuator here *********************",
        "#************************************************************************",
        "#",
        "EDIT_ACTUATOR",
        f"ACTUATOR {actuator}",
        f"NAME {name}",
        f"TYPE {actuator_type}",
        f"FRAME {frame}",
        f"AXIS {axis}",
        f"OFFSET {offset}",
        f"RADIUS {radius}",
    ]
    
    if actuator_type == 'PROPELLER':
        if ct is not None:
            lines.append(f"CT {ct}")
        if rpm is not None:
            lines.append(f"RPM {rpm}")
        if swirl_velocity is not None:
            if swirl_velocity in VALID_RUN_OPTIONS:
                lines.append(f"SWIRL_VELOCITY {swirl_velocity}")
            else:
                raise ValueError("`swirl_velocity` should be either 'ENABLE' or 'DISABLE'.")
    
    elif actuator_type == 'JET_EXHAUST':
        if velocity is not None:
            lines.append(f"VELOCITY {velocity}")
        if density is not None:
            lines.append(f"DENSITY {density}")
        if cm is not None:
            lines.append(f"CM {cm}")
    
    script.append_lines(lines)
    return

def set_prop_actuator_rpm(actuator_index: int = 1, rpm: Union[int, float] = 2000) -> None:
    """
    Set the RPM of a propeller actuator.

    This function appends a command to the script state to set the rotational
    speed (RPM) of a specified propeller actuator.

    Parameters
    ----------
    actuator_index : int, optional
        The index of the actuator to be modified. Defaults to 1.
    rpm : Union[int, float], optional
        The new RPM value for the propeller actuator. Defaults to 2000.

    Raises
    ------
    ValueError
        If `actuator_index` is not a positive integer or if `rpm` is not a
        numeric value.

    Examples
    --------
    >>> # Set the RPM of actuator 1 to 2500
    >>> set_prop_actuator_rpm(actuator_index=1, rpm=2500)

    >>> # Use default actuator index and set RPM to 3000
    >>> set_prop_actuator_rpm(rpm=3000)
    """
    
    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer value greater than 0.")
    
    if not isinstance(rpm, (int, float)):
        raise ValueError("`rpm` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the RPM of an existing actuator *****************",
        "#************************************************************************",
        "#",
        f"SET_PROP_ACTUATOR_RPM {actuator_index} {rpm}"
    ]

    script.append_lines(lines)
    return

def set_prop_actuator_profile(actuator_index: int, units_type: str, file_name: str) -> None:
    """
    Set the thrust profile of a propeller actuator from a file.

    This function appends a command to the script state to define the thrust
    profile of a specified actuator using data from an external file.

    Parameters
    ----------
    actuator_index : int
        The index of the actuator to be modified.
    units_type : str
        The units of force used in the profile file. Must be one of
        'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', or 'KILOGRAM-FORCE'.
    file_name : str
        The absolute path to the TXT file containing the thrust profile data.

    Raises
    ------
    ValueError
        If `units_type` is invalid, `actuator_index` is not a non-negative
        integer, or `file_name` is not a string.

    Examples
    --------
    >>> # Set the thrust profile for actuator 1 from a file
    >>> set_prop_actuator_profile(
    ...     actuator_index=1,
    ...     units_type='NEWTONS',
    ...     file_name='C:/path/to/thrust_profile.txt'
    ... )
    """

    # Validate parameters
    if units_type not in VALID_FORCE_UNITS_LIST:
        raise ValueError(f"`units_type` must be one of {VALID_FORCE_UNITS_LIST}")

    if not isinstance(actuator_index, int) or actuator_index < 0:
        raise ValueError("`actuator_index` should be a non-negative integer.")

    if not isinstance(file_name, str):
        raise ValueError("`file_name` must be a string indicating the path to the thrust profile file.")

    # Script command formation
    lines = [
        "#************************************************************************",
        "#********* Set the thrust profile of an existing actuator ****************",
        "#************************************************************************",
        "#",
        f"SET_PROP_ACTUATOR_PROFILE {actuator_index} {units_type}",
        file_name
    ]

    script.append_lines(lines)
    return

def set_prop_actuator_thrust(
    actuator_index: int,
    ct: Union[int, float],
    thrust_type: str = 'COEFFICIENT'
) -> None:
    """
    Set the thrust of a propeller actuator.

    This function appends a command to the script state to set the thrust of a
    propeller, either as a coefficient or as a force value in specified units.

    Parameters
    ----------
    actuator_index : int
        The index of the actuator to be modified.
    ct : Union[int, float]
        The thrust value, either as a coefficient or in force units.
    thrust_type : str, optional
        The type of thrust unit. Must be one of 'COEFFICIENT', 'NEWTONS', or
        'POUNDS'. Defaults to 'COEFFICIENT'.

    Raises
    ------
    ValueError
        If input parameters have invalid types or values.

    Examples
    --------
    >>> # Set thrust as a coefficient
    >>> set_prop_actuator_thrust(actuator_index=1, ct=0.05, thrust_type='COEFFICIENT')

    >>> # Set thrust in Newtons
    >>> set_prop_actuator_thrust(actuator_index=1, ct=150.0, thrust_type='NEWTONS')
    """
    
    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be a positive integer value.")
    
    if not isinstance(ct, (int, float)) or ct <= 0:
        raise ValueError("`ct` should be a positive integer or float value.")
    
    valid_thrust_types = ['COEFFICIENT', 'NEWTONS', 'POUNDS']
    if thrust_type not in valid_thrust_types:
        raise ValueError(f"`thrust_type` should be one of {valid_thrust_types}")
    
    lines = [
        "#************************************************************************",
        "#********* Set the thrust coefficient of an existing actuator ***********",
        "#************************************************************************",
        "#",
        f"SET_PROP_ACTUATOR_THRUST {actuator_index} {ct} {thrust_type}"
    ]

    script.append_lines(lines)
    return

def set_prop_actuator_swirl(actuator_index: int, status: str = 'DISABLE') -> None:
    """
    Enable or disable swirl velocity for a propeller actuator.

    This function appends a command to the script state to either enable or
    disable the swirl velocity effect for a specified propeller actuator.

    Parameters
    ----------
    actuator_index : int
        The index of the actuator to be modified.
    status : str, optional
        The desired status for the swirl velocity, either 'ENABLE' or 'DISABLE'.
        Defaults to 'DISABLE'.

    Raises
    ------
    ValueError
        If `actuator_index` is not a positive integer or if `status` is not
        'ENABLE' or 'DISABLE'.

    Examples
    --------
    >>> # Enable swirl velocity for actuator 1
    >>> set_prop_actuator_swirl(actuator_index=1, status='ENABLE')

    >>> # Disable swirl velocity for actuator 3
    >>> set_prop_actuator_swirl(actuator_index=3, status='DISABLE')
    """

    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer greater than 0.")
    
    if status not in VALID_RUN_OPTIONS:
        raise ValueError(f"`status` should be one of {VALID_RUN_OPTIONS}")
    
    lines = [
        "#************************************************************************",
        "#****************** Toggle the swirl velocity selection *****************",
        "#************************************************************************",
        "#",
        f"SET_PROP_ACTUATOR_SWIRL {actuator_index} {status}"
    ]

    script.append_lines(lines)
    return

def set_actuator_exhaust(
    actuator_index: int,
    del_vel: Union[int, float],
    jet_density: Union[int, float],
    jet_spreading_rate: Union[int, float],
) -> None:
    """
    Set the exhaust properties for a jet exhaust actuator.

    This function appends a command to the script state to define the exhaust
    properties, such as velocity, density, and spreading rate, for a specified
    jet exhaust actuator.

    Parameters
    ----------
    actuator_index : int
        The index of the actuator to be modified.
    del_vel : Union[int, float]
        The exhaust velocity increment (above freestream) of the jet.
    jet_density : Union[int, float]
        The density of the jet flow.
    jet_spreading_rate : Union[int, float]
        The jet spreading coefficient.

    Raises
    ------
    ValueError
        If `actuator_index` is not a positive integer or if `del_vel`,
        `jet_density`, or `jet_spreading_rate` are not numeric.

    Examples
    --------
    >>> # Set exhaust properties for actuator 2
    >>> set_actuator_exhaust(
    ...     actuator_index=2,
    ...     del_vel=100.0,
    ...     jet_density=0.5,
    ...     jet_spreading_rate=0.1
    ... )
    """

    # Validate parameters
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be a positive integer.")
    if not isinstance(del_vel, (int, float)):
        raise ValueError("`del_vel` should be a number (integer or float).")
    if not isinstance(jet_density, (int, float)):
        raise ValueError("`jet_density` should be a number (integer or float).")
    if not isinstance(jet_spreading_rate, (int, float)):
        raise ValueError("`jet_spreading_rate` should be a number (integer or float).")

    # Prepare command
    lines = [
        "#************************************************************************",
        "#********************** Set the exhaust actuator properties *************",
        "#************************************************************************",
        "#",
        f"SET_ACTUATOR_EXHAUST {actuator_index} {del_vel} {jet_density} {jet_spreading_rate}"
    ]

    # Assuming script.append_lines is a function that adds these lines to the script
    script.append_lines(lines)
    return

def enable_actuator(actuator_id: int) -> None:
    """
    Enable an existing actuator.

    This function appends a command to the script state to enable a specified
    actuator by its ID.

    Parameters
    ----------
    actuator_id : int
        The ID of the actuator to be enabled.

    Raises
    ------
    ValueError
        If `actuator_id` is not a non-negative integer.

    Examples
    --------
    >>> # Enable actuator with ID 2
    >>> enable_actuator(actuator_id=2)
    """
    
    # Type and value checking
    if not isinstance(actuator_id, int) or actuator_id < 0:
        raise ValueError("`actuator_id` should be a non-negative integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Enable an existing actuator *************************",
        "#************************************************************************",
        "#",
        f"ENABLE_ACTUATOR {actuator_id}"
    ]

    script.append_lines(lines)
    return

def disable_actuator(actuator_id: int) -> None:
    """
    Disable an existing actuator.

    This function appends a command to the script state to disable a specified
    actuator by its ID.

    Parameters
    ----------
    actuator_id : int
        The ID of the actuator to be disabled.

    Raises
    ------
    ValueError
        If `actuator_id` is not an integer.

    Examples
    --------
    >>> # Disable actuator with ID 2
    >>> disable_actuator(actuator_id=2)
    """
    
    # Type and value checking
    if not isinstance(actuator_id, int):
        raise ValueError("`actuator_id` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Disable an existing actuator ************************",
        "#************************************************************************",
        "#",
        f"DISABLE_ACTUATOR {actuator_id}"
    ]

    script.append_lines(lines)
    return

def delete_actuator(actuator_index: int) -> None:
    """
    Delete an existing actuator.

    This function appends a command to the script state to delete a specified
    actuator by its index.

    Parameters
    ----------
    actuator_index : int
        The index of the actuator to be deleted.

    Raises
    ------
    ValueError
        If `actuator_index` is not a positive integer.

    Examples
    --------
    >>> # Delete actuator with index 1
    >>> delete_actuator(actuator_index=1)
    """
    
    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an actuator **********************************",
        "#************************************************************************",
        "#",
        f"DELETE ACTUATOR {actuator_index}"
    ]

    script.append_lines(lines)
    return
