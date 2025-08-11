from .utils import *    
from .script import script
from .types import *

def create_new_rectangle_volume_section(
    frame: int = 1,
    plane: str = 'XZ',
    offset: float = 0.0,
    size: float = -0.5,
    x1: float = -2.5,
    y1: float = -1.0,
    x2: float = 2.5,
    y2: float = 1.0,
    prisms_type: str = 'PRISMS',
    thickness: float = 0.3,
    layers: int = 20,
    growth_rate: float = 1.2
) -> None:
    """
    Create a new rectangular volume section.

    This function appends a command to the script state to create a volume
    section with a rectangular shape for detailed analysis.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system, by default 1.
    plane : str, optional
        Section plane, by default 'XZ'. Must be one of `VALID_PLANE_LIST`.
    offset : float, optional
        Offset distance of the plane, by default 0.0.
    size : float, optional
        Refinement size, by default -0.5.
    x1 : float, optional
        x-coordinate of the first diagonal corner, by default -2.5.
    y1 : float, optional
        y-coordinate of the first diagonal corner, by default -1.0.
    x2 : float, optional
        x-coordinate of the second diagonal corner, by default 2.5.
    y2 : float, optional
        y-coordinate of the second diagonal corner, by default 1.0.
    prisms_type : str, optional
        Option for near-wall prismatic cells, by default 'PRISMS'.
        Must be one of `VALID_PRISMS_TYPE_LIST`.
    thickness : float, optional
        Thickness of the prism layer, by default 0.3.
    layers : int, optional
        Number of layers in the prism layer, by default 20.
    growth_rate : float, optional
        Growth rate of prism cells, by default 1.2.

    Examples
    --------
    >>> create_new_rectangle_volume_section(plane='XY', offset=5.0, size=-0.2)
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` must be an integer.")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` must be one of {VALID_PLANE_LIST}")
    if not all(isinstance(v, (int, float)) for v in [offset, size, x1, y1, x2, y2, thickness, growth_rate]):
        raise ValueError("Numeric parameters must be of type int or float.")
    if prisms_type not in VALID_PRISMS_TYPE_LIST:
        raise ValueError(f"`prisms_type` must be one of {VALID_PRISMS_TYPE_LIST}")
    if not isinstance(layers, int):
        raise ValueError("`layers` must be an integer.")

    lines = [
        "#************************************************************************",
        "#****************** Create new volume section (rectangle) ***************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_RECTANGLE_VOLUME_SECTION {frame} {plane} {offset} {size} {x1} {y1} {x2} {y2} {prisms_type} {thickness} {layers} {growth_rate}"
    ]
    script.append_lines(lines)
    return

def create_new_circle_volume_section(
    frame: int = 1,
    plane: str = 'XZ',
    offset: float = 0.1,
    ipts: int = 20,
    jpts: int = 40,
    r1: float = 0.0,
    r2: float = 2.5,
    prisms_type: str = 'PRISMS',
    thickness: float = 0.3,
    layers: int = 20,
    growth_rate: float = 1.2
) -> None:
    """
    Create a new circular volume section.

    This function appends a command to the script state to create a volume
    section with a circular or annular shape.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system, by default 1.
    plane : str, optional
        Section plane, by default 'XZ'. Must be one of `VALID_PLANE_LIST`.
    offset : float, optional
        Offset distance of the plane, by default 0.1.
    ipts : int, optional
        Number of radial segments, by default 20.
    jpts : int, optional
        Number of azimuth segments, by default 40.
    r1 : float, optional
        Inner radius of the circular section, by default 0.0.
    r2 : float, optional
        Outer radius of the circular section, by default 2.5.
    prisms_type : str, optional
        Option for near-wall prismatic cells, by default 'PRISMS'.
        Must be one of `VALID_PRISMS_TYPE_LIST`.
    thickness : float, optional
        Thickness of the prism layer, by default 0.3.
    layers : int, optional
        Number of layers in the prism layer, by default 20.
    growth_rate : float, optional
        Growth rate of prism cells, by default 1.2.

    Examples
    --------
    >>> create_new_circle_volume_section(r1=1.0, r2=3.0, ipts=30, jpts=60)
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` must be an integer.")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` must be one of {VALID_PLANE_LIST}")
    if not all(isinstance(v, (int, float)) for v in [offset, r1, r2, thickness, growth_rate]):
        raise ValueError("Numeric parameters must be of type int or float.")
    if not all(isinstance(v, int) for v in [ipts, jpts, layers]):
        raise ValueError("`ipts`, `jpts`, and `layers` must be integers.")
    if prisms_type not in VALID_PRISMS_TYPE_LIST:
        raise ValueError(f"`prisms_type` must be one of {VALID_PRISMS_TYPE_LIST}")

    lines = [
        "#************************************************************************",
        "#****************** Create new volume section (circle) ******************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_CIRCLE_VOLUME_SECTION {frame} {plane} {offset} {ipts} {jpts} {r1} {r2} {prisms_type} {thickness} {layers} {growth_rate}"
    ]
    script.append_lines(lines)
    return

