from typing import List
from .utils import *
from .script import script
from .types import *

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
    
    file_type = normalize_option(file_type, "file_type")
    if file_type not in VALID_IMPORT_MESH_FILE_TYPES:
        raise ValueError(f"'{file_type}' is not a valid file type. Valid file types are: {', '.join(VALID_IMPORT_MESH_FILE_TYPES)}")
    
    lines = [
        "#************************************************************************",
        "#****************** Import an geometry into the simulation **************",
        "#************************************************************************",
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

    close_component_ends = normalize_option(close_component_ends, "close_component_ends")
    update_properties = normalize_option(update_properties, "update_properties")
    clear_existing = normalize_option(clear_existing, "clear_existing")
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
    file_type = normalize_option(file_type, "file_type")
    if file_type not in VALID_EXPORT_MESH_FILE_TYPES:
        raise ValueError(f"'file_type' should be one of {VALID_EXPORT_MESH_FILE_TYPES}. Received: {file_type}")
    
    lines = [
        "#************************************************************************",
        "#************ Export a geometry surface to external file ****************",
        "#************************************************************************",
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
    axis = normalize_option(axis, "axis")
    if axis not in VALID_ROTATION_AXIS_LIST:
        raise ValueError(f"'axis' should be one of {VALID_ROTATION_AXIS_LIST}. Received: {axis}")
    
    split_vertices = normalize_option(split_vertices, "split_vertices")
    adaptive_mesh = normalize_option(adaptive_mesh, "adaptive_mesh")
    detach_normal_to_axis = normalize_option(detach_normal_to_axis, "detach_normal_to_axis")
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
    
    split_vertices = normalize_option(split_vertices, "split_vertices")
    if split_vertices not in VALID_RUN_OPTIONS:
        raise ValueError(f"'split_vertices' should be one of {VALID_RUN_OPTIONS}. Received: {split_vertices}")
    
    lines = [
        "#************************************************************************",
        "#****************** Translate a surface with a vector *******************",
        "#************************************************************************",
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
    threshold = normalize_option(threshold, "threshold")
    if threshold not in VALID_THRESHOLD_LIST:
        raise ValueError(f"`threshold` must be one of {VALID_THRESHOLD_LIST}")
    if not isinstance(min_value, (int, float)):
        raise TypeError("`min_value` must be a numeric value.")
    if not isinstance(max_value, (int, float)):
        raise TypeError("`max_value` must be a numeric value.")
    range_value = normalize_option(range_value, "range_value")
    if range_value not in VALID_RANGE_LIST:
        raise ValueError(f"`range_value` must be one of {VALID_RANGE_LIST}")
    subset = normalize_option(subset, "subset")
    if subset not in VALID_SUBSET_LIST:
        raise ValueError(f"`subset` must be one of {VALID_SUBSET_LIST}")
    
    lines = [
        "#************************************************************************",
        "#****************** Select surface faces by threshold *******************",
        "#************************************************************************",
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
    plane = normalize_option(plane, "plane")
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
    translation_type = normalize_option(translation_type, "translation_type")
    if translation_type not in VALID_TRANSLATION_TYPES:
        raise ValueError(f"`translation_type` must be one of {VALID_TRANSLATION_TYPES}.")
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise TypeError("`x`, `y`, and `z` must be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#****************** Transform node by translation ***********************",
        "#************************************************************************",
        f"TRANSFORM_SELECTED_NODES {coordinate_system} {translation_type} {x} {y} {z}"
    ]

    script.append_lines(lines)
    return


def default_ccs_wing_mesh_settings(
    direction: str = 'CHORD'
) -> None:
    """
    Apply default CCS wing mesh settings for the specified direction.

    This function appends a command to the script state to reset the CCS
    wing mesh parameters to their default values for the specified direction.

    Parameters
    ----------
    direction : str, optional
        Meshing direction ('CHORD' or 'SPAN'). Defaults to 'CHORD'.

    Raises
    ------
    ValueError
        If `direction` is not 'CHORD' or 'SPAN'.

    Examples
    --------
    >>> default_ccs_wing_mesh_settings()

    >>> default_ccs_wing_mesh_settings(direction='SPAN')
    """
    valid_directions = ['CHORD', 'SPAN']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    lines = [
        "#************************************************************************",
        "#**************** Default CCS wing mesh settings *************************",
        "#************************************************************************",
        f"DEFAULT_CCS_WING_MESH_SETTINGS {direction}"
    ]

    script.append_lines(lines)
    return


def ccs_wing_mesh_subdivisions(
    direction: str = 'CHORD',
    num_pts: int = 120
) -> None:
    """
    Set the number of CCS wing mesh subdivisions in a specified direction.

    This function appends a command to the script state to set the number
    of grid subdivisions for the CCS wing mesh in the chordwise or
    spanwise direction.

    Parameters
    ----------
    direction : str, optional
        Subdivision direction ('CHORD' or 'SPAN'). Defaults to 'CHORD'.
    num_pts : int, optional
        Number of subdivisions in the specified direction (> 0). Defaults to 120.

    Raises
    ------
    ValueError
        If `direction` is invalid or `num_pts` is not a positive integer.

    Examples
    --------
    >>> ccs_wing_mesh_subdivisions(direction='CHORD', num_pts=80)
    """
    valid_directions = ['CHORD', 'SPAN']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    if not isinstance(num_pts, int) or num_pts <= 0:
        raise ValueError("`num_pts` should be a positive integer value.")

    lines = [
        "#************************************************************************",
        "#**************** Set CCS wing mesh subdivisions *************************",
        "#************************************************************************",
        f"CCS_WING_MESH_SUBDIVISIONS {direction} {num_pts}"
    ]

    script.append_lines(lines)
    return


def ccs_wing_mesh_growth_scheme(
    direction: str = 'CHORD',
    scheme: str = 'DUAL-SIDED'
) -> None:
    """
    Set the CCS wing mesh node clustering growth scheme.

    This function appends a command to the script state to set the node
    clustering growth scheme for the CCS wing mesh in the specified direction.

    Parameters
    ----------
    direction : str, optional
        Direction of node clustering ('CHORD' or 'SPAN'). Defaults to 'CHORD'.
    scheme : str, optional
        Clustering scheme ('NONE', 'DUAL-SIDED', 'SUCCESSIVE', or 'REVERSE').
        Defaults to 'DUAL-SIDED'.

    Raises
    ------
    ValueError
        If `direction` or `scheme` is invalid.

    Examples
    --------
    >>> ccs_wing_mesh_growth_scheme(direction='SPAN', scheme='SUCCESSIVE')
    """
    valid_directions = ['CHORD', 'SPAN']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    valid_schemes = ['NONE', 'DUAL-SIDED', 'SUCCESSIVE', 'REVERSE']
    scheme = normalize_option(scheme, "scheme")
    if scheme not in valid_schemes:
        raise ValueError(f"`scheme` should be one of {valid_schemes}. Received: {scheme}")

    lines = [
        "#************************************************************************",
        "#**************** Set CCS wing mesh growth scheme ************************",
        "#************************************************************************",
        f"CCS_WING_MESH_GROWTH_SCHEME {direction} {scheme}"
    ]

    script.append_lines(lines)
    return


def ccs_wing_mesh_growth_rate(
    direction: str = 'CHORD',
    rate: float = 1.2
) -> None:
    """
    Set the CCS wing mesh node clustering growth rate.

    This function appends a command to the script state to set the node
    clustering growth rate for the CCS wing mesh in the specified direction.

    Parameters
    ----------
    direction : str, optional
        Direction of node clustering ('CHORD' or 'SPAN'). Defaults to 'CHORD'.
    rate : float, optional
        Clustering growth rate (> 0). Defaults to 1.2.

    Raises
    ------
    ValueError
        If `direction` is invalid or `rate` is not positive.

    Examples
    --------
    >>> ccs_wing_mesh_growth_rate(direction='SPAN', rate=1.1)
    """
    valid_directions = ['CHORD', 'SPAN']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    if not isinstance(rate, (int, float)) or rate <= 0:
        raise ValueError("`rate` should be a numeric value greater than zero.")

    lines = [
        "#************************************************************************",
        "#**************** Set CCS wing mesh growth rate **************************",
        "#************************************************************************",
        f"CCS_WING_MESH_GROWTH_RATE {direction} {rate}"
    ]

    script.append_lines(lines)
    return


def ccs_wing_mesh_periodicity(
    direction: str = 'CHORD',
    periodicity: int = 2
) -> None:
    """
    Set the CCS wing mesh clustering periodicity in a specified direction.

    This function appends a command to the script state to set the number
    of self-repeating clustering periods for the CCS wing mesh.

    Parameters
    ----------
    direction : str, optional
        Direction of periodicity ('CHORD' or 'SPAN'). Defaults to 'CHORD'.
    periodicity : int, optional
        Number of self-repeating periods (> 0). Defaults to 2.

    Raises
    ------
    ValueError
        If `direction` is invalid or `periodicity` is not a positive integer.

    Examples
    --------
    >>> ccs_wing_mesh_periodicity(direction='SPAN', periodicity=4)
    """
    valid_directions = ['CHORD', 'SPAN']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    if not isinstance(periodicity, int) or periodicity <= 0:
        raise ValueError("`periodicity` should be an integer value greater than zero.")

    lines = [
        "#************************************************************************",
        "#**************** Set CCS wing mesh periodicity **************************",
        "#************************************************************************",
        f"CCS_WING_MESH_PERIODICITY {direction} {periodicity}"
    ]

    script.append_lines(lines)
    return


def new_ccs_wing_refinement_zone(
    v0: float,
    v1: float,
    num_pts: int
) -> None:
    """
    Add a new spanwise refinement zone to the CCS wing mesh.

    This function appends a command to the script state to define a spanwise
    refinement zone between parametric limits v0 and v1, inserting additional
    grid nodes in that region.

    Parameters
    ----------
    v0 : float
        Inner spanwise parametric limit (0 to 1).
    v1 : float
        Outer spanwise parametric limit (0 to 1); must be greater than `v0`.
    num_pts : int
        Number of additional grid nodes to insert in the specified spanwise range.

    Raises
    ------
    ValueError
        If `v0` or `v1` are outside [0, 1], `v1` <= `v0`, or `num_pts`
        is not a positive integer.

    Examples
    --------
    >>> new_ccs_wing_refinement_zone(v0=0.8, v1=1.0, num_pts=20)
    """
    if not isinstance(v0, (int, float)) or not isinstance(v1, (int, float)):
        raise ValueError("`v0` and `v1` should be numeric values.")
    if not (0 <= v0 <= 1) or not (0 <= v1 <= 1):
        raise ValueError("`v0` and `v1` should be between 0 and 1.")
    if v1 <= v0:
        raise ValueError("`v1` should be greater than `v0`.")

    if not isinstance(num_pts, int) or num_pts <= 0:
        raise ValueError("`num_pts` should be a positive integer value.")

    lines = [
        "#************************************************************************",
        "#**************** Add new CCS wing refinement zone ***********************",
        "#************************************************************************",
        f"NEW_CCS_WING_REFINEMENT_ZONE {v0} {v1} {num_pts}"
    ]

    script.append_lines(lines)
    return


def delete_ccs_wing_refinement_zones(
    zone_index: int = -1
) -> None:
    """
    Delete one or all CCS wing mesh refinement zones.

    This function appends a command to the script state to delete a specified
    spanwise refinement zone, or all refinement zones if `zone_index` is -1.

    Parameters
    ----------
    zone_index : int, optional
        Index of the refinement zone to delete (> 0), or -1 to delete all.
        Defaults to -1.

    Raises
    ------
    ValueError
        If `zone_index` is not a positive integer or -1.

    Examples
    --------
    >>> # Delete all refinement zones
    >>> delete_ccs_wing_refinement_zones()

    >>> # Delete refinement zone 2
    >>> delete_ccs_wing_refinement_zones(zone_index=2)
    """
    if not isinstance(zone_index, int):
        raise ValueError("`zone_index` should be an integer value.")
    if zone_index == 0 or zone_index < -1:
        raise ValueError("`zone_index` should be -1 (all) or a positive integer value.")

    lines = [
        "#************************************************************************",
        "#**************** Delete CCS wing refinement zones ***********************",
        "#************************************************************************",
        f"DELETE_CCS_WING_REFINEMENT_ZONES {zone_index}"
    ]

    script.append_lines(lines)
    return


def new_ccs_wing_control_surface(
    name: str,
    v0: float,
    v1: float,
    u0: float,
    u1: float,
    hinge_height: float,
    angle: float,
    slot_gap: float
) -> None:
    """
    Define a new control surface on the CCS wing mesh.

    This function appends a command to the script state to create a control
    surface on the CCS wing mesh, defined by its spanwise and chordwise
    parametric extents, hinge geometry, deflection angle, and slot gap.

    Parameters
    ----------
    name : str
        Name to assign to this control surface.
    v0 : float
        Inner spanwise parametric limit (0 to 1).
    v1 : float
        Outer spanwise parametric limit (0 to 1); must be greater than `v0`.
    u0 : float
        Chordwise parametric depth at the inner span location (0 < u0 < 0.5).
    u1 : float
        Chordwise parametric depth at the outer span location (0 < u1 < 0.5).
    hinge_height : float
        Parametric hinge height (0 to 1).
    angle : float
        Control surface deflection angle in degrees.
    slot_gap : float
        Slot gap as a percentage of span on either side of the control surface.

    Raises
    ------
    ValueError
        If any parameter fails validation.

    Examples
    --------
    >>> new_ccs_wing_control_surface(
    ...     name='aileron', v0=0.6, v1=0.9,
    ...     u0=0.2, u1=0.2, hinge_height=0.5, angle=10.0, slot_gap=0.01
    ... )
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("`name` should be a non-empty string value.")

    for value, label in [(v0, 'v0'), (v1, 'v1')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")
        if not (0 <= value <= 1):
            raise ValueError(f"`{label}` should be between 0 and 1.")
    if v1 <= v0:
        raise ValueError("`v1` should be greater than `v0`.")

    for value, label in [(u0, 'u0'), (u1, 'u1')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")
        if not (0 < value < 0.5):
            raise ValueError(f"`{label}` should be greater than 0 and less than 0.5.")

    if not isinstance(hinge_height, (int, float)) or not (0 <= hinge_height <= 1):
        raise ValueError("`hinge_height` should be a numeric value between 0 and 1.")

    if not isinstance(angle, (int, float)):
        raise ValueError("`angle` should be a numeric value.")

    if not isinstance(slot_gap, (int, float)) or slot_gap < 0:
        raise ValueError("`slot_gap` should be a numeric value greater than or equal to zero.")

    lines = [
        "#************************************************************************",
        "#**************** Add new CCS wing control surface ***********************",
        "#************************************************************************",
        f"NEW_CCS_WING_CONTROL_SURFACE {name} {v0} {v1} {u0} {u1} {hinge_height} {angle} {slot_gap}"
    ]

    script.append_lines(lines)
    return


def new_ccs_wing_morphing_surface(
    name: str,
    v0: float,
    v1: float,
    u0: float,
    u1: float
) -> None:
    """
    Define a new morphing surface on the CCS wing mesh.

    This function appends a command to the script state to create a morphing
    surface region on the CCS wing mesh, defined by its spanwise and chordwise
    parametric extents.

    Parameters
    ----------
    name : str
        Name to assign to this morphing surface.
    v0 : float
        Inner spanwise parametric limit (0 to 1).
    v1 : float
        Outer spanwise parametric limit (0 to 1); must be greater than `v0`.
    u0 : float
        Chordwise parametric depth at the inner span location (0 < u0 < 0.5).
    u1 : float
        Chordwise parametric depth at the outer span location (0 < u1 < 0.5).

    Raises
    ------
    ValueError
        If any parameter fails validation.

    Examples
    --------
    >>> new_ccs_wing_morphing_surface(
    ...     name='flap', v0=0.0, v1=0.5, u0=0.3, u1=0.3
    ... )
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("`name` should be a non-empty string value.")

    for value, label in [(v0, 'v0'), (v1, 'v1')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")
        if not (0 <= value <= 1):
            raise ValueError(f"`{label}` should be between 0 and 1.")
    if v1 <= v0:
        raise ValueError("`v1` should be greater than `v0`.")

    for value, label in [(u0, 'u0'), (u1, 'u1')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")
        if not (0 < value < 0.5):
            raise ValueError(f"`{label}` should be greater than 0 and less than 0.5.")

    lines = [
        "#************************************************************************",
        "#**************** Add new CCS wing morphing surface **********************",
        "#************************************************************************",
        f"NEW_CCS_WING_MORPHING_SURFACE {name} {v0} {v1} {u0} {u1}"
    ]

    script.append_lines(lines)
    return


def delete_ccs_wing_control_surface(
    control_index: int = -1
) -> None:
    """
    Delete one or all CCS wing mesh control surfaces.

    This function appends a command to the script state to delete a specified
    control surface, or all control surfaces if `control_index` is -1.

    Parameters
    ----------
    control_index : int, optional
        Index of the control surface to delete (> 0), or -1 to delete all.
        Defaults to -1.

    Raises
    ------
    ValueError
        If `control_index` is not a positive integer or -1.

    Examples
    --------
    >>> # Delete all control surfaces
    >>> delete_ccs_wing_control_surface()

    >>> # Delete control surface 1
    >>> delete_ccs_wing_control_surface(control_index=1)
    """
    if not isinstance(control_index, int):
        raise ValueError("`control_index` should be an integer value.")
    if control_index == 0 or control_index < -1:
        raise ValueError("`control_index` should be -1 (all) or a positive integer value.")

    lines = [
        "#************************************************************************",
        "#**************** Delete CCS wing control surface ************************",
        "#************************************************************************",
        f"DELETE_CCS_WING_CONTROL_SURFACE {control_index}"
    ]

    script.append_lines(lines)
    return


def cad_create_wing_mesh_from_ccs(
    name: str,
    mark_trailing_edges: str = 'TRUE',
    te_geometry: str = 'SHARP',
    close_ends: str = 'TRUE',
    loft_type_u: str = 'C2',
    loft_type_v: str = 'C0'
) -> None:
    """
    Generate a CAD wing mesh from the current CCS wing mesh settings.

    This function appends a command to the script state to create a CAD wing
    boundary mesh from the configured CCS settings, assigning it the given name.

    Parameters
    ----------
    name : str
        Name to assign to the generated mesh boundary.
    mark_trailing_edges : str, optional
        Whether to mark trailing edge boundaries ('TRUE' or 'FALSE').
        Defaults to 'TRUE'.
    te_geometry : str, optional
        Trailing-edge geometry type ('SHARP', 'BLUNT', 'BLEND', or 'OPEN').
        Defaults to 'SHARP'.
    close_ends : str, optional
        Whether to close wing component ends ('TRUE', 'FALSE', 'OPEN', or 'CLOSED').
        Defaults to 'TRUE'.
    loft_type_u : str, optional
        Chordwise spline loft continuity type ('C2' or 'C0'). Defaults to 'C2'.
    loft_type_v : str, optional
        Spanwise spline loft continuity type ('C2' or 'C0'). Defaults to 'C0'.

    Raises
    ------
    ValueError
        If `name` is empty or any option parameter is invalid.

    Examples
    --------
    >>> cad_create_wing_mesh_from_ccs(name='MainWing')
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("`name` should be a non-empty string value.")

    valid_mark = ['TRUE', 'FALSE']
    mark_trailing_edges = normalize_option(mark_trailing_edges, "mark_trailing_edges")
    if mark_trailing_edges not in valid_mark:
        raise ValueError(f"`mark_trailing_edges` should be one of {valid_mark}. Received: {mark_trailing_edges}")

    valid_te_geometry = ['SHARP', 'BLUNT', 'BLEND', 'OPEN']
    te_geometry = normalize_option(te_geometry, "te_geometry")
    if te_geometry not in valid_te_geometry:
        raise ValueError(f"`te_geometry` should be one of {valid_te_geometry}. Received: {te_geometry}")

    valid_close_ends = ['TRUE', 'FALSE', 'OPEN', 'CLOSED']
    close_ends = normalize_option(close_ends, "close_ends")
    if close_ends not in valid_close_ends:
        raise ValueError(f"`close_ends` should be one of {valid_close_ends}. Received: {close_ends}")

    valid_loft_types = ['C2', 'C0']
    loft_type_u = normalize_option(loft_type_u, "loft_type_u")
    loft_type_v = normalize_option(loft_type_v, "loft_type_v")
    if loft_type_u not in valid_loft_types:
        raise ValueError(f"`loft_type_u` should be one of {valid_loft_types}. Received: {loft_type_u}")
    if loft_type_v not in valid_loft_types:
        raise ValueError(f"`loft_type_v` should be one of {valid_loft_types}. Received: {loft_type_v}")

    lines = [
        "#************************************************************************",
        "#**************** Create CAD wing mesh from CCS **************************",
        "#************************************************************************",
        f"CAD_CREATE_WING_MESH_FROM_CCS {name} {mark_trailing_edges} {te_geometry} {close_ends} {loft_type_u} {loft_type_v}"
    ]

    script.append_lines(lines)
    return


def export_wing_ccs_file(
    name: str,
    mark_trailing_edges: str = 'TRUE',
    te_geometry: str = 'SHARP',
    close_ends: str = 'TRUE',
    loft_type_u: str = 'C2',
    loft_type_v: str = 'C0',
    file_path: str = ''
) -> None:
    """
    Export wing CCS mesh settings to a file.

    This function appends a command to the script state to export the CCS
    wing mesh configuration to a file, using the specified mesh parameters.

    Parameters
    ----------
    name : str
        Name to assign to the mesh boundary in the export.
    mark_trailing_edges : str, optional
        Whether to mark trailing edge boundaries ('TRUE' or 'FALSE').
        Defaults to 'TRUE'.
    te_geometry : str, optional
        Trailing-edge geometry type ('SHARP', 'BLUNT', 'BLEND', or 'OPEN').
        Defaults to 'SHARP'.
    close_ends : str, optional
        Whether to close wing component ends ('TRUE', 'FALSE', 'OPEN', or 'CLOSED').
        Defaults to 'TRUE'.
    loft_type_u : str, optional
        Chordwise spline loft continuity type ('C2' or 'C0'). Defaults to 'C2'.
    loft_type_v : str, optional
        Spanwise spline loft continuity type ('C2' or 'C0'). Defaults to 'C0'.
    file_path : str, optional
        Output file path for the exported CCS file. Must be non-empty.

    Raises
    ------
    ValueError
        If `name` or `file_path` is empty, or any option parameter is invalid.

    Examples
    --------
    >>> export_wing_ccs_file(name='MainWing', file_path='output/wing.ccs')
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("`name` should be a non-empty string value.")

    valid_mark = ['TRUE', 'FALSE']
    mark_trailing_edges = normalize_option(mark_trailing_edges, "mark_trailing_edges")
    if mark_trailing_edges not in valid_mark:
        raise ValueError(f"`mark_trailing_edges` should be one of {valid_mark}. Received: {mark_trailing_edges}")

    valid_te_geometry = ['SHARP', 'BLUNT', 'BLEND', 'OPEN']
    te_geometry = normalize_option(te_geometry, "te_geometry")
    if te_geometry not in valid_te_geometry:
        raise ValueError(f"`te_geometry` should be one of {valid_te_geometry}. Received: {te_geometry}")

    valid_close_ends = ['TRUE', 'FALSE', 'OPEN', 'CLOSED']
    close_ends = normalize_option(close_ends, "close_ends")
    if close_ends not in valid_close_ends:
        raise ValueError(f"`close_ends` should be one of {valid_close_ends}. Received: {close_ends}")

    valid_loft_types = ['C2', 'C0']
    loft_type_u = normalize_option(loft_type_u, "loft_type_u")
    loft_type_v = normalize_option(loft_type_v, "loft_type_v")
    if loft_type_u not in valid_loft_types:
        raise ValueError(f"`loft_type_u` should be one of {valid_loft_types}. Received: {loft_type_u}")
    if loft_type_v not in valid_loft_types:
        raise ValueError(f"`loft_type_v` should be one of {valid_loft_types}. Received: {loft_type_v}")

    if not isinstance(file_path, str) or not file_path.strip():
        raise ValueError("`file_path` should be a non-empty string value.")

    lines = [
        "#************************************************************************",
        "#**************** Export wing CCS file ***********************************",
        "#************************************************************************",
        f"EXPORT_WING_CCS_FILE {name} {mark_trailing_edges} {te_geometry} {close_ends} {loft_type_u} {loft_type_v}",
        file_path
    ]

    script.append_lines(lines)
    return


def default_ccs_fuselage_mesh_settings(
    direction: str = 'AXIAL'
) -> None:
    """
    Apply default CCS fuselage mesh settings for the specified direction.

    This function appends a command to the script state to reset the CCS
    fuselage mesh parameters to their default values for the specified direction.

    Parameters
    ----------
    direction : str, optional
        Meshing direction ('AXIAL' or 'RADIAL'). Defaults to 'AXIAL'.

    Raises
    ------
    ValueError
        If `direction` is not 'AXIAL' or 'RADIAL'.

    Examples
    --------
    >>> default_ccs_fuselage_mesh_settings()

    >>> default_ccs_fuselage_mesh_settings(direction='RADIAL')
    """
    valid_directions = ['AXIAL', 'RADIAL']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    lines = [
        "#************************************************************************",
        "#************* Default CCS fuselage mesh settings ************************",
        "#************************************************************************",
        f"DEFAULT_CCS_FUSELAGE_MESH_SETTINGS {direction}"
    ]

    script.append_lines(lines)
    return


def ccs_fuselage_mesh_subdivisions(
    direction: str = 'RADIAL',
    num_pts: int = 40
) -> None:
    """
    Set the number of CCS fuselage mesh subdivisions in a specified direction.

    This function appends a command to the script state to set the number
    of grid subdivisions for the CCS fuselage mesh in the axial or
    radial direction.

    Parameters
    ----------
    direction : str, optional
        Subdivision direction ('AXIAL' or 'RADIAL'). Defaults to 'RADIAL'.
    num_pts : int, optional
        Number of subdivisions in the specified direction (> 0). Defaults to 40.

    Raises
    ------
    ValueError
        If `direction` is invalid or `num_pts` is not a positive integer.

    Examples
    --------
    >>> ccs_fuselage_mesh_subdivisions(direction='AXIAL', num_pts=60)
    """
    valid_directions = ['AXIAL', 'RADIAL']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    if not isinstance(num_pts, int) or num_pts <= 0:
        raise ValueError("`num_pts` should be a positive integer value.")

    lines = [
        "#************************************************************************",
        "#************* Set CCS fuselage mesh subdivisions ************************",
        "#************************************************************************",
        f"CCS_FUSELAGE_MESH_SUBDIVISIONS {direction} {num_pts}"
    ]

    script.append_lines(lines)
    return


def ccs_fuselage_mesh_growth_scheme(
    direction: str = 'AXIAL',
    scheme: str = 'DUAL-SIDED'
) -> None:
    """
    Set the CCS fuselage mesh node clustering growth scheme.

    This function appends a command to the script state to set the node
    clustering growth scheme for the CCS fuselage mesh in the specified direction.

    Parameters
    ----------
    direction : str, optional
        Direction of node clustering ('AXIAL' or 'RADIAL'). Defaults to 'AXIAL'.
    scheme : str, optional
        Clustering scheme ('NONE', 'DUAL-SIDED', 'SUCCESSIVE', or 'REVERSE').
        Defaults to 'DUAL-SIDED'.

    Raises
    ------
    ValueError
        If `direction` or `scheme` is invalid.

    Examples
    --------
    >>> ccs_fuselage_mesh_growth_scheme(direction='RADIAL', scheme='SUCCESSIVE')
    """
    valid_directions = ['AXIAL', 'RADIAL']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    valid_schemes = ['NONE', 'DUAL-SIDED', 'SUCCESSIVE', 'REVERSE']
    scheme = normalize_option(scheme, "scheme")
    if scheme not in valid_schemes:
        raise ValueError(f"`scheme` should be one of {valid_schemes}. Received: {scheme}")

    lines = [
        "#************************************************************************",
        "#************* Set CCS fuselage mesh growth scheme ************************",
        "#************************************************************************",
        f"CCS_FUSELAGE_MESH_GROWTH_SCHEME {direction} {scheme}"
    ]

    script.append_lines(lines)
    return


def ccs_fuselage_mesh_growth_rate(
    direction: str = 'AXIAL',
    rate: float = 1.1
) -> None:
    """
    Set the CCS fuselage mesh node clustering growth rate.

    This function appends a command to the script state to set the node
    clustering growth rate for the CCS fuselage mesh in the specified direction.

    Parameters
    ----------
    direction : str, optional
        Direction of node clustering ('AXIAL' or 'RADIAL'). Defaults to 'AXIAL'.
    rate : float, optional
        Clustering growth rate (> 0). Defaults to 1.1.

    Raises
    ------
    ValueError
        If `direction` is invalid or `rate` is not positive.

    Examples
    --------
    >>> ccs_fuselage_mesh_growth_rate(direction='RADIAL', rate=1.2)
    """
    valid_directions = ['AXIAL', 'RADIAL']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    if not isinstance(rate, (int, float)) or rate <= 0:
        raise ValueError("`rate` should be a numeric value greater than zero.")

    lines = [
        "#************************************************************************",
        "#************* Set CCS fuselage mesh growth rate *************************",
        "#************************************************************************",
        f"CCS_FUSELAGE_MESH_GROWTH_RATE {direction} {rate}"
    ]

    script.append_lines(lines)
    return


def ccs_fuselage_mesh_periodicity(
    direction: str = 'RADIAL',
    periodicity: int = 1
) -> None:
    """
    Set the CCS fuselage mesh clustering periodicity in a specified direction.

    This function appends a command to the script state to set the number
    of self-repeating clustering periods for the CCS fuselage mesh.

    Parameters
    ----------
    direction : str, optional
        Direction of periodicity ('AXIAL' or 'RADIAL'). Defaults to 'RADIAL'.
    periodicity : int, optional
        Number of self-repeating periods (> 0). Defaults to 1.

    Raises
    ------
    ValueError
        If `direction` is invalid or `periodicity` is not a positive integer.

    Examples
    --------
    >>> ccs_fuselage_mesh_periodicity(direction='AXIAL', periodicity=2)
    """
    valid_directions = ['AXIAL', 'RADIAL']
    direction = normalize_option(direction, "direction")
    if direction not in valid_directions:
        raise ValueError(f"`direction` should be one of {valid_directions}. Received: {direction}")

    if not isinstance(periodicity, int) or periodicity <= 0:
        raise ValueError("`periodicity` should be an integer value greater than zero.")

    lines = [
        "#************************************************************************",
        "#************* Set CCS fuselage mesh periodicity *************************",
        "#************************************************************************",
        f"CCS_FUSELAGE_MESH_PERIODICITY {direction} {periodicity}"
    ]

    script.append_lines(lines)
    return


def new_ccs_fuselage_relaxed_te(
    u: float,
    v0: float,
    v1: float
) -> None:
    """
    Add a new relaxed trailing-edge boundary to the CCS fuselage mesh.

    This function appends a command to the script state to define a relaxed
    trailing-edge boundary on the CCS fuselage mesh at the specified radial
    and axial parametric locations.

    Parameters
    ----------
    u : float
        Radial parametric location of the relaxed trailing-edge boundary (0 to 1).
    v0 : float
        Axial parametric inner limit (0 to 1).
    v1 : float
        Axial parametric outer limit (0 to 1); must be greater than `v0`.

    Raises
    ------
    ValueError
        If any value is outside [0, 1] or `v1` <= `v0`.

    Examples
    --------
    >>> new_ccs_fuselage_relaxed_te(u=0.0, v0=0.2, v1=0.8)
    """
    for value, label in [(u, 'u'), (v0, 'v0'), (v1, 'v1')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")
        if not (0 <= value <= 1):
            raise ValueError(f"`{label}` should be between 0 and 1.")

    if v1 <= v0:
        raise ValueError("`v1` should be greater than `v0`.")

    lines = [
        "#************************************************************************",
        "#************* Add new CCS fuselage relaxed TE ***************************",
        "#************************************************************************",
        f"NEW_CCS_FUSELAGE_RELAXED_TE {u} {v0} {v1}"
    ]

    script.append_lines(lines)
    return


def delete_ccs_fuselage_relaxed_te(
    index: int = -1
) -> None:
    """
    Delete one or all CCS fuselage relaxed trailing-edge boundaries.

    This function appends a command to the script state to delete a specified
    relaxed trailing-edge boundary, or all boundaries if `index` is -1.

    Parameters
    ----------
    index : int, optional
        Index of the boundary to delete (> 0), or -1 to delete all.
        Defaults to -1.

    Raises
    ------
    ValueError
        If `index` is not a positive integer or -1.

    Examples
    --------
    >>> # Delete all relaxed TE boundaries
    >>> delete_ccs_fuselage_relaxed_te()

    >>> # Delete boundary 1
    >>> delete_ccs_fuselage_relaxed_te(index=1)
    """
    if not isinstance(index, int):
        raise ValueError("`index` should be an integer value.")
    if index == 0 or index < -1:
        raise ValueError("`index` should be -1 (all) or a positive integer value.")

    lines = [
        "#************************************************************************",
        "#************* Delete CCS fuselage relaxed TE ****************************",
        "#************************************************************************",
        f"DELETE_CCS_FUSELAGE_RELAXED_TE {index}"
    ]

    script.append_lines(lines)
    return


def cad_create_fuselage_mesh_from_ccs(
    name: str,
    close_ends: str = 'CLOSED',
    loft_type_u: str = 'C2',
    loft_type_v: str = 'C2'
) -> None:
    """
    Generate a CAD fuselage mesh from the current CCS fuselage mesh settings.

    This function appends a command to the script state to create a CAD fuselage
    boundary mesh from the configured CCS settings, assigning it the given name.

    Parameters
    ----------
    name : str
        Name to assign to the generated mesh boundary.
    close_ends : str, optional
        Whether to close fuselage ends ('OPEN' or 'CLOSED'). Defaults to 'CLOSED'.
    loft_type_u : str, optional
        Radial spline loft continuity type ('C2' or 'C0'). Defaults to 'C2'.
    loft_type_v : str, optional
        Axial spline loft continuity type ('C2' or 'C0'). Defaults to 'C2'.

    Raises
    ------
    ValueError
        If `name` is empty or any option parameter is invalid.

    Examples
    --------
    >>> cad_create_fuselage_mesh_from_ccs(name='Fuselage')
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("`name` should be a non-empty string value.")

    valid_close_ends = ['OPEN', 'CLOSED']
    close_ends = normalize_option(close_ends, "close_ends")
    if close_ends not in valid_close_ends:
        raise ValueError(f"`close_ends` should be one of {valid_close_ends}. Received: {close_ends}")

    valid_loft_types = ['C2', 'C0']
    loft_type_u = normalize_option(loft_type_u, "loft_type_u")
    loft_type_v = normalize_option(loft_type_v, "loft_type_v")
    if loft_type_u not in valid_loft_types:
        raise ValueError(f"`loft_type_u` should be one of {valid_loft_types}. Received: {loft_type_u}")
    if loft_type_v not in valid_loft_types:
        raise ValueError(f"`loft_type_v` should be one of {valid_loft_types}. Received: {loft_type_v}")

    lines = [
        "#************************************************************************",
        "#************* Create CAD fuselage mesh from CCS *************************",
        "#************************************************************************",
        f"CAD_CREATE_FUSELAGE_MESH_FROM_CCS {name} {close_ends} {loft_type_u} {loft_type_v}"
    ]

    script.append_lines(lines)
    return


def export_fuselage_ccs_file(
    name: str,
    close_ends: str = 'CLOSED',
    loft_type_u: str = 'C2',
    loft_type_v: str = 'C0',
    file_path: str = ''
) -> None:
    """
    Export fuselage CCS mesh settings to a file.

    This function appends a command to the script state to export the CCS
    fuselage mesh configuration to a file using the specified mesh parameters.

    Parameters
    ----------
    name : str
        Name to assign to the mesh boundary in the export.
    close_ends : str, optional
        Whether to close fuselage ends ('OPEN' or 'CLOSED'). Defaults to 'CLOSED'.
    loft_type_u : str, optional
        Radial spline loft continuity type ('C2' or 'C0'). Defaults to 'C2'.
    loft_type_v : str, optional
        Axial spline loft continuity type ('C2' or 'C0'). Defaults to 'C0'.
    file_path : str, optional
        Output file path for the exported CCS file. Must be non-empty.

    Raises
    ------
    ValueError
        If `name` or `file_path` is empty, or any option parameter is invalid.

    Examples
    --------
    >>> export_fuselage_ccs_file(name='Fuselage', file_path='output/fuselage.ccs')
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("`name` should be a non-empty string value.")

    valid_close_ends = ['OPEN', 'CLOSED']
    close_ends = normalize_option(close_ends, "close_ends")
    if close_ends not in valid_close_ends:
        raise ValueError(f"`close_ends` should be one of {valid_close_ends}. Received: {close_ends}")

    valid_loft_types = ['C2', 'C0']
    loft_type_u = normalize_option(loft_type_u, "loft_type_u")
    loft_type_v = normalize_option(loft_type_v, "loft_type_v")
    if loft_type_u not in valid_loft_types:
        raise ValueError(f"`loft_type_u` should be one of {valid_loft_types}. Received: {loft_type_u}")
    if loft_type_v not in valid_loft_types:
        raise ValueError(f"`loft_type_v` should be one of {valid_loft_types}. Received: {loft_type_v}")

    if not isinstance(file_path, str) or not file_path.strip():
        raise ValueError("`file_path` should be a non-empty string value.")

    lines = [
        "#************************************************************************",
        "#************* Export fuselage CCS file **********************************",
        "#************************************************************************",
        f"EXPORT_FUSELAGE_CCS_FILE {name} {close_ends} {loft_type_u} {loft_type_v}",
        file_path
    ]

    script.append_lines(lines)
    return
