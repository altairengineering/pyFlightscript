from .utils import *
from .script import script
from .types import *

def new_off_body_streamline(
    position_x: float,
    position_y: float,
    position_z: float,
    upstream: RunOptions = 'DISABLE'
) -> None:
    """
    Create an off-body streamline.

    This function appends a command to the script state to create a single
    off-body streamline starting at a specified position.

    Parameters
    ----------
    position_x : float
        X-coordinate of the streamline's starting position.
    position_y : float
        Y-coordinate of the streamline's starting position.
    position_z : float
        Z-coordinate of the streamline's starting position.
    upstream : RunOptions, optional
        Whether to generate the streamline upstream from the starting point,
        by default 'DISABLE'. Must be one of `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Create a downstream streamline at a specific point
    >>> new_off_body_streamline(-3.0, -0.1, 0.2)

    >>> # Create an upstream streamline
    >>> new_off_body_streamline(-3.0, -0.1, 0.2, upstream='ENABLE')
    """
    if not all(isinstance(v, (int, float)) for v in [position_x, position_y, position_z]):
        raise ValueError("Position coordinates must be numeric.")
    if upstream not in VALID_RUN_OPTIONS:
        raise ValueError(f"`upstream` must be one of {VALID_RUN_OPTIONS}")

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

def new_streamline_distribution(
    position_1_x: float,
    position_1_y: float,
    position_1_z: float,
    position_2_x: float,
    position_2_y: float,
    position_2_z: float,
    subdivisions: int
) -> None:
    """
    Create a new off-body streamline distribution.

    This function appends a command to the script state to create a line of
    streamlines between two specified points.

    Parameters
    ----------
    position_1_x : float
        X-coordinate of the starting vertex.
    position_1_y : float
        Y-coordinate of the starting vertex.
    position_1_z : float
        Z-coordinate of the starting vertex.
    position_2_x : float
        X-coordinate of the ending vertex.
    position_2_y : float
        Y-coordinate of the ending vertex.
    position_2_z : float
        Z-coordinate of the ending vertex.
    subdivisions : int
        The number of streamlines to create is `subdivisions` - 1.
        Value must be > 1.

    Examples
    --------
    >>> # Create 48 streamlines between two points
    >>> new_streamline_distribution(-3.0, -1.2, -0.3, -3.0, 1.2, -0.3, 49)
    """
    if not all(isinstance(v, (int, float)) for v in [
        position_1_x, position_1_y, position_1_z,
        position_2_x, position_2_y, position_2_z
    ]):
        raise ValueError("Position coordinates must be numeric.")
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

def new_off_body_streamtube(
    radius: float,
    frame: int,
    axis: int,
    radial_subdivisions: int,
    azimuth_subdivisions: int
) -> None:
    """
    Create a new off-body streamtube.

    This function appends a command to the script state to create a streamtube,
    which is a bundle of streamlines starting from a circular area.

    Parameters
    ----------
    radius : float
        The radius of the streamtube's circular base.
    frame : int
        The index of the coordinate system to be used (> 0).
    axis : int
        The axis of the streamtube's disc. Use 1 for X, 2 for Y, and 3 for Z.
    radial_subdivisions : int
        The number of subdivisions along the radius.
    azimuth_subdivisions : int
        The number of subdivisions around the azimuth.

    Examples
    --------
    >>> # Create a streamtube with a radius of 0.5 in frame 2 along the X-axis
    >>> new_off_body_streamtube(0.5, 2, 1, 3, 10)
    """
    if not isinstance(radius, (int, float)):
        raise ValueError("`radius` should be a numeric value.")
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be a positive integer.")
    if axis not in [1, 2, 3]:
        raise ValueError("`axis` must be 1 (X), 2 (Y), or 3 (Z).")
    if not isinstance(radial_subdivisions, int):
        raise ValueError("`radial_subdivisions` must be an integer.")
    if not isinstance(azimuth_subdivisions, int):
        raise ValueError("`azimuth_subdivisions` must be an integer.")

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

def set_off_body_streamline_length(length: Optional[float] = None) -> None:
    """
    Set the length of new off-body streamlines.

    This function appends a command to the script state to define the length
    of subsequently created off-body streamlines.

    Parameters
    ----------
    length : float, optional
        The length of the streamline. If not provided or set to None,
        the length is considered unrestricted.

    Examples
    --------
    >>> # Set a specific streamline length
    >>> set_off_body_streamline_length(length=10.5)

    >>> # Set streamlines to have unrestricted length
    >>> set_off_body_streamline_length()
    """
    lines = [
        "#************************************************************************",
        "#****************** Set the length of the new off-body streamlines ******",
        "#************************************************************************",
        "#",
        "SET_OFF_BODY_STREAMLINE_LENGTH"
    ]

    if length is not None:
        if not isinstance(length, (int, float)):
            raise ValueError("`length` should be a numeric value.")
        lines.append(f"SET_LENGTH {length}")
    else:
        lines.append("SET_UNRESTRICTED_LENGTH")

    script.append_lines(lines)
    return

def set_all_off_body_streamlines_upstream():
    """
    Appends lines to script state to set all off-body streamlines upstream.

    Examples
    --------
    >>> # Set all off-body streamlines upstream
    >>> set_all_off_body_streamlines_upstream()
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

    Examples
    --------
    >>> # Set all off-body streamlines downstream
    >>> set_all_off_body_streamlines_downstream()
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

    Examples
    --------
    >>> # Generate all off-body streamlines
    >>> generate_all_off_body_streamlines()
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

    Examples
    --------
    >>> # Delete all off-body streamlines
    >>> delete_all_off_body_streamlines()
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

def export_all_off_body_streamlines(filename: str) -> None:
    """
    Appends lines to script state to export all off-body streamlines.


    :param filename: Filename with path to store the streamlines.

    Examples
    --------
    >>> # Export all off-body streamlines to a file
    >>> export_all_off_body_streamlines('C:/.../Test_streamlines.txt')
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

    Examples
    --------
    >>> # Generate all surface streamlines
    >>> generate_all_surface_streamlines()
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

    Examples
    --------
    >>> # Delete all surface streamlines
    >>> delete_all_surface_streamlines()
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

def export_all_surface_streamlines(output_filepath: str) -> None:
    """
    Appends lines to script state to export all on-body (surface) streamlines.


    :param output_filepath: Filename with path for the streamlines output.

    Examples
    --------
    >>> # Export all surface streamlines to a file
    >>> export_all_surface_streamlines('C:/.../Test_streamlines.txt')
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