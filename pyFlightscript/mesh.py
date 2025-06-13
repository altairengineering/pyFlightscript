from .utils import *    
from .script import script
import numpy as np

def import_mesh( geometry_filepath, units='METER', file_type='STL', clear=True):
    """
    Appends lines to script state to import a geometry into the simulation.
    

    :param units: The unit type for the geometry.
    :param file_type: Type of the geometry file.
    :param geometry_filepath: Path to the geometry file.
    :param clear: Boolean, if True, will add CLEAR to the script to delete existing geometry boundaries.
    """
    
    check_file_existence(geometry_filepath)
    
    # Valid units and file types
    valid_file_types = ["STL", "TRI", "P3D", "CSV", "INP", "STRUCTURED_QUAD", "UNSTRUCTURED_QUAD", "LAWGS", "VTK", "AC", "FAC", "OBJ"]
    
    check_valid_length_units(units)
    
    if file_type not in valid_file_types:
        raise ValueError(f"'{file_type}' is not a valid file type. Valid file types are: {', '.join(valid_file_types)}")
    
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

def ccs_import(ccs_filepath, close_component_ends="ENABLE", update_properties="DISABLE", clear_existing="ENABLE"):
    """
    Appends lines to script state to import a Component Cross-Section (CCS) geometry.
    

    :param ccs_filepath: Path to the CCS geometry file.
    :param close_component_ends: "ENABLE" or "DISABLE" hole-filling at the ends of each valid component. Default is "ENABLE".
    :param update_properties: "ENABLE" or "DISABLE" to update the simulation using the user-defined simulation properties in the file. Default is "DISABLE".
    :param clear_existing: "ENABLE" or "DISABLE" to delete all existing geometry boundaries prior to importing new geometry. Default is "ENABLE".
    """
    
    check_file_existence(ccs_filepath)

    
    # Validate values for ENABLE or DISABLE options
    valid_values = ["ENABLE", "DISABLE"]
    if close_component_ends not in valid_values:
        raise ValueError(f"'close_component_ends' value should be one of {valid_values}. Received: {close_component_ends}")
    if update_properties not in valid_values:
        raise ValueError(f"'update_properties' value should be one of {valid_values}. Received: {update_properties}")
    if clear_existing not in valid_values:
        raise ValueError(f"'clear_existing' value should be one of {valid_values}. Received: {clear_existing}")
    
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

def export_surface_mesh(file_path, file_type, surface=-1):
    """
    Appends lines to script state to export a geometry surface to an external file.
    

    :param file_path: Path to save the exported file.
    :param file_type: File type for the exported geometry. One of the following: STL, TRI, OBJ.
    :param surface: Index of the surface that should be exported. Default is -1 (exports all geometry surfaces).
    """
    
    # Validate file type
    valid_file_types = ["STL", "TRI", "OBJ"]
    if file_type not in valid_file_types:
        raise ValueError(f"'file_type' should be one of {valid_file_types}. Received: {file_type}")
    
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

def surface_rotate(frame=1, axis='X', angle=0, surfaces=[-1], 
                   split_vertices='DISABLE', adaptive_mesh='DISABLE', 
                   detach_normal_to_axis='DISABLE'):
                   
    """
    Appends lines to script state to rotate an existing surface.
    

    :param frame: Index of the coordinate system to be used. Default is 1.
    :param axis: Coordinate axis about which to rotate the surface. Default is 'X'.
    :param angle: Angle value in degrees. Default is 0.
    :param surfaces: List of surface indices to be rotated. Default is [-1] which selects all surfaces.
    :param split_vertices: ENABLE or DISABLE. Default is 'DISABLE'.
    :param adaptive_mesh: ENABLE or DISABLE. Default is 'ENABLE'.
    :param detach_normal_to_axis: ENABLE or DISABLE. Default is 'ENABLE'.

    Example usage:
    surface_rotate(1, 'X', 90, [-1], split_vertices='ENABLE', adaptive_mesh='DISABLE', detach_normal_to_axis='DISABLE')
    """
    
    # Validate axis
    valid_axes = ['X', 'Y', 'Z', '1', '2', '3']
    if axis not in valid_axes:
        raise ValueError(f"'axis' should be one of {valid_axes}. Received: {axis}")
    
    # Validate ENABLE/DISABLE options
    valid_options = ['ENABLE', 'DISABLE']
    if any(option not in valid_options for option in [split_vertices, adaptive_mesh, detach_normal_to_axis]):
        raise ValueError(f"Options 'split_vertices', 'adaptive_mesh', and 'detach_normal_to_axis' should be one of {valid_options}.")
    
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
        ", ".join(str(s) for s in surfaces),
        f"SPLIT_VERTICES {split_vertices}",
        f"ADAPTIVE_MESH {adaptive_mesh}",
        f"DETACH_NORMAL_TO_AXIS {detach_normal_to_axis}"
    ]

    script.append_lines(lines)
    return

