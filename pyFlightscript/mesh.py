from .utils import check_file_existence, check_valid_length_units
from .script import script
from .types import *
from typing import List

def import_mesh(
    geometry_filepath: str, 
    units: ValidUnits = 'METER', 
    file_type: ValidImportMeshFileTypes = 'STL', 
    clear: bool = True
) -> None:
    """
    Import a geometry into the simulation.

    This function appends a command to the script state to import a geometry
    file, specifying units, file type, and whether to clear existing
    geometry boundaries.

    Parameters
    ----------
    geometry_filepath : str
        Path to the geometry file.
    units : ValidUnits, optional
        The unit type for the geometry, by default 'METER'.
    file_type : ValidImportMeshFileTypes, optional
        Type of the geometry file, by default 'STL'.
    clear : bool, optional
        If True, deletes existing geometry boundaries before import, by default True.

    Raises
    ------
    ValueError
        If an invalid file type or unit is provided.
    """
    check_file_existence(geometry_filepath)
    check_valid_length_units(units)
    
    if file_type not in VALID_IMPORT_MESH_FILE_TYPES:
        raise ValueError(f"'{file_type}' is not a valid file type. Valid file types are: {', '.join(VALID_IMPORT_MESH_FILE_TYPES)}")
    
    lines = [
        "#************************************************************************",
        "#****************** Import an geometry into the simulation **************",
        "#************************************************************************",
        "#",
        "IMPORT",
        f"UNITS {units}",
        f"FILE_TYPE {file_type}",
        f"FILE {geometry_filepath}"
    ]
    
    if clear:
        lines.append("CLEAR")

    script.append_lines(lines)
    return

def ccs_import(
    ccs_filepath: str, 
    close_component_ends: RunOptions = "ENABLE", 
    update_properties: RunOptions = "DISABLE", 
    clear_existing: RunOptions = "ENABLE"
) -> None:
    """
    Import a Component Cross-Section (CCS) geometry.

    This function appends a command to the script state to import a CCS
    geometry file with options for handling component ends, properties, and
    existing geometry.

    Parameters
    ----------
    ccs_filepath : str
        Path to the CCS geometry file.
    close_component_ends : RunOptions, optional
        Enable/disable hole-filling at component ends, by default "ENABLE".
    update_properties : RunOptions, optional
        Enable/disable updating simulation properties from the file, by default "DISABLE".
    clear_existing : RunOptions, optional
        Enable/disable deleting existing geometry before import, by default "ENABLE".

    Raises
    ------
    ValueError
        If any option is not 'ENABLE' or 'DISABLE'.
    """
    check_file_existence(ccs_filepath)

    for option, name in [
        (close_component_ends, 'close_component_ends'),
        (update_properties, 'update_properties'),
        (clear_existing, 'clear_existing')
    ]:
        if option not in VALID_RUN_OPTIONS:
            raise ValueError(f"'{name}' value should be one of {VALID_RUN_OPTIONS}. Received: {option}")
    
    lines = [
        "#************************************************************************",
        "#************ Import a Component Cross-Section (CCS) geometry file ******",
        "#************************************************************************",
        "#",
        "CCS_IMPORT",
        f"CLOSE_COMPONENT_ENDS {close_component_ends}",
        f"UPDATE_PROPERTIES {update_properties}",
        f"CLEAR_EXISTING {clear_existing}",
        f"FILE {ccs_filepath}"
    ]

    script.append_lines(lines)
    return

def export_surface_mesh(
    file_path: str, 
    file_type: ValidExportMeshFileTypes, 
    surface: int = -1
) -> None:
    """
    Export a geometry surface to an external file.

    This function appends a command to the script state to export one or all
    geometry surfaces to a specified file format.

    Parameters
    ----------
    file_path : str
        Path to save the exported file.
    file_type : ValidExportMeshFileTypes
        File type for the exported geometry (STL, TRI, OBJ).
    surface : int, optional
        Index of the surface to export (-1 for all surfaces), by default -1.

    Raises
    ------
    ValueError
        If an invalid file type is provided.
    """
    if file_type not in VALID_EXPORT_MESH_FILE_TYPES:
        raise ValueError(f"'file_type' should be one of {VALID_EXPORT_MESH_FILE_TYPES}. Received: {file_type}")
    
    lines = [
        "#************************************************************************",
        "#************ Export a geometry surface to external file ****************",
        "#************************************************************************",
        "#",
        f"EXPORT_SURFACE_MESH {file_type} {surface}",
        file_path
    ]

    script.append_lines(lines)
    return