def volume_section_boundary_layer(index: int, setting: RunOptions = 'DISABLE') -> None:
    """
    Toggle volume section boundary layer induction.

    This function appends a command to the script state to enable or disable
    boundary layer induction for a specific volume section.

    Parameters
    ----------
    index : int
        Index of the volume section to modify (> 0).
    setting : RunOptions, optional
        The setting to apply, by default 'DISABLE'. Must be one of `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Enable boundary layer induction for volume section 2
    >>> volume_section_boundary_layer(2, 'ENABLE')
    """
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` must be an integer greater than 0.")
    if setting not in VALID_RUN_OPTIONS:
        raise ValueError(f"`setting` must be one of {VALID_RUN_OPTIONS}")

    lines = [
        "#************************************************************************",
        "#*************** Toggle volume section boundary layer induction *********",
        "#************************************************************************",
        "#",
        f"VOLUME_SECTION_BOUNDARY_LAYER {index} {setting}"
    ]
    script.append_lines(lines)
    return

def volume_section_wireframe(index: int, setting: RunOptions = 'ENABLE') -> None:
    """
    Toggle volume section wireframe visibility.

    This function appends a command to the script state to show or hide the
    wireframe for a specific volume section.

    Parameters
    ----------
    index : int
        Index of the volume section to modify (> 0).
    setting : RunOptions, optional
        The setting to apply, by default 'ENABLE'. Must be one of `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Disable wireframe for volume section 3
    >>> volume_section_wireframe(3, 'DISABLE')
    """
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` must be an integer greater than 0.")
    if setting not in VALID_RUN_OPTIONS:
        raise ValueError(f"`setting` must be one of {VALID_RUN_OPTIONS}")

    lines = [
        "#************************************************************************",
        "#****************** Toggle volume section wire-frame setting ************",
        "#************************************************************************",
        "#",
        f"VOLUME_SECTION_WIREFRAME {index} {setting}"
    ]
    script.append_lines(lines)
    return

def update_all_volume_sections() -> None:
    """
    Update all volume sections.

    This function appends a command to the script state to regenerate and
    update all existing volume sections based on the current flow solution.

    Examples
    --------
    >>> # Update all volume sections
    >>> update_all_volume_sections()
    """
    lines = [
        "#************************************************************************",
        "#****************** Update the volume sections **************************",
        "#************************************************************************",
        "#",
        "UPDATE_ALL_VOLUME_SECTIONS"
    ]
    script.append_lines(lines)
    return

def export_volume_section_vtk(index: int, filename: str) -> None:
    """
    Export a volume section as a ParaView (VTK) file.

    This function appends a command to the script state to export a specific
    volume section to a VTK file for visualization in ParaView.

    Parameters
    ----------
    index : int
        Index of the volume section to be exported (> 0).
    filename : str
        The absolute path to the desired output VTK file.

    Examples
    --------
    >>> # Export volume section 2 to a VTK file
    >>> export_volume_section_vtk(2, 'C:/data/volume_section_2.vtk')
    """
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` must be an integer greater than 0.")
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string.")

    lines = [
        "#************************************************************************",
        "#****************** Export volume section as ParaView (VTK) file ********",
        "#************************************************************************",
        "#",
        f"EXPORT_VOLUME_SECTION_VTK {index}",
        filename
    ]
    script.append_lines(lines)
    return

def export_volume_section_2d_vtk(index: int, filename: str) -> None:
    """
    Export a volume section as a 2D ParaView (VTK) file.

    This function appends a command to the script state to export a specific
    volume section to a 2D VTK file.

    Parameters
    ----------
    index : int
        Index of the volume section to be exported (> 0).
    filename : str
        The absolute path to the desired output VTK file.

    Examples
    --------
    >>> # Export volume section 1 as a 2D VTK file
    >>> export_volume_section_2d_vtk(1, 'C:/data/volume_section_2d.vtk')
    """
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` must be an integer greater than 0.")
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string.")

    lines = [
        "#************************************************************************",
        "#************* Export volume section as 2D ParaView (VTK) file **********",
        "#************************************************************************",
        "#",
        f"EXPORT_VOLUME_SECTION_2D_VTK {index}",
        filename
    ]
    script.append_lines(lines)
    return

def export_volume_section_tecplot(index: int, filename: str) -> None:
    """
    Export a volume section as a Tecplot (DAT) file.

    This function appends a command to the script state to export a specific
    volume section to a Tecplot DAT file.

    Parameters
    ----------
    index : int
        Index of the volume section to be exported (> 0).
    filename : str
        The absolute path to the desired output DAT file.

    Examples
    --------
    >>> # Export volume section 4 to a Tecplot file
    >>> export_volume_section_tecplot(4, 'C:/data/volume_section_4.dat')
    """
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` must be an integer greater than 0.")
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string.")

    lines = [
        "#************************************************************************",
        "#****************** Export volume section as Tecplot (DAT) file *********",
        "#************************************************************************",
        "#",
        f"EXPORT_VOLUME_SECTION_TECPLOT {index}",
        filename
    ]
    script.append_lines(lines)
    return

def delete_volume_section(index: int) -> None:
    """
    Delete a particular volume section.

    This function appends a command to the script state to delete a specific
    volume section by its index.

    Parameters
    ----------
    index : int
        Index of the volume section to be deleted (> 0).

    Examples
    --------
    >>> # Delete volume section 2
    >>> delete_volume_section(2)
    """
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` must be an integer greater than 0.")

    lines = [
        "#************************************************************************",
        "#****************** Delete a volume section *****************************",
        "#************************************************************************",
        "#",
        f"DELETE_VOLUME_SECTION {index}"
    ]
    script.append_lines(lines)
    return

def delete_all_volume_sections() -> None:
    """
    Delete all volume sections.

    This function appends a command to the script state to delete all existing
    volume sections.

    Examples
    --------
    >>> # Delete all volume sections
    >>> delete_all_volume_sections()
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all volume sections **************************",
        "#************************************************************************",
        "#",
        "DELETE_ALL_VOLUME_SECTIONS"
    ]
    script.append_lines(lines)
    return