def translate_surface_in_frame(frame=1, x=0.0, y=0.0, z=0.0, units='INCH', 
                               surface=0, split_vertices='DISABLE'):
    """
    Appends lines to script state to translate a surface with a vector.
    

    :param frame: Index of the coordinate system to be used. Default is 1.
    :param x, y, z: Translation vector values in the specified coordinate system. Default is (0.0, 0.0, 0.0).
    :param units: Unit type for translation. Default is 'INCH'.
    :param surface: Index of the surface to be translated. Default is 0 which selects all surfaces.
    :param split_vertices: ENABLE or DISABLE. Default is 'DISABLE'.
    """
    
    # Validate units
    check_valid_length_units(units)
    
    # Validate ENABLE/DISABLE option
    valid_options = ['ENABLE', 'DISABLE']
    if split_vertices not in valid_options:
        raise ValueError(f"'split_vertices' should be one of {valid_options}. Received: {split_vertices}")
    
    lines = [
        "#************************************************************************",
        "#****************** Translate a surface with a vector *******************",
        "#************************************************************************",
        "#",
        f"TRANSLATE_SURFACE_IN_FRAME {frame} {x} {y} {z} {units} {surface} {split_vertices}"
    ]

    script.append_lines(lines)
    return

def translate_surface_by_frame(frame1=1, frame2=1, surface=0):
    """
    Appends lines to script state to translate a surface from one frame to another.
    

    :param frame1: Index of initial frame. Default is 1.
    :param frame2: Index of destination frame. Default is 1.
    :param surface: Index of the surface to be translated. Default is 0 which selects all surfaces.
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Translate a surface from one frame to another *******",
        "#************************************************************************",
        "#",
        f"TRANSLATE_SURFACE_BY_FRAME {frame1} {frame2} {surface}"
    ]

    script.append_lines(lines)
    return

def surface_scale(frame=1, scale_x=1.0, scale_y=1.0, scale_z=1.0, surface=-1):
    """
    Appends lines to script state to scale existing surface(s).
    

    :param frame: Index of the coordinate system for scaling. Default is 1.
    :param scale_x: Scaling value in X direction. Default is 1.0.
    :param scale_y: Scaling value in Y direction. Default is 1.0.
    :param scale_z: Scaling value in Z direction. Default is 1.0.
    :param surface: Index of the surface to be scaled. Default is -1 which selects all surfaces.
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Scale existing surface(s) ***************************",
        "#************************************************************************",
        "#",
        f"SURFACE_SCALE {frame} {scale_x} {scale_y} {scale_z} {surface}"
    ]

    script.append_lines(lines)
    return

