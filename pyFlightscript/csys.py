from .utils import *    
from .script import script
from .types import *
import numpy as np

def create_new_coordinate_system() -> None:
    """
    Create a new coordinate system.

    This function appends a command to the script state to create a new
    local coordinate system.

    Examples
    --------
    >>> # Create a new local coordinate system
    >>> create_new_coordinate_system()
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new coordinate system **********************",
        "#************************************************************************",
        "#",
        "CREATE_NEW_COORDINATE_SYSTEM"
    ]

    script.append_lines(lines)
    return

def edit_coordinate_system(
    frame: int,
    name: str,
    origin_x: float, origin_y: float, origin_z: float,
    vector_x_x: float, vector_x_y: float, vector_x_z: float,
    vector_y_x: float, vector_y_y: float, vector_y_z: float,
    vector_z_x: float, vector_z_y: float, vector_z_z: float
) -> None:
    """
    Edit a local coordinate system.

    This function appends a command to the script state to modify an existing
    local coordinate system's properties, including its name, origin, and
    axis vectors.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system to edit. Must be > 1.
    name : str
        New name for the coordinate system.
    origin_x, origin_y, origin_z : float
        Coordinates of the new origin.
    vector_x_x, vector_x_y, vector_x_z : float
        Components of the new X-axis vector.
    vector_y_x, vector_y_y, vector_y_z : float
        Components of the new Y-axis vector.
    vector_z_x, vector_z_y, vector_z_z : float
        Components of the new Z-axis vector.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1, or if any coordinate
        or vector component is not a numeric value.

    Examples
    --------
    >>> # Edit coordinate system 2
    >>> edit_coordinate_system(
    ...     frame=2, name="Prop-1",
    ...     origin_x=0, origin_y=1, origin_z=0.5,
    ...     vector_x_x=1, vector_x_y=0, vector_x_z=0,
    ...     vector_y_x=0, vector_y_y=-1, vector_y_z=0,
    ...     vector_z_x=0, vector_z_y=0, vector_z_z=-1.2
    ... )
    """

    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    if not all(isinstance(val, (int, float)) for val in [
        origin_x, origin_y, origin_z,
        vector_x_x, vector_x_y, vector_x_z,
        vector_y_x, vector_y_y, vector_y_z,
        vector_z_x, vector_z_y, vector_z_z
    ]):
        raise ValueError("Coordinates and vector components should be numeric values.")

    lines = [
        "#************************************************************************",
        "#****************** Edit a local coordinate system **********************",
        "#************************************************************************",
        "#",
        "EDIT_COORDINATE_SYSTEM",
        f"FRAME {frame}",
        f"NAME {name}",
        f"ORIGIN_X {origin_x}",
        f"ORIGIN_Y {origin_y}",
        f"ORIGIN_Z {origin_z}",
        f"VECTOR_X_X {vector_x_x}",
        f"VECTOR_X_Y {vector_x_y}",
        f"VECTOR_X_Z {vector_x_z}",
        f"VECTOR_Y_X {vector_y_x}",
        f"VECTOR_Y_Y {vector_y_y}",
        f"VECTOR_Y_Z {vector_y_z}",
        f"VECTOR_Z_X {vector_z_x}",
        f"VECTOR_Z_Y {vector_z_y}",
        f"VECTOR_Z_Z {vector_z_z}"
    ]

    script.append_lines(lines)
    return

def set_coordinate_system_name(frame: int, name: str) -> None:
    """
    Set the name of an existing local coordinate system.

    This function appends a command to the script state to change the name
    of a specified local coordinate system.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system. Must be an integer > 1.
    name : str
        The new name for the coordinate system.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1, or if `name` is not a
        string.

    Examples
    --------
    >>> # Set the name of coordinate system 2 to "Propeller_Axis"
    >>> set_coordinate_system_name(frame=2, name='Propeller_Axis')
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    
    if not isinstance(name, str):
        raise ValueError("`name` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the name of an existing local coordinate system **********",
        "#************************************************************************",
        "#",
        f"SET_COORDINATE_SYSTEM_NAME {frame} {name}"
    ]

    script.append_lines(lines)
    return

