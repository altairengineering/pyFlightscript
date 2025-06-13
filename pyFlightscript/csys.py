from .utils import *    
from .script import script
import numpy as np

def create_new_coordinate_system():
    """
    Appends lines to script state to create a new coordinate system.
    
    Example usage:
    create_new_coordinate_system()


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

def edit_coordinate_system(frame, name, origin_x, origin_y, origin_z, 
                           vector_x_x, vector_x_y, vector_x_z, 
                           vector_y_x, vector_y_y, vector_y_z,
                           vector_z_x, vector_z_y, vector_z_z):
    """
    Appends lines to script state to edit a local coordinate system.

    Example usage:
    edit_coordinate_system(2, "Prop-1", 0, 1, 0.5,
                           1, 0, 0, 0, -1, 0, 0, 0, -1.2)


    :param frame: Index of the local coordinate system.
    :param name: Name of the local coordinate system.
    :param origin_x: X coordinate of the origin.
    :param origin_y: Y coordinate of the origin.
    :param origin_z: Z coordinate of the origin.
    :param vector_x_x: X component of the X axis vector.
    :param vector_x_y: Y component of the X axis vector.
    :param vector_x_z: Z component of the X axis vector.
    :param vector_y_x: X component of the Y axis vector.
    :param vector_y_y: Y component of the Y axis vector.
    :param vector_y_z: Z component of the Y axis vector.
    :param vector_z_x: X component of the Z axis vector.
    :param vector_z_y: Y component of the Z axis vector.
    :param vector_z_z: Z component of the Z axis vector.
    """

    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    if not all(isinstance(val, (int, float)) for val in [origin_x, origin_y, origin_z, 
                                                         vector_x_x, vector_x_y, vector_x_z,
                                                         vector_y_x, vector_y_y, vector_y_z,
                                                         vector_z_x, vector_z_y, vector_z_z]):
        raise ValueError("Coordinates and vector components should be integer or float values.")

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

def set_coordinate_system_name(frame, name):
    """
    Appends lines to script state to set the name of an existing local coordinate system.
    
    Example usage:
    set_coordinate_system_name(, 2, 'Propeller_Axis')
    

    :param frame: Index of the local coordinate system.
    :param name: New name of the coordinate system.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if frame <= 1:
        raise ValueError("`frame` should be greater than 1.")
    
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

def set_coordinate_system_origin(frame, x, y, z, units='INCH'):
    """
    Appends lines to script state to set the origin of an existing local 
    coordinate system.
    
    Example usage:
    set_coordinate_system_origin(, 2, 0.0, 1.0, 1.4, 'INCH')
    

    :param frame: Index of the local coordinate system.
    :param x: Origin position in X relative to the reference coordinate system.
    :param y: Origin position in Y relative to the reference coordinate system.
    :param z: Origin position in Z relative to the reference coordinate system.
    :param units: Units of the position values.
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
        raise ValueError("`x`, `y`, and `z` should be integer or float values.")
    
    check_valid_length_units(units)
    
    lines = [
        "#************************************************************************",
        "#********* Set the origin of an existing local coordinate system ********",
        "#************************************************************************",
        "#",
        f"SET_COORDINATE_SYSTEM_ORIGIN {frame} {x} {y} {z} {units}"
    ]

    script.append_lines(lines)
    return

def set_coordinate_system_axis(frame, axis, nx, ny, nz, 
                               normalize_frame=True):
    """
    Example usage:
    set_coordinate_system_axis(, 2, 'X', -1.0, 0.5, 0.0, True)
    
    Appends lines to script state to set an axis of an existing local coordinate system.
    

    :param frame: Index of the local coordinate system.
    :param axis: Axis of the coordinate system to be set.
    :param nx: X-coordinate of the normal direction vector.
    :param ny: Y-coordinate of the normal direction vector.
    :param nz: Z-coordinate of the normal direction vector.
    :param normalize_frame: Automatically normalize all axes of the coordinate system after updating.
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer value greater than 1.")
    
    valid_axes = ['X', 'Y', 'Z']
    if axis not in valid_axes:
        raise ValueError(f"`axis` should be one of {valid_axes}")
    
    if not isinstance(nx, (int, float)) or not isinstance(ny, (int, float)) or not isinstance(nz, (int, float)):
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

