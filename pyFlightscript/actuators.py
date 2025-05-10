import os
from .utils import *    
from .script import script

def create_new_actuator(actuator_type='PROPELLER'):
    """
    Appends lines to script state to create a new actuator.
    
    Example usage:
    create_new_actuator()
    

    :param actuator_type: Type of the actuator, either 'PROPELLER' or 'JET_EXHAUST'.
    """
    
    # Type and value checking
    valid_types = ['PROPELLER', 'JET_EXHAUST']
    if actuator_type not in valid_types:
        raise ValueError(f"`actuator_type` should be one of {valid_types}")
    
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

def edit_actuator(actuator, name, actuator_type, frame, axis, 
                  offset, radius, ct=None, rpm=None, swirl_velocity=None, 
                  velocity=None, density=None, cm=None):
    """
    Example usage:
        edit_actuator(, 1, "Prop-1", "PROPELLER", 2, 1, 0.5, 
                      1.2, ct=0.013, rpm=7000, swirl_velocity="ENABLE")
    
    Appends lines to script state to edit an actuator.
    

    :param actuator: Index of the actuator to be edited.
    :param name: Name to be assigned to the selected actuator.
    :param actuator_type: Type of the actuator (PROPELLER or JET_EXHAUST).
    :param frame: Index of the coordinate system to be used for this actuator.
    :param axis: Directional axis for the actuator disc.
    :param offset: Offset distance along the axis for the actuator disc.
    :param radius: Radius of the actuator disc.
    :param ct: Thrust coefficient of the propeller (for PROPELLER type only).
    :param rpm: RPM of the propeller (for PROPELLER type only).
    :param swirl_velocity: ENABLE/DISABLE swirl velocity (for PROPELLER type only).
    :param velocity: Exhaust velocity (for JET_EXHAUST type only).
    :param density: Density of the exhaust jet (for JET_EXHAUST type only).
    :param cm: Jet spreading coefficient (for JET_EXHAUST type only).
    """
    
    # Type and value checking
    if not isinstance(actuator, int) or actuator <= 0:
        raise ValueError("`actuator` should be an integer greater than 0.")
    
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer greater than 0.")
    
    if actuator_type not in ['PROPELLER', 'JET_EXHAUST']:
        raise ValueError("`actuator_type` should be either 'PROPELLER' or 'JET_EXHAUST'.")
    
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
        if swirl_velocity in ["ENABLE", "DISABLE"]:
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

def set_prop_actuator_rpm(actuator_index=1, rpm=2000):
    """
    Appends lines to script state to set the RPM of an actuator.
    
    Example usage:
    set_prop_actuator_rpm(, 2, -3400)


    :param actuator_index: Index of the actuator whose properties are being set.
    :param rpm: RPM of the propeller actuator.
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

def set_prop_actuator_profile(actuator_index, units_type, file_name):
    """
    Appends lines to script state to set the thrust profile of an actuator.

    :param actuator_index: Index of the actuator.
    :param units_type: Type of force units (e.g., 'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE').
    :param file_name: Path and name of the TXT file containing the thrust profile.
    """

    # Validate parameters
    valid_units = ['NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE']
    if units_type not in valid_units:
        raise ValueError(f"`units_type` must be one of {valid_units}")

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

def set_prop_actuator_thrust(actuator_index, ct, thrust_type='COEFFICIENT'):
    """
    Appends lines to script state to set the thrust coefficient of an existing actuator.
    

    :param actuator_index: Index of the actuator whose properties are being set.
    :param ct: Thrust coefficient of the propeller.
    :param thrust_type: Units for the thrust force.

    Example usage:
    set_prop_actuator_thrust(, 2, 0.034)
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

def set_prop_actuator_swirl(actuator_index, status='DISABLE'):
    """
    Appends lines to script state to toggle the swirl velocity selection.
    

    :param actuator_index: Index of the actuator whose properties are being set.
    :param status: Either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    set_prop_actuator_swirl(, 3)
    """

    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer greater than 0.")
    
    valid_statuses = ['ENABLE', 'DISABLE']
    if status not in valid_statuses:
        raise ValueError(f"`status` should be one of {valid_statuses}")
    
    lines = [
        "#************************************************************************",
        "#****************** Toggle the swirl velocity selection *****************",
        "#************************************************************************",
        "#",
        f"SET_PROP_ACTUATOR_SWIRL {actuator_index} {status}"
    ]

    script.append_lines(lines)
    return

def set_actuator_exhaust(actuator_index, del_vel, jet_density, jet_spreading_rate):
    """
    Appends lines to script state to set exhaust properties for a specified actuator.

    :param actuator_index: Index of the actuator (>0) of the propeller type.
    :param del_vel: Exhaust velocity increment (above freestream) of the jet.
    :param jet_density: Density of the jet flow.
    :param jet_spreading_rate: Jet spreading coefficient.
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

def enable_actuator(actuator_id):
    """
    Appends lines to script state to enable an existing actuator.
    
    Example usage:
    >>> enable_actuator(, 2)
    

    :param actuator_id: ID of the actuator to be enabled.
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

def disable_actuator(actuator_id):
    """
    Appends lines to script state to disable an existing actuator.
    
    Example usage:
    disable_actuator(, 2)
    

    :param actuator_id: ID of the actuator to disable.
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

def delete_actuator(actuator_index):
    """
    Appends lines to script state to delete an actuator.
    
    Example usage:
    delete_actuator(, 1)


    :param actuator_index: Index of the actuator to be deleted.
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