def surface_rotate(
    frame: int = 1, 
    axis: ValidRotationAxis = 'X', 
    angle: float = 0, 
    surfaces: List[int] = [-1], 
    split_vertices: RunOptions = 'DISABLE', 
    adaptive_mesh: RunOptions = 'DISABLE', 
    detach_normal_to_axis: RunOptions = 'DISABLE'
) -> None:
    """
    Rotate an existing surface.

    This function appends a command to the script state to rotate specified
    surfaces around a given axis and frame.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system to be used, by default 1.
    axis : ValidRotationAxis, optional
        Coordinate axis about which to rotate the surface, by default 'X'.
    angle : float, optional
        Angle value in degrees, by default 0.
    surfaces : List[int], optional
        List of surface indices to be rotated (-1 for all), by default [-1].
    split_vertices : RunOptions, optional
        Enable/disable splitting vertices, by default 'DISABLE'.
    adaptive_mesh : RunOptions, optional
        Enable/disable adaptive meshing, by default 'DISABLE'.
    detach_normal_to_axis : RunOptions, optional
        Enable/disable detaching normals, by default 'DISABLE'.

    Raises
    ------
    ValueError
        If an invalid axis or option is provided.
    """
    if axis not in VALID_ROTATION_AXIS_LIST:
        raise ValueError(f"'axis' should be one of {VALID_ROTATION_AXIS_LIST}. Received: {axis}")
    
    for option, name in [
        (split_vertices, 'split_vertices'),
        (adaptive_mesh, 'adaptive_mesh'),
        (detach_normal_to_axis, 'detach_normal_to_axis')
    ]:
        if option not in VALID_RUN_OPTIONS:
            raise ValueError(f"'{name}' should be one of {VALID_RUN_OPTIONS}. Received: {option}")
    
    lines = [
        "#************************************************************************",
        "#****************** Rotate an existing surface **************************",
        "#************************************************************************",
        "#",
        "SURFACE_ROTATE",
        f"FRAME {frame}",
        f"AXIS {axis}",
        f"ANGLE {angle}",
        f"SURFACES {len(surfaces)}",
        ", ".join(map(str, surfaces)),
        f"SPLIT_VERTICES {split_vertices}",
        f"ADAPTIVE_MESH {adaptive_mesh}",
        f"DETACH_NORMAL_TO_AXIS {detach_normal_to_axis}"
    ]

    script.append_lines(lines)
    return

def translate_surface_in_frame(
    frame: int = 1, 
    x: float = 0.0, 
    y: float = 0.0, 
    z: float = 0.0, 
    units: ValidUnits = 'INCH', 
    surface: int = 0, 
    split_vertices: RunOptions = 'DISABLE'
) -> None:
    """
    Translate a surface with a vector.

    This function appends a command to the script state to translate a surface
    using a vector in a specified coordinate system.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system, by default 1.
    x, y, z : float, optional
        Translation vector components, by default 0.0.
    units : ValidUnits, optional
        Unit type for translation, by default 'INCH'.
    surface : int, optional
        Index of the surface to translate (0 for all), by default 0.
    split_vertices : RunOptions, optional
        Enable/disable splitting vertices, by default 'DISABLE'.

    Raises
    ------
    ValueError
        If an invalid option is provided.
    """
    check_valid_length_units(units)
    
    if split_vertices not in VALID_RUN_OPTIONS:
        raise ValueError(f"'split_vertices' should be one of {VALID_RUN_OPTIONS}. Received: {split_vertices}")
    
    lines = [
        "#************************************************************************",
        "#****************** Translate a surface with a vector *******************",
        "#************************************************************************",
        "#",
        f"TRANSLATE_SURFACE_IN_FRAME {frame} {x} {y} {z} {units} {surface} {split_vertices}"
    ]

    script.append_lines(lines)
    return

def translate_surface_by_frame(frame1: int = 1, frame2: int = 1, surface: int = 0) -> None:
    """
    Translate a surface from one frame to another.

    This function appends a command to the script state to translate a surface
    by aligning its coordinate system from an initial frame to a destination frame.

    Parameters
    ----------
    frame1 : int, optional
        Index of the initial frame, by default 1.
    frame2 : int, optional
        Index of the destination frame, by default 1.
    surface : int, optional
        Index of the surface to translate (0 for all), by default 0.
    """
    if not all(isinstance(arg, int) for arg in [frame1, frame2, surface]):
        raise TypeError("All arguments must be integers.")

    lines = [
        "#************************************************************************",
        "#****************** Translate a surface from one frame to another *******",
        "#************************************************************************",
        "#",
        f"TRANSLATE_SURFACE_BY_FRAME {frame1} {frame2} {surface}"
    ]

    script.append_lines(lines)
    return

