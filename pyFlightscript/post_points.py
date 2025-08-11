from . import script
from .types import VALID_PROBE_POINT_TYPE_LIST, ValidUnits, VALID_UNITS_LIST

def new_probe_point(
    probe_type: str = 'VOLUME', 
    x: float = 1.3, 
    y: float = 3.3, 
    z: float = -0.5
) -> None:
    """
    Create a new probe point.

    This function appends a command to the script state to create a single
    probe point at a specified location.

    Parameters
    ----------
    probe_type : {'VOLUME', 'SURFACE'}, optional
        The type of the probe point, by default 'VOLUME'.
    x : float, optional
        The x-coordinate of the probe point, by default 1.3.
    y : float, optional
        The y-coordinate of the probe point, by default 3.3.
    z : float, optional
        The z-coordinate of the probe point, by default -0.5.

    Examples
    --------
    >>> # Create a volume probe point at a specific location
    >>> new_probe_point('VOLUME', 1.0, 2.0, 3.0)

    >>> # Create a surface probe point with default coordinates
    >>> new_probe_point('SURFACE')
    """
    if probe_type not in VALID_PROBE_POINT_TYPE_LIST:
        raise ValueError(f"`probe_type` should be one of {VALID_PROBE_POINT_TYPE_LIST}")
    if not all(isinstance(coord, (int, float)) for coord in [x, y, z]):
        raise ValueError("Coordinates (`x`, `y`, `z`) should be numeric values.")

    lines = [
        "#************************************************************************",
        "#****************** Create a new probe point ****************************",
        "#************************************************************************",
        "#",
        f"NEW_PROBE_POINT {probe_type} {x} {y} {z}"
    ]
    script.append_lines(lines)
    return

def new_probe_line(
    num_points: int = 15, 
    x1: float = 0.0, 
    y1: float = 0.0, 
    z1: float = 0.0, 
    x2: float = 1.5, 
    y2: float = -1.0, 
    z2: float = 0.0
) -> None:
    """
    Create a new probe survey line.

    This function appends a command to the script state to create a line of
    equally spaced probe points.

    Parameters
    ----------
    num_points : int, optional
        Number of probe vertices along the survey line, by default 15.
    x1 : float, optional
        The x-coordinate of the starting point, by default 0.0.
    y1 : float, optional
        The y-coordinate of the starting point, by default 0.0.
    z1 : float, optional
        The z-coordinate of the starting point, by default 0.0.
    x2 : float, optional
        The x-coordinate of the ending point, by default 1.5.
    y2 : float, optional
        The y-coordinate of the ending point, by default -1.0.
    z2 : float, optional
        The z-coordinate of the ending point, by default 0.0.

    Examples
    --------
    >>> # Create a probe line with 20 points
    >>> new_probe_line(num_points=20, x1=0, y1=0, z1=0, x2=5, y2=0, z2=0)
    """
    if not isinstance(num_points, int):
        raise ValueError("`num_points` should be an integer value.")
    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, z1, x2, y2, z2]):
        raise ValueError("Coordinates (`x1`, `y1`, `z1`, `x2`, `y2`, `z2`) should be numeric values.")

    lines = [
        "#************************************************************************",
        "#****************** Create a new probe survey line **********************",
        "#************************************************************************",
        "#",
        f"NEW_PROBE_LINE {num_points} {x1} {y1} {z1} {x2} {y2} {z2}"
    ]
    script.append_lines(lines)
    return

def update_probe_points() -> None:
    """
    Update probe point flow properties.

    This function appends a command to the script state to update the flow
    properties at all existing probe points.

    Examples
    --------
    >>> # Update the flow properties at all probe points
    >>> update_probe_points()
    """
    lines = [
        "#************************************************************************",
        "#****************** Update probe point flow properties *****************",
        "#************************************************************************",
        "#",
        "UPDATE_PROBE_POINTS"
    ]
    script.append_lines(lines)
    return

def probe_points_import(filepath: str, units: ValidUnits = 'INCH', frame: int = 1) -> None:
    """
    Import probe points from a file.

    This function appends a command to the script state to import probe points
    from an external file.

    Parameters
    ----------
    filepath : str
        Path to the probes file.
    units : ValidUnits, optional
        Units for the probe points, by default 'INCH'.
    frame : int, optional
        Index of the coordinate system, by default 1.

    Examples
    --------
    >>> # Import probe points from a file with metric units
    >>> probe_points_import("C:/.../My_Probes.txt", units='METER', frame=2)
    """
    if not isinstance(filepath, str):
        raise ValueError("`filepath` should be a string.")
    if units not in VALID_UNITS_LIST:
        raise ValueError(f"`units` should be one of {VALID_UNITS_LIST}")
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Import probe points from file ***********************",
        "#************************************************************************",
        "#",
        "PROBE_POINTS_IMPORT",
        f"UNITS {units}",
        f"FRAME {frame}",
        filepath
    ]
    script.append_lines(lines)
    return

def export_probe_points(filepath: str) -> None:
    """
    Export probe points to a file.

    This function appends a command to the script state to export the current
    probe points to a file.

    Parameters
    ----------
    filepath : str
        Path to the file where probe points will be exported.

    Examples
    --------
    >>> # Export probe points to a text file
    >>> export_probe_points("C:/.../My_Probes_Export.txt")
    """
    if not isinstance(filepath, str):
        raise ValueError("`filepath` should be a string.")

    lines = [
        "#************************************************************************",
        "#****************** Export probe points to file *************************",
        "#************************************************************************",
        "#",
        "EXPORT_PROBE_POINTS",
        filepath
    ]
    script.append_lines(lines)
    return

def delete_probe_points() -> None:
    """
    Delete all existing probe points.

    This function appends a command to the script state to delete all probe
    points from the current session.

    Examples
    --------
    >>> # Delete all probe points
    >>> delete_probe_points()
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all existing probe points ********************",
        "#************************************************************************",
        "#",
        "DELETE_PROBE_POINTS"
    ]
    script.append_lines(lines)
    return