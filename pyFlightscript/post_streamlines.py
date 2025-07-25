from .utils import *    
from .script import script
from .types import *

def new_off_body_streamline(position_x, position_y, position_z, upstream='DISABLE'):
    """
    Appends lines to script state to create an off-body streamline.
    
    Example usage:
    new_off_body_streamline(, -3.0, -0.1, 0.2, 'DISABLE')
    

    :param position_x: X coordinate of the position.
    :param position_y: Y coordinate of the position.
    :param position_z: Z coordinate of the position.
    :param upstream: Enable/Disable upstream.
    """
    
    # Value checking
    valid_upstream_values = ['ENABLE', 'DISABLE']
    if upstream not in valid_upstream_values:
        raise ValueError(f"`upstream` should be one of {valid_upstream_values}")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a off-body streamline ************************",
        "#************************************************************************",
        "#",
        "NEW_OFF_BODY_STREAMLINE",
        f"POSITION_X {position_x}",
        f"POSITION_Y {position_y}",
        f"POSITION_Z {position_z}",
        f"UPSTREAM {upstream}"
    ]

    script.append_lines(lines)
    return

def new_streamline_distribution(position_1_x, position_1_y, position_1_z,
                                position_2_x, position_2_y, position_2_z, subdivisions):
    """
    Appends lines to script state to create a new off-body streamline distribution.
    
    Example usage:
    new_streamline_distribution(, -3.0, -1.2, -0.3, -3.0, 1.2, -0.3, 48)
    

    :param position_1_x: X coordinate of the starting vertex.
    :param position_1_y: Y coordinate of the starting vertex.
    :param position_1_z: Z coordinate of the starting vertex.
    :param position_2_x: X coordinate of the ending vertex.
    :param position_2_y: Y coordinate of the ending vertex.
    :param position_2_z: Z coordinate of the ending vertex.
    :param subdivisions: N+1 , where N = Number of streamlines.
    """
    
    # Type and value checking
    if not isinstance(subdivisions, int) or subdivisions < 2:
        raise ValueError("`subdivisions` should be an integer value greater than 1.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new off-body streamline distribution *******",
        "#************************************************************************",
        "#",
        "NEW_STREAMLINE_DISTRIBUTION",
        f"POSITION_1_X {position_1_x}",
        f"POSITION_1_Y {position_1_y}",
        f"POSITION_1_Z {position_1_z}",
        f"POSITION_2_X {position_2_x}",
        f"POSITION_2_Y {position_2_y}",
        f"POSITION_2_Z {position_2_z}",
        f"SUBDIVISIONS {subdivisions}"
    ]

    script.append_lines(lines)
    return

def new_off_body_streamtube(radius, frame, axis, radial_subdivisions, azimuth_subdivisions):
    """
    Appends lines to script state to create a new off-body streamtube.


    :param radius: Value of the radius.
    :param frame: Index of the coordinate system to be used for this actuator (> 0).
    :param axis: Axis of the actuator disc. Value is 1, 2 or 3 for X, Y and Z axes respectively.
    :param radial_subdivisions: Number of radial subdivisions.
    :param azimuth_subdivisions: Number of azimuth subdivisions.
    
    Example usage:
    new_off_body_streamtube(, 0.5, 2, 1, 3, 10)
    """

    # Type and value checking
    if not isinstance(radius, (int, float)):
        raise ValueError("`radius` should be an integer or float value.")
    
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be a positive integer.")
    
    if axis not in [1, 2, 3]:
        raise ValueError("`axis` should be 1, 2 or 3 for X, Y and Z axes respectively.")
    
    if not isinstance(radial_subdivisions, int):
        raise ValueError("`radial_subdivisions` should be an integer.")
    
    if not isinstance(azimuth_subdivisions, int):
        raise ValueError("`azimuth_subdivisions` should be an integer.")

    lines = [
        "#************************************************************************",
        "#****************** Create a new off-body streamtube ********************",
        "#************************************************************************",
        "#",
        "NEW_OFF_BODY_STREAMTUBE",
        f"RADIUS {radius}",
        f"FRAME {frame}",
        f"AXIS {axis}",
        f"RADIAL_SUBDIVISIONS {radial_subdivisions}",
        f"AZIMUTH_SUBDIVISIONS {azimuth_subdivisions}"
    ]

    script.append_lines(lines)
    return