def surface_scale(
    frame: int = 1, 
    scale_x: float = 1.0, 
    scale_y: float = 1.0, 
    scale_z: float = 1.0, 
    surface: int = -1
) -> None:
    """
    Scale existing surface(s).

    This function appends a command to the script state to scale one or all
    surfaces in a specified coordinate system.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system for scaling, by default 1.
    scale_x, scale_y, scale_z : float, optional
        Scaling factors in X, Y, and Z directions, by default 1.0.
    surface : int, optional
        Index of the surface to scale (-1 for all), by default -1.
    """
    if not isinstance(frame, int) or not all(isinstance(s, (int, float)) for s in [scale_x, scale_y, scale_z, surface]):
        raise TypeError("Frame and surface must be integers, and scaling factors must be numeric.")

    lines = [
        "#************************************************************************",
        "#****************** Scale existing surface(s) ***************************",
        "#************************************************************************",
        "#",
        f"SURFACE_SCALE {frame} {scale_x} {scale_y} {scale_z} {surface}"
    ]

    script.append_lines(lines)
    return

def surface_invert(index: int = 1) -> None:
    """
    Invert the surface normals of a given surface.

    This function appends a command to the script state to invert the normals
    of a specified surface.

    Parameters
    ----------
    index : int, optional
        Index of the surface to invert (-1 for all), by default 1.
    """
    if not isinstance(index, int):
        raise TypeError("`index` must be an integer.")

    lines = [
        "#************************************************************************",
        "#****************** Invert the surface normals of a surface *************",
        "#************************************************************************",
        "#",
        f"SURFACE_INVERT {index}"
    ]

    script.append_lines(lines)
    return

def surface_rename(name: str, index: int = 1) -> None:
    """
    Rename the surface geometry.

    This function appends a command to the script state to assign a new name
    to a specified geometry surface.

    Parameters
    ----------
    name : str
        New name for the geometry surface.
    index : int, optional
        Index of the surface to be renamed, by default 1.
    """
    if not isinstance(index, int):
        raise TypeError("`index` must be an integer.")
    if not isinstance(name, str):
        raise TypeError("`name` must be a string.")
    
    lines = [
        "#************************************************************************",
        "#****************** Rename the surface geometry *************************",
        "#************************************************************************",
        "#",
        f"SURFACE_RENAME {index} {name}"
    ]

    script.append_lines(lines)
    return

def select_geometry_by_id(surface: int = 1) -> None:
    """
    Select a geometry surface by its index.

    This function appends a command to the script state to select a geometry
    surface.

    Parameters
    ----------
    surface : int, optional
        Index of the surface to select (-1 for all), by default 1.

    Raises
    ------
    ValueError
        If the surface index is invalid.
    """
    if not isinstance(surface, int):
        raise TypeError("`surface` must be an integer.")
    if surface <= 0 and surface != -1:
        raise ValueError("`surface` must be a positive integer or -1 to select all surfaces.")
    
    lines = [
        "#************************************************************************",
        "#****************** Select a geometry surface by its index **************",
        "#************************************************************************",
        "#",
        f"SELECT_GEOMETRY_BY_ID {surface}"
    ]

    script.append_lines(lines)
    return