def surface_invert(index=1):
    """
    Appends lines to script state to invert the surface normals of a given surface.
    

    :param index: Index of the surface to be inverted. Default is 1. 
                  To invert all surfaces, specify -1.
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Invert the surface normals of a surface *************",
        "#************************************************************************",
        "#",
        f"SURFACE_INVERT {index}"
    ]

    script.append_lines(lines)
    return

def surface_rename(name, index=1):
    """
    Appends lines to script state to rename the surface geometry.
    

    :param index: Index of the surface to be renamed.
    :param name: New name to be used for the geometry surface.
    """
    
    # Type checking
    if not isinstance(index, int):
        raise ValueError("`index` should be an integer value.")
    if not isinstance(name, str):
        raise ValueError("`name` should be a string value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Rename the surface geometry *************************",
        "#************************************************************************",
        "#",
        f"SURFACE_RENAME {index} {name}"
    ]

    script.append_lines(lines)
    return

def select_geometry_by_id(surface=1):
    """
    Appends lines to script state to select a geometry surface by its index.
    

    :param surface: Index of the surface to be selected.
    """
    
    # Type checking
    if not isinstance(surface, int):
        raise TypeError("`surface` should be an integer value.")
    
    # Value checking
    if surface <= 0 and surface != -1:
        raise ValueError("`surface` should be greater than 0 or -1 to select all surfaces.")
    
    lines = [
        "#************************************************************************",
        "#****************** Select a geometry surface by its index **************",
        "#************************************************************************",
        "#",
        f"SELECT_GEOMETRY_BY_ID {surface}"
    ]

    script.append_lines(lines)
    return

def surface_select_by_threshold(frame=1, threshold='Y', min_value=0.5, 
                                max_value=2.5, range_value='ABOVE_MIN_BELOW_MAX', 
                                subset='ALL_FACES'):
    """
    Appends lines to script state to select surface faces by threshold.
    

    :param frame: Index of the coordinate system used for defining the threshold parameters.
    :param threshold: Type of the threshold.
    :param min_value: Minimum value of the threshold range.
    :param max_value: Maximum value of the threshold range.
    :param range_value: Range type.
    :param subset: Subset type.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_thresholds = ['AREA', 'QUALITY', 'X', 'Y', 'Z', 'VELOCITY', 'VX', 
                        'VY', 'VZ', 'CP', 'MACH', 'SOLVER_QUALITY']
    if threshold not in valid_thresholds:
        raise ValueError(f"`threshold` should be one of {valid_thresholds}")
    
    if not isinstance(min_value, (int, float)):
        raise ValueError("`min_value` should be an integer or float value.")
    
    if not isinstance(max_value, (int, float)):
        raise ValueError("`max_value` should be an integer or float value.")
    
    valid_ranges = ['ABOVE_MIN', 'BELOW_MAX', 'ABOVE_MIN_BELOW_MAX']
    if range_value not in valid_ranges:
        raise ValueError(f"`range_value` should be one of {valid_ranges}")
    
    valid_subsets = ['ALL_FACES', 'VISIBLE_FACES', 'SELECTED_FACES']
    if subset not in valid_subsets:
        raise ValueError(f"`subset` should be one of {valid_subsets}")
    
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

def create_new_surface_from_selection():
    """
    Appends lines to script state to create a new geometry surface 
    from the currently selected faces.
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

def surface_cut_by_plane(frame=1, plane='XZ', offset=0.0, 
                         surface=-1):
    """
    Appends lines to script state to cut surfaces using a cutting plane.
    

    :param frame: Index of the coordinate system used for defining the cutting plane.
    :param plane: Plane of the specified coordinate system used as a cutting plane.
    :param offset: Offset distance of the plane along the plane normal vector.
    :param surface: Index of the surface that must be cut.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_planes = ['ZX', 'YZ', 'XY']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")
    
    if not isinstance(offset, (int, float)):
        raise ValueError("`offset` should be an integer or float value.")
    
    if not isinstance(surface, int):
        raise ValueError("`surface` should be an integer value.")
    
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