def normalize_coordinate_system(coord_system_index=1):
    """
    Appends lines to script state to normalize a coordinate system.
    

    :param coord_system_index: Index of the local coordinate system to be rotated.
    
    Example usage:
    normalize_coordinate_system(, 2)
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

def rotate_coordinate_system(frame=2, rotation_frame=3, 
                             rotation_axis='Y', angle=-45.0):
    """
    Example usage:
    rotate_coordinate_system()
    
    Appends lines to script state to rotate a coordinate system.
    

    :param frame: Index of the local coordinate system to be rotated.
    :param rotation_frame: Index of the local coordinate system to be used to rotate the selected system.
    :param rotation_axis: Axis of rotation. Can be 'X', 'Y', 'Z', '1', '2', or '3'.
    :param angle: Rotation angle in degrees.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if not isinstance(rotation_frame, int):
        raise ValueError("`rotation_frame` should be an integer value.")
    
    valid_axes = ['X', 'Y', 'Z', '1', '2', '3']
    if rotation_axis not in valid_axes:
        raise ValueError(f"`rotation_axis` should be one of {valid_axes}")
    
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

def translate_coordinate_system(frame, x, y, z, units='METER'):
    """
    Appends lines to script state to translate a coordinate system.
    
    Example usage:
    translate_coordinate_system(, 2, 0.0, 1.0, 1.4, 'INCH')
    

    :param frame: Index of the local coordinate system to be rotated.
    :param x: Translation vector value in X direction.
    :param y: Translation vector value in Y direction.
    :param z: Translation vector value in Z direction.
    :param units: Unit type for translation.
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer value greater than 1.")
    
    check_valid_length_units(units)
    
    for value in [x, y, z]:
        if not isinstance(value, (int, float)):
            raise ValueError("Translation vector values (x, y, z) should be integers or float values.")
    
    lines = [
        "#************************************************************************",
        "#****************** Translate a coordinate system ***********************",
        "#************************************************************************",
        "#",
        f"TRANSLATE_COORDINATE_SYSTEM {frame} {x} {y} {z} {units}"
    ]

    script.append_lines(lines)
    return

def duplicate_coordinate_system(frame):
    """
    Appends lines to script state to duplicate a local coordinate system.
    

    :param frame: Index of the local coordinate system to be duplicated.
    
    Example usage:
    duplicate_coordinate_system(, 2)
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if frame <= 1:
        raise ValueError("`frame` should be greater than 1.")
    
    lines = [
        "#************************************************************************",
        "#****************** Duplicate a local coordinate system *****************",
        "#************************************************************************",
        "#",
        f"DUPLICATE_COORDINATE_SYSTEM {frame}"
    ]

    script.append_lines(lines)
    return

def mirror_coordinate_system(frame, plane='XZ'):
    """
    Example usage:
    mirror_coordinate_system(, 2)
    
    Appends lines to script state to mirror a local coordinate system.
    

    :param frame: Index of the local coordinate system to be duplicated and then mirrored.
    :param plane: Plane of the reference coordinate system to be used.
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer value greater than 1.")
    
    valid_planes = ['YZ', 'XZ', 'XY']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")
    
    lines = [
        "#************************************************************************",
        "#****************** Mirror a local coordinate system ********************",
        "#************************************************************************",
        "#",
        f"MIRROR_COORDINATE_SYSTEM {frame} {plane}"
    ]

    script.append_lines(lines)
    return

def delete_coordinate_system(frame):
    """
    Appends lines to script state to delete a coordinate system.
    
    Example usage:
    delete_coordinate_system(, 2)
    

    :param frame: Index of the local coordinate system to be deleted.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    if frame <= 1:
        raise ValueError("`frame` should be greater than 1.")

    lines = [
        "#************************************************************************",
        "#****************** Delete a coordinate system **************************",
        "#************************************************************************",
        "#",
        f"DELETE_COORDINATE_SYSTEM {frame}"
    ]

    script.append_lines(lines)
    return