def set_off_body_streamline_length(set_length=None, set_unrestricted_length=None):
    """
    Appends lines to script state to set the length of the new off-body streamlines.


    :param set_length: Length of the streamline.
    :param set_unrestricted_length: Unrestricted length of the streamline. 

    Note: Either `set_length` or `set_unrestricted_length` should be provided, not both.
    
    Example usage:
    set_off_body_streamline_length(, set_length=5)
    """

    # Type and value checking
    if set_length is not None and set_unrestricted_length is not None:
        raise ValueError("Either `set_length` or `set_unrestricted_length` should be provided, not both.")
    
    if set_length:
        if not isinstance(set_length, (int, float)):
            raise ValueError("`set_length` should be an integer or float value.")
    else:
        if set_unrestricted_length is None:
            raise ValueError("Either `set_length` or `set_unrestricted_length` should be provided.")

    lines = [
        "#************************************************************************",
        "#****************** Set the length of the new off-body streamlines ******",
        "#************************************************************************",
        "#",
        "SET_OFF_BODY_STREAMLINE_LENGTH"
    ]

    if set_length:
        lines.append(f"SET_LENGTH {set_length}")
    else:
        lines.append("SET_UNRESTRICTED_LENGTH")

    script.append_lines(lines)
    return

def set_all_off_body_streamlines_upstream():
    """
    Appends lines to script state to set all off-body streamlines upstream.
    


    Example usage:
    set_all_off_body_streamlines_upstream()
    """
    lines = [
        "#************************************************************************",
        "#********** Set all off-body streamlines upstream **********************",
        "#************************************************************************",
        "#",
        "SET_ALL_OFF_BODY_STREAMLINES_UPSTREAM"
    ]
    script.append_lines(lines)
    return

def set_all_off_body_streamlines_downstream():
    """
    Appends lines to script state to set all off-body streamlines downstream.
    


    Example usage:
    set_all_off_body_streamlines_downstream()
    """
    lines = [
        "#************************************************************************",
        "#********** Set all off-body streamlines downstream ********************",
        "#************************************************************************",
        "#",
        "SET_ALL_OFF_BODY_STREAMLINES_DOWNSTREAM"
    ]
    script.append_lines(lines)
    return

def generate_all_off_body_streamlines():
    """
    Appends lines to script state to generate all off-body streamlines.
    


    Example usage:
    generate_all_off_body_streamlines()
    """
    lines = [
        "#************************************************************************",
        "#********** Generate all off-body streamlines *************************",
        "#************************************************************************",
        "#",
        "GENERATE_ALL_OFF_BODY_STREAMLINES"
    ]
    script.append_lines(lines)
    return

def delete_all_off_body_streamlines():
    """
    Appends lines to script state to delete all off-body streamlines.
    


    Example usage:
    delete_all_off_body_streamlines()
    """
    lines = [
        "#************************************************************************",
        "#********** Delete all off-body streamlines ****************************",
        "#************************************************************************",
        "#",
        "DELETE_ALL_OFF_BODY_STREAMLINES"
    ]
    script.append_lines(lines)
    return

def export_all_off_body_streamlines(filename):
    """
    Appends lines to script state to export all off-body streamlines.


    :param filename: Filename with path to store the streamlines.

    Example usage:
    export_all_off_body_streamlines(, 'C:/.../Test_streamlines.txt')
    """
    
    # Check for filename's type
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export all off-body streamlines ********************",
        "#************************************************************************",
        "#",
        "EXPORT_ALL_OFF_BODY_STREAMLINES",
        f"{filename}"
    ]

    script.append_lines(lines)
    return

#### Surface Streamlines
def generate_all_surface_streamlines():
    """
    Appends lines to script state to generate all surface streamlines.
    
    Example usage:
    generate_all_surface_streamlines()
    """
    lines = [
        "#************************************************************************",
        "#****************** Generate all surface streamlines *******************",
        "#************************************************************************",
        "#",
        "GENERATE_ALL_SURFACE_STREAMLINES",
    ]

    script.append_lines(lines)
    return

def delete_all_surface_streamlines():
    """
    Appends lines to script state to delete all surface streamlines.
    
    Example usage:
    delete_all_surface_streamlines()
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all surface streamlines *********************",
        "#************************************************************************",
        "#",
        "DELETE_ALL_SURFACE_STREAMLINES",
    ]

    script.append_lines(lines)
    return

def export_all_surface_streamlines(output_filepath):
    """
    Appends lines to script state to export all on-body (surface) streamlines.
    

    :param output_filepath: Filename with path for the streamlines output.
    
    Example usage:
    export_all_surface_streamlines(, 'C:/.../Test_streamlines.txt')
    """
    
    # Type checking for output_filepath
    if not isinstance(output_filepath, str):
        raise ValueError("`output_filepath` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export all on-body (surface) streamlines ************",
        "#************************************************************************",
        "#",
        "EXPORT_ALL_SURFACE_STREAMLINES",
        f"{output_filepath}",
    ]

    script.append_lines(lines)
    return