def surface_mirror(surface=1, coordinate_system=1, mirror_plane=1, 
                   combine_flag=True, delete_source_flag=False):
    """
    Appends lines to script state to mirror an existing surface.
    

    :param surface: Index of the surface that must be mirrored.
    :param coordinate_system: Index of the coordinate system to be used.
    :param mirror_plane: Index of the mirror plane within the selected coordinate system.
    :param combine_flag: Indicate whether the mirrored geometry should be combined with the source.
    :param delete_source_flag: Indicate if the source geometry should be deleted after mirroring.
    """
    
    # Type and value checking
    if not isinstance(surface, int):
        raise ValueError("`surface` should be an integer value.")
    
    if not isinstance(coordinate_system, int):
        raise ValueError("`coordinate_system` should be an integer value.")
    
    valid_mirror_planes = [1, 2, 3]
    if mirror_plane not in valid_mirror_planes:
        raise ValueError(f"`mirror_plane` should be one of {valid_mirror_planes}")
    
    if not isinstance(combine_flag, bool):
        raise ValueError("`combine_flag` should be a boolean value.")
    
    if not isinstance(delete_source_flag, bool):
        raise ValueError("`delete_source_flag` should be a boolean value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Mirror an existing surface **************************",
        "#************************************************************************",
        "#",
        f"SURFACE_MIRROR {surface} {coordinate_system} {mirror_plane} {combine_flag} {delete_source_flag}"
    ]

    script.append_lines(lines)
    return

def surface_auto_hole_fill(surface=1):
    """
    Appends lines to script state to automatically fill holes on a surface.
    

    :param surface: Index of the surface on which the geometry holes must be filled.
    """
    
    # Type and value checking
    if not isinstance(surface, int):
        raise ValueError("`surface` should be an integer value.")
    
    if surface <= 0:
        raise ValueError("`surface` index should be greater than 0.")
    
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

def surface_combine(surface_indices):
    """
    Appends lines to script state to combine selected surfaces.

    :param surface_indices: List of surface indices to be combined.
    """
    
    # Type and value checking
    if not isinstance(surface_indices, list):
        raise ValueError("`surface_indices` should be a list of integer values.")
    
    if not all(isinstance(idx, int) for idx in surface_indices):
        raise ValueError("All elements in `surface_indices` should be integers.")
    
    surface_count = len(surface_indices)
    
    lines = [
        "#************************************************************************",
        "#****************** Combine selected surfaces ***************************",
        "#************************************************************************",
        "#",
        f"SURFACE_COMBINE {surface_count}",
        ",".join(map(str, surface_indices))
    ]

    script.append_lines(lines)
    return

def delete_selected_faces():
    """
    Appends lines to script state to delete selected mesh faces.
    

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

def surface_delete(surface_index):
    """
    Appends lines to script state to delete an existing surface.
    

    :param surface_index: Index of the surface to be deleted.
    """
    
    # Type and value checking
    if not isinstance(surface_index, int) or surface_index < 1:
        raise ValueError("`surface_index` should be an integer value greater than 0.")
    
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

def surface_clearall():
    """
    Appends lines to script state to delete all surfaces in the simulation.
    

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

def transform_selected_nodes(coordinate_system, translation_type, x, y, z):
    """
    Appends lines to script state to transform selected nodes by translation.
    

    :param coordinate_system: Index of the coordinate system to be used.
    :param translation_type: Type of translation - 'ABSOLUTE' or 'TRANSLATION'.
                             ABSOLUTE specifies the absolute values of the new XYZ coordinates.
                             TRANSLATION specifies delta increments to the current node XYZ values.
    :param x: X value of translation.
    :param y: Y value of translation.
    :param z: Z value of translation.
    
    Example usage:
        pyfs.transform_selected_nodes(1, 'TRANSLATION', -1, 0, 0)
    """
    
    # Type and value checking
    if not isinstance(coordinate_system, int):
        raise ValueError("`coordinate_system` should be an integer value.")
    
    if coordinate_system <= 0:
        raise ValueError("`coordinate_system` index should be greater than 0.")
    
    # Validate translation type
    valid_translation_types = ["ABSOLUTE", "TRANSLATION"]
    if translation_type not in valid_translation_types:
        raise ValueError(f"`translation_type` should be one of {valid_translation_types}. Received: {translation_type}")
    
    # Validate x, y, z are numeric
    for val, name in [(x, 'x'), (y, 'y'), (z, 'z')]:
        if not isinstance(val, (int, float)):
            raise ValueError(f"`{name}` should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Transform node by translation ***********************",
        "#************************************************************************",
        "#",
        f"TRANSFORM_SELECTED_NODES {coordinate_system} {translation_type} {x} {y} {z}"
    ]

    script.append_lines(lines)
    return