def set_coordinate_system_origin(
    frame: int,
    x: float,
    y: float,
    z: float,
    units: ValidUnits = 'INCH'
) -> None:
    """
    Set the origin of an existing local coordinate system.

    This function appends a command to the script state to set the origin
    of a specified local coordinate system relative to the reference
    coordinate system.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system. Must be an integer > 1.
    x, y, z : float
        The new origin coordinates.
    units : ValidUnits, optional
        The units for the position values. Defaults to 'INCH'.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1, if coordinates are not
        numeric, or if `units` is invalid.

    Examples
    --------
    >>> # Set the origin of coordinate system 2 to (0, 1, 1.4) in inches
    >>> set_coordinate_system_origin(frame=2, x=0.0, y=1.0, z=1.4, units='INCH')
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise ValueError("`x`, `y`, and `z` should be numeric values.")
    
    if units not in VALID_UNITS_LIST:
        raise ValueError(f"Invalid units: {units}. Must be one of {VALID_UNITS_LIST}.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the origin of an existing local coordinate system ********",
        "#************************************************************************",
        "#",
        f"SET_COORDINATE_SYSTEM_ORIGIN {frame} {x} {y} {z} {units}"
    ]

    script.append_lines(lines)
    return

def set_coordinate_system_axis(
    frame: int,
    axis: ValidAxis,
    nx: float,
    ny: float,
    nz: float,
    normalize_frame: bool = True
) -> None:
    """
    Set an axis of an existing local coordinate system.

    This function appends a command to the script state to set a specified
    axis of an existing local coordinate system with a new vector.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system. Must be an integer > 1.
    axis : ValidAxis
        The axis to set ('X', 'Y', or 'Z').
    nx, ny, nz : float
        Components of the new axis vector.
    normalize_frame : bool, optional
        If True, automatically normalizes all axes of the coordinate system
        after the update. Defaults to True.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1, if `axis` is invalid,
        if vector components are not numeric, or if `normalize_frame` is
        not a boolean.

    Examples
    --------
    >>> # Set the X-axis of coordinate system 2
    >>> set_coordinate_system_axis(frame=2, axis='X', nx=-1.0, ny=0.5, nz=0.0)
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer value greater than 1.")
    
    if axis not in VALID_AXIS_LIST:
        raise ValueError(f"`axis` should be one of {VALID_AXIS_LIST}")
    
    if not all(isinstance(val, (int, float)) for val in [nx, ny, nz]):
        raise ValueError("`nx`, `ny`, and `nz` should be numeric values.")
    
    if not isinstance(normalize_frame, bool):
        raise ValueError("`normalize_frame` should be a boolean value.")
    
    lines = [
        "#************************************************************************",
        "#********* Edit the axis of an existing local coordinate system *********",
        "#************************************************************************",
        "#",
        f"SET_COORDINATE_SYSTEM_AXIS {frame} {axis} {nx} {ny} {nz} {normalize_frame}"
    ]

    script.append_lines(lines)
    return

def normalize_coordinate_system(coord_system_index: int = 1) -> None:
    """
    Normalize a coordinate system.

    This function appends a command to the script state to normalize the
    axes of a specified local coordinate system.

    Parameters
    ----------
    coord_system_index : int, optional
        The index of the local coordinate system to normalize. Must be a
        positive integer. Defaults to 1.

    Raises
    ------
    ValueError
        If `coord_system_index` is not a positive integer.

    Examples
    --------
    >>> # Normalize coordinate system 2
    >>> normalize_coordinate_system(coord_system_index=2)
    """
    
    # Type and value checking
    if not isinstance(coord_system_index, int) or coord_system_index < 1:
        raise ValueError("`coord_system_index` should be a positive integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Normalize coordinate system axes ********************",
        "#************************************************************************",
        "#",
        f"NORMALIZE_COORDINATE_SYSTEM {coord_system_index}"
    ]

    script.append_lines(lines)
    return