def surface_select_by_threshold(
    frame: int = 1, 
    threshold: ValidThresholds = 'Y', 
    min_value: float = 0.5, 
    max_value: float = 2.5, 
    range_value: ValidRanges = 'ABOVE_MIN_BELOW_MAX', 
    subset: ValidSubsets = 'ALL_FACES'
) -> None:
    """
    Select surface faces by threshold.

    This function appends a command to the script state to select surface
    faces based on a specified threshold criterion.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system for thresholding, by default 1.
    threshold : ValidThresholds, optional
        Type of threshold, by default 'Y'.
    min_value : float, optional
        Minimum value of the threshold range, by default 0.5.
    max_value : float, optional
        Maximum value of the threshold range, by default 2.5.
    range_value : ValidRanges, optional
        Type of range selection, by default 'ABOVE_MIN_BELOW_MAX'.
    subset : ValidSubsets, optional
        Subset of faces to consider, by default 'ALL_FACES'.

    Raises
    ------
    ValueError
        If any parameter is invalid.
    """
    if not isinstance(frame, int):
        raise TypeError("`frame` must be an integer.")
    if threshold not in VALID_THRESHOLD_LIST:
        raise ValueError(f"`threshold` must be one of {VALID_THRESHOLD_LIST}")
    if not isinstance(min_value, (int, float)):
        raise TypeError("`min_value` must be a numeric value.")
    if not isinstance(max_value, (int, float)):
        raise TypeError("`max_value` must be a numeric value.")
    if range_value not in VALID_RANGE_LIST:
        raise ValueError(f"`range_value` must be one of {VALID_RANGE_LIST}")
    if subset not in VALID_SUBSET_LIST:
        raise ValueError(f"`subset` must be one of {VALID_SUBSET_LIST}")
    
    lines = [
        "#************************************************************************",
        "#****************** Select surface faces by threshold *******************",
        "#************************************************************************",
        "#",
        "SURFACE_SELECT_BY_THRESHOLD",
        f"FRAME {frame}",
        f"THRESHOLD {threshold}",
        f"MIN_VALUE {min_value}",
        f"MAX_VALUE {max_value}",
        f"RANGE {range_value}",
        f"SUBSET {subset}"
    ]

    script.append_lines(lines)
    return

def create_new_surface_from_selection() -> None:
    """
    Create a new geometry surface from the currently selected faces.

    This function appends a command to the script state to generate a new
    surface from the set of currently selected faces.
    """
    lines = [
        "#************************************************************************",
        "#************** Create new geometry surface from selected faces *********",
        "#************************************************************************",
        "#",
        "CREATE_NEW_SURFACE_FROM_SELECTION"
    ]

    script.append_lines(lines)
    return

