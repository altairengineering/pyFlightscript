import os
from .utils import *    
from .script import script
from .types import *

def set_freestream(
    freestream_type: str,
    profile_path: str = None,
    frame: int = None,
    axis: str = None,
    angular_velocity: float = None
):
    """
    Appends lines to script state to set a freestream velocity type.

    :param freestream_type: Type of the freestream ('CONSTANT', 'CUSTOM', or 'ROTATION').
    :param profile_path: (Optional) Path to the custom velocity profile. Needed for 'CUSTOM' type.
    :param frame: (Optional) Index of the coordinate system used for defining the rotation. Needed for 'ROTATION' type.
    :param axis: (Optional) Axis of the chosen coordinate system used for rotation ('X', 'Y', or 'Z'). Needed for 'ROTATION' type.
    :param angular_velocity: (Optional) Rotational velocity in rad/sec. Needed for 'ROTATION' type.

    Example usage:
    set_freestream('CONSTANT')
    set_freestream('CUSTOM', profile_path='C:/.../Custom_freestream_profile.txt')
    set_freestream('ROTATION', frame=1, axis='X', angular_velocity=-0.2)
    """

    # Type and value checking
    valid_types = ['CONSTANT', 'CUSTOM', 'ROTATION']
    if not isinstance(freestream_type, str):
        raise TypeError("`freestream_type` must be a string.")
    if freestream_type not in valid_types:
        raise ValueError(f"`freestream_type` should be one of {valid_types}")

    lines = []
    if freestream_type == 'CONSTANT':
        lines.extend([
            "#************************************************************************",
            "#**************** Set a constant free-stream velocity *******************",
            "#************************************************************************",
            "#",
            "SET_FREESTREAM CONSTANT"
        ])

    elif freestream_type == 'CUSTOM':
        if profile_path is None:
            raise ValueError("For `CUSTOM` freestream_type, `profile_path` must be provided.")
        if not isinstance(profile_path, str):
            raise TypeError("`profile_path` must be a string when `freestream_type` is 'CUSTOM'.")
        lines.extend([
            "#************************************************************************",
            "#*************** Set a custom free-stream velocity ********************",
            "#************************************************************************",
            "#",
            "SET_FREESTREAM CUSTOM",
            profile_path
        ])

    else:  # ROTATION
        if frame is None or axis is None or angular_velocity is None:
            raise ValueError("For `ROTATION` freestream_type, `frame`, `axis`, and `angular_velocity` must be provided.")
        if not isinstance(frame, int):
            raise TypeError("`frame` must be an integer when `freestream_type` is 'ROTATION'.")
        valid_axes = ['X', 'Y', 'Z']
        if not isinstance(axis, str):
            raise TypeError("`axis` must be a string when `freestream_type` is 'ROTATION'.")
        if axis not in valid_axes:
            raise ValueError(f"`axis` should be one of {valid_axes}")
        if not isinstance(angular_velocity, (int, float)):
            raise TypeError("`angular_velocity` must be a number (int or float) when `freestream_type` is 'ROTATION'.")

        lines.extend([
            "#************************************************************************",
            "#*************** Set a rotational free-stream velocity ******************",
            "#************************************************************************",
            "#",
            f"SET_FREESTREAM ROTATION {frame} {axis} {angular_velocity}"
        ])

    script.append_lines(lines)
    return

def fluid_properties(
    density: float = 1.225,
    pressure: float = 101325.0,
    sonic_velocity: float = 340.0,
    temperature: float = 288.15,
    viscosity: float = 1.789e-5
):
    """
    Appends lines to script state to set the fluid properties.
    
    Example usage:
        fluid_properties()
    
    :param density: Density value (kg/m^3).
    :param pressure: Static pressure value (Pa).
    :param sonic_velocity: Sonic velocity (m/sec).
    :param temperature: Temperature value (K).
    :param viscosity: Viscosity value (Pa-sec).
    """

    lines = [
        "#************************************************************************",
        "#********* Set the fluid properties *************************************",
        "#************************************************************************",
        "#",
        "FLUID_PROPERTIES",
        f"DENSITY {density}",
        f"PRESSURE {pressure}",
        f"SONIC_VELOCITY {sonic_velocity}",
        f"TEMPERATURE {temperature}",
        f"VISCOSITY {viscosity}"
    ]

    script.append_lines(lines)
    return

def air_altitude(altitude: float = 15000.0):
    """
    Appends lines to script state to set fluid (air) properties based on altitude.

    Example usage:
    air_altitude()


    :param altitude: Altitude value in feet.
    """
    
    lines = [
        "#************************************************************************",
        "#********* Set the fluid (air) properties based on altitude *************",
        "#************************************************************************",
        "#",
        f"AIR_ALTITUDE {altitude}"
    ]

    script.append_lines(lines)
    return