def rotate_coordinate_system(
    frame: int = 2,
    rotation_frame: int = 3,
    rotation_axis: ValidRotationAxis = 'Y',
    angle: float = -45.0
) -> None:
    """
    Rotate a coordinate system.

    This function appends a command to the script state to rotate a local
    coordinate system around a specified axis of another coordinate system.

    Parameters
    ----------
    frame : int, optional
        Index of the local coordinate system to be rotated. Defaults to 2.
    rotation_frame : int, optional
        Index of the local coordinate system to be used for the rotation.
        Defaults to 3.
    rotation_axis : ValidRotationAxis, optional
        The axis of rotation ('X', 'Y', 'Z', '1', '2', or '3').
        Defaults to 'Y'.
    angle : float, optional
        The rotation angle in degrees. Defaults to -45.0.

    Raises
    ------
    ValueError
        If `frame` or `rotation_frame` are not integers, if `rotation_axis`
        is invalid, or if `angle` is not a numeric value.

    Examples
    --------
    >>> # Rotate coordinate system 2 around the Y-axis of system 3 by -45 degrees
    >>> rotate_coordinate_system()
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if not isinstance(rotation_frame, int):
        raise ValueError("`rotation_frame` should be an integer value.")
    
    if rotation_axis not in VALID_ROTATION_AXIS_LIST:
        raise ValueError(f"`rotation_axis` should be one of {VALID_ROTATION_AXIS_LIST}")
    
    if not isinstance(angle, (int, float, np.integer, np.floating)):
        raise ValueError("`angle` should be an integer or float value, including numpy types.")
    
    lines = [
        "#************************************************************************",
        "#****************** Rotate a coordinate system **************************",
        "#************************************************************************",
        "#",
        "ROTATE_COORDINATE_SYSTEM",
        f"FRAME {frame}",
        f"ROTATION_FRAME {rotation_frame}",
        f"ROTATION_AXIS {rotation_axis}",
        f"ANGLE {angle}"
    ]

    script.append_lines(lines)
    return

def translate_coordinate_system(
    frame: int,
    x: float,
    y: float,
    z: float,
    units: ValidUnits = 'METER'
) -> None:
    """
    Translate a coordinate system.

    This function appends a command to the script state to translate a local
    coordinate system by a specified vector.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system to translate. Must be > 1.
    x, y, z : float
        Components of the translation vector.
    units : ValidUnits, optional
        The units for the translation vector. Defaults to 'METER'.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1, if translation
        components are not numeric, or if `units` is invalid.

    Examples
    --------
    >>> # Translate coordinate system 2 by (0, 1, 1.4) in inches
    >>> translate_coordinate_system(frame=2, x=0.0, y=1.0, z=1.4, units='INCH')
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer value greater than 1.")
    
    if units not in VALID_UNITS_LIST:
        raise ValueError(f"Invalid units: {units}. Must be one of {VALID_UNITS_LIST}.")
    
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise ValueError("Translation vector values (x, y, z) should be numeric.")
    
    lines = [
        "#************************************************************************",
        "#****************** Translate a coordinate system ***********************",
        "#************************************************************************",
        "#",
        f"TRANSLATE_COORDINATE_SYSTEM {frame} {x} {y} {z} {units}"
    ]

    script.append_lines(lines)
    return

def duplicate_coordinate_system(frame: int) -> None:
    """
    Duplicate a local coordinate system.

    This function appends a command to the script state to duplicate a
    specified local coordinate system.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system to be duplicated. Must be > 1.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1.

    Examples
    --------
    >>> # Duplicate coordinate system 2
    >>> duplicate_coordinate_system(frame=2)
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    
    lines = [
        "#************************************************************************",
        "#****************** Duplicate a local coordinate system *****************",
        "#************************************************************************",
        "#",
        f"DUPLICATE_COORDINATE_SYSTEM {frame}"
    ]

    script.append_lines(lines)
    return

def mirror_coordinate_system(frame: int, plane: ValidPlanes = 'XZ') -> None:
    """
    Mirror a local coordinate system.

    This function appends a command to the script state to duplicate and
    mirror a local coordinate system across a specified plane of the
    reference coordinate system.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system to be mirrored. Must be > 1.
    plane : ValidPlanes, optional
        The plane of the reference coordinate system to be used for
        mirroring ('XY', 'XZ', 'YZ'). Defaults to 'XZ'.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1, or if `plane` is
        invalid.

    Examples
    --------
    >>> # Mirror coordinate system 2 across the XZ plane
    >>> mirror_coordinate_system(frame=2)

    >>> # Mirror coordinate system 3 across the YZ plane
    >>> mirror_coordinate_system(frame=3, plane='YZ')
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer value greater than 1.")
    
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}")
    
    lines = [
        "#************************************************************************",
        "#****************** Mirror a local coordinate system ********************",
        "#************************************************************************",
        "#",
        f"MIRROR_COORDINATE_SYSTEM {frame} {plane}"
    ]

    script.append_lines(lines)
    return

def delete_coordinate_system(frame: int) -> None:
    """
    Delete a coordinate system.

    This function appends a command to the script state to delete a specified
    local coordinate system.

    Parameters
    ----------
    frame : int
        Index of the local coordinate system to be deleted. Must be > 1.

    Raises
    ------
    ValueError
        If `frame` is not an integer greater than 1.

    Examples
    --------
    >>> # Delete coordinate system 2
    >>> delete_coordinate_system(frame=2)
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")

    lines = [
        "#************************************************************************",
        "#****************** Delete a coordinate system **************************",
        "#************************************************************************",
        "#",
        f"DELETE_COORDINATE_SYSTEM {frame}"
    ]

    script.append_lines(lines)
    return