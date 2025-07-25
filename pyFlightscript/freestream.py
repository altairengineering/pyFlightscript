import os
from .utils import *    
from .script import script
from .types import *
from typing import Optional, List

def set_freestream(
    freestream_type: ValidFreestreamType,
    profile_path: Optional[str] = None,
    frame: Optional[int] = None,
    axis: Optional[ValidAxis] = None,
    angular_velocity: Optional[float] = None
) -> None:
    """
    Set the freestream velocity type.

    This function appends a command to the script state to configure the
    freestream velocity, which can be constant, custom from a file, or
    rotational.

    Parameters
    ----------
    freestream_type : ValidFreestreamType
        The type of freestream ('CONSTANT', 'CUSTOM', or 'ROTATION').
    profile_path : Optional[str], optional
        The absolute path to a custom velocity profile file. Required if
        `freestream_type` is 'CUSTOM'. Defaults to None.
    frame : Optional[int], optional
        The index of the coordinate system for defining rotation. Required
        if `freestream_type` is 'ROTATION'. Defaults to None.
    axis : Optional[ValidAxis], optional
        The axis of rotation ('X', 'Y', or 'Z'). Required if
        `freestream_type` is 'ROTATION'. Defaults to None.
    angular_velocity : Optional[float], optional
        The rotational velocity in rad/sec. Required if `freestream_type`
        is 'ROTATION'. Defaults to None.

    Raises
    ------
    ValueError
        If `freestream_type` is invalid, or if required parameters for a
        given type are missing or have incorrect types.

    Examples
    --------
    >>> # Set a constant freestream velocity
    >>> set_freestream(freestream_type='CONSTANT')

    >>> # Set a custom freestream velocity from a profile file
    >>> set_freestream(
    ...     freestream_type='CUSTOM',
    ...     profile_path='C:/path/to/profile.txt'
    ... )

    >>> # Set a rotational freestream velocity
    >>> set_freestream(
    ...     freestream_type='ROTATION',
    ...     frame=1,
    ...     axis='X',
    ...     angular_velocity=-0.2
    ... )
    """

    # Type and value checking
    if freestream_type not in VALID_FREESTREAM_TYPE_LIST:
        raise ValueError(f"`freestream_type` should be one of {VALID_FREESTREAM_TYPE_LIST}")

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
        check_file_existence(profile_path)
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
        if axis not in VALID_AXIS_LIST:
            raise ValueError(f"`axis` should be one of {VALID_AXIS_LIST}")
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
) -> None:
    """
    Set the fluid properties.

    This function appends a command to the script state to define the
    properties of the fluid for the simulation.

    Parameters
    ----------
    density : float, optional
        Density of the fluid in kg/m^3. Defaults to 1.225.
    pressure : float, optional
        Static pressure of the fluid in Pa. Defaults to 101325.0.
    sonic_velocity : float, optional
        Sonic velocity in the fluid in m/sec. Defaults to 340.0.
    temperature : float, optional
        Temperature of the fluid in Kelvin. Defaults to 288.15.
    viscosity : float, optional
        Viscosity of the fluid in Pa-sec. Defaults to 1.789e-5.

    Raises
    ------
    ValueError
        If any of the properties are not numeric values.

    Examples
    --------
    >>> # Set fluid properties with default values
    >>> fluid_properties()

    >>> # Set custom fluid properties
    >>> fluid_properties(density=1.2, pressure=101000, sonic_velocity=343)
    """
    if not all(isinstance(val, (int, float)) for val in [
        density, pressure, sonic_velocity, temperature, viscosity
    ]):
        raise ValueError("All fluid properties must be numeric values.")

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

def air_altitude(altitude: float = 15000.0) -> None:
    """
    Set fluid (air) properties based on altitude.

    This function appends a command to the script state to set the fluid
    properties corresponding to a specified altitude in feet, based on
    standard atmospheric models.

    Parameters
    ----------
    altitude : float, optional
        The altitude in feet. Defaults to 15000.0.

    Raises
    ------
    ValueError
        If `altitude` is not a numeric value.

    Examples
    --------
    >>> # Set air properties for an altitude of 15,000 feet
    >>> air_altitude()

    >>> # Set air properties for sea level
    >>> air_altitude(altitude=0)
    """
    if not isinstance(altitude, (int, float)):
        raise ValueError("`altitude` must be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the fluid (air) properties based on altitude *************",
        "#************************************************************************",
        "#",
        f"AIR_ALTITUDE {altitude}"
    ]

    script.append_lines(lines)
    return