def surface_cut_by_plane(
    frame: int = 1, 
    plane: ValidPlanes = 'XZ', 
    offset: float = 0.0, 
    surface: int = -1
) -> None:
    """
    Cut surfaces using a cutting plane.

    This function appends a command to the script state to cut one or all
    surfaces with a specified plane.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system for the cutting plane, by default 1.
    plane : ValidPlanes, optional
        Plane of the coordinate system to use as the cutting plane, by default 'XZ'.
    offset : float, optional
        Offset distance of the plane along its normal vector, by default 0.0.
    surface : int, optional
        Index of the surface to cut (-1 for all), by default -1.
    """
    if not isinstance(frame, int):
        raise TypeError("`frame` must be an integer.")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` must be one of {VALID_PLANE_LIST}")
    if not isinstance(offset, (int, float)):
        raise TypeError("`offset` must be a numeric value.")
    if not isinstance(surface, int):
        raise TypeError("`surface` must be an integer.")
    
    lines = [
        "#************************************************************************",
        "#****************** Cut all surfaces using a cutting plane **************",
        "#************************************************************************",
        "#",
        "SURFACE_CUT_BY_PLANE",
        f"FRAME {frame}",
        f"PLANE {plane}",
        f"OFFSET {offset}",
        f"SURFACE {surface}"
    ]

    script.append_lines(lines)
    return

def surface_mirror(
    surface: int = 1, 
    coordinate_system: int = 1, 
    mirror_plane: int = 1, 
    combine_flag: bool = True, 
    delete_source_flag: bool = False
) -> None:
    """
    Mirror an existing surface.

    This function appends a command to the script state to mirror a surface
    across a specified plane.

    Parameters
    ----------
    surface : int, optional
        Index of the surface to mirror, by default 1.
    coordinate_system : int, optional
        Index of the coordinate system to use, by default 1.
    mirror_plane : int, optional
        Index of the mirror plane (1=XY, 2=YZ, 3=XZ), by default 1.
    combine_flag : bool, optional
        Combine the mirrored geometry with the source, by default True.
    delete_source_flag : bool, optional
        Delete the source geometry after mirroring, by default False.
    """
    if not all(isinstance(arg, int) for arg in [surface, coordinate_system, mirror_plane]):
        raise TypeError("`surface`, `coordinate_system`, and `mirror_plane` must be integers.")
    if mirror_plane not in [1, 2, 3]:
        raise ValueError("`mirror_plane` must be 1, 2, or 3.")
    if not all(isinstance(arg, bool) for arg in [combine_flag, delete_source_flag]):
        raise TypeError("`combine_flag` and `delete_source_flag` must be booleans.")
    
    lines = [
        "#************************************************************************",
        "#****************** Mirror an existing surface **************************",
        "#************************************************************************",
        "#",
        f"SURFACE_MIRROR {surface} {coordinate_system} {mirror_plane} {combine_flag} {delete_source_flag}"
    ]

    script.append_lines(lines)
    return

def surface_auto_hole_fill(surface: int = 1) -> None:
    """
    Automatically fill holes on a surface.

    This function appends a command to the script state to automatically fill
    all holes on a specified surface.

    Parameters
    ----------
    surface : int, optional
        Index of the surface to fill, by default 1.

    Raises
    ------
    ValueError
        If the surface index is not a positive integer.
    """
    if not isinstance(surface, int) or surface <= 0:
        raise ValueError("`surface` must be a positive integer.")
    
    lines = [
        "#************************************************************************",
        "#************* Automatic hole filling on an existing surface ************",
        "#************************************************************************",
        "#",
        "SURFACE_AUTO_HOLE_FILL",
        f"{surface}"
    ]

    script.append_lines(lines)
    return

def surface_combine(surface_indices: List[int]) -> None:
    """
    Combine selected surfaces.

    This function appends a command to the script state to combine multiple
    surfaces into a single surface.

    Parameters
    ----------
    surface_indices : List[int]
        List of surface indices to be combined.
    """
    if not isinstance(surface_indices, list) or not all(isinstance(idx, int) for idx in surface_indices):
        raise TypeError("`surface_indices` must be a list of integers.")
    
    lines = [
        "#************************************************************************",
        "#****************** Combine selected surfaces ***************************",
        "#************************************************************************",
        "#",
        f"SURFACE_COMBINE {len(surface_indices)}",
        ",".join(map(str, surface_indices))
    ]

    script.append_lines(lines)
    return

def delete_selected_faces() -> None:
    """

    Delete selected mesh faces.
    This function appends a command to the script state to delete all
    currently selected mesh faces.
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete selected mesh faces **************************",
        "#************************************************************************",
        "#",
        "DELETE_SELECTED_FACES"
    ]

    script.append_lines(lines)
    return

def surface_delete(surface_index: int) -> None:
    """
    Delete an existing surface.

    This function appends a command to the script state to delete a specified
    surface.

    Parameters
    ----------
    surface_index : int
        Index of the surface to be deleted.

    Raises
    ------
    ValueError
        If the surface index is not a positive integer.
    """
    if not isinstance(surface_index, int) or surface_index < 1:
        raise ValueError("`surface_index` must be an integer greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an existing surface **************************",
        "#************************************************************************",
        "#",
        "SURFACE_DELETE",
        f"SURFACE {surface_index}"
    ]

    script.append_lines(lines)
    return

def surface_clearall() -> None:
    """
    Delete all surfaces in the simulation.

    This function appends a command to the script state to delete all
    geometry surfaces currently in the simulation.
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all surfaces in simulation *******************",
        "#************************************************************************",
        "#",
        "SURFACE_CLEARALL"
    ]

    script.append_lines(lines)
    return

def transform_selected_nodes(
    coordinate_system: int, 
    translation_type: ValidTranslationTypes, 
    x: float, 
    y: float, 
    z: float
) -> None:
    """
    Transform selected nodes by translation.

    This function appends a command to the script state to transform selected
    nodes by either absolute coordinates or a translation vector.

    Parameters
    ----------
    coordinate_system : int
        Index of the coordinate system to be used.
    translation_type : ValidTranslationTypes
        Type of translation ('ABSOLUTE' or 'TRANSLATION').
    x, y, z : float
        Translation values.

    Raises
    ------
    ValueError
        If any parameter is invalid.
    """
    if not isinstance(coordinate_system, int) or coordinate_system <= 0:
        raise ValueError("`coordinate_system` must be a positive integer.")
    if translation_type not in VALID_TRANSLATION_TYPES:
        raise ValueError(f"`translation_type` must be one of {VALID_TRANSLATION_TYPES}.")
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise TypeError("`x`, `y`, and `z` must be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#****************** Transform node by translation ***********************",
        "#************************************************************************",
        "#",
        f"TRANSFORM_SELECTED_NODES {coordinate_system} {translation_type} {x} {y} {z}"
    ]

    script.append_lines(lines)
    return
