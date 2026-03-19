from typing import Union, Optional, Literal, List
from .utils import *
from .script import script
from .types import *

def cad_create_initialize(model_index: int = 1) -> None:
    """
    Initialize the CAD->Create pane window.

    This function appends a command to the script state to initialize the
    CAD->Create pane window and link it to a specified model index.

    Parameters
    ----------
    model_index : int, optional
        The model index to which the CAD->Create pane is linked.
        Defaults to 1.

    Raises
    ------
    ValueError
        If `model_index` is not a positive integer.

    Examples
    --------
    >>> # Initialize the CAD->Create pane for model index 2
    >>> cad_create_initialize(model_index=2)

    >>> # Initialize the CAD->Create pane with the default model index
    >>> cad_create_initialize()
    """
    if not isinstance(model_index, int) or model_index <= 0:
        raise ValueError("`model_index` should be a positive integer value.")
        
    lines = [
        "#************************************************************************",
        "#****************** Initialize the CAD-->Create pane window *************",
        "#************************************************************************",
        f"CAD_CREATE_INITIALIZE {model_index}"
    ]

    script.append_lines(lines)
    return

def cad_create_import_curve_txt(
    txt_filepath: str,
    units: ValidUnits = 'METER',
    dimension: ValidDimensions = '2D',
    frame: int = 1,
    plane: ValidPlanes = 'YZ'
) -> None:
    """
    Import a CAD->Create drawing curve from a text file.

    This function appends a command to the script state to import a drawing
    curve from a specified text file with given parameters.

    Parameters
    ----------
    txt_filepath : str
        The absolute path to the text file to import.
    units : ValidUnits, optional
        The units for the imported curve. Defaults to 'METER'.
    dimension : ValidDimensions, optional
        The dimension of the curve, either '2D' or '3D'. Defaults to '2D'.
    frame : int, optional
        The coordinate system frame index. Defaults to 1.
    plane : ValidPlanes, optional
        The plane orientation for 2D curves ('XY', 'XZ', 'YZ').
        Defaults to 'YZ'.

    Raises
    ------
    FileNotFoundError
        If `txt_filepath` does not exist.
    ValueError
        If `units`, `dimension`, or `plane` are not valid options, or if
        `frame` is not a positive integer.

    Examples
    --------
    >>> # Import a 2D curve from a text file with default parameters
    >>> cad_create_import_curve_txt(txt_filepath='C:/path/to/curve.txt')

    >>> # Import a 3D curve with specified units
    >>> cad_create_import_curve_txt(
    ...     txt_filepath='C:/path/to/3d_curve.txt',
    ...     units='INCH',
    ...     dimension='3D'
    ... )
    """
    check_file_existence(txt_filepath)

    units = normalize_option(units, "units")
    if units not in VALID_UNITS_LIST:
        raise ValueError(f"Invalid units: {units}. Must be one of {VALID_UNITS_LIST}.")
    
    dimension = normalize_option(dimension, "dimension")
    if dimension not in VALID_DIMENSIONS_LIST:
        raise ValueError(f"Invalid dimension: {dimension}. Must be one of {VALID_DIMENSIONS_LIST}.")
    
    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"Invalid plane: {plane}. Must be one of {VALID_PLANE_LIST}.")

    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` must be a positive integer.")

    lines = [
        "#************************************************************************",
        "#*************** Import a CAD-->Create drawing curve from txt file ******",
        "#************************************************************************",
        f"CAD_CREATE_IMPORT_CURVE_TXT {units} {dimension} {frame} {plane}",
        txt_filepath
    ]

    script.append_lines(lines)
    return

def cad_create_import_ccs(ccs_filepath: str) -> None:
    """
    Import a CAD->Create drawing curve from a CCS file.

    This function appends a command to the script state to import a drawing
    curve from a specified CCS (Curve-Curve-Section) file.

    Parameters
    ----------
    ccs_filepath : str
        The absolute path to the CCS file to import.

    Raises
    ------
    FileNotFoundError
        If `ccs_filepath` does not exist.

    Examples
    --------
    >>> # Import a curve from a CCS file
    >>> cad_create_import_ccs(ccs_filepath='C:/path/to/curve.ccs')
    """
    check_file_existence(ccs_filepath)
    
    lines = [
        "#************************************************************************",
        "#*************** Import a CAD-->Create drawing curve from CSV file ******",
        "#************************************************************************",
        "CAD_CREATE_IMPORT_CURVE_CCS",
        ccs_filepath
    ]

    script.append_lines(lines)
    return

def cad_create_auto_cross_sections(
    frame: int = 1,
    axis: ValidAxis = 'Y',
    sections: int = 20,
    body_index: int = 1,
    growth_scheme: ValidGrowthScheme = 3,
    growth_rate: float = 1.2,
    symmetry: ValidSymmetry = 'NONE',
    cad_mesh: ValidCadMesh = 'MESH'
) -> None:
    """
    Create automatic cross-sections from a mesh or CAD body.

    This function appends a command to the script state to create a series
    of automatic cross-sections from a specified mesh or CAD body.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system to be used. Defaults to 1.
    axis : ValidAxis, optional
        Sweep direction for creating cross-section curves ('X', 'Y', 'Z').
        Defaults to 'Y'.
    sections : int, optional
        Number of cross-sections to create (> 1). Defaults to 20.
    body_index : int, optional
        Index of the mesh or CAD body to use. Defaults to 1.
    growth_scheme : ValidGrowthScheme, optional
        Clustering scheme for positioning cross-sections.
        1: Uniform, 2: Successive, 3: Dual-successive, 4: Reverse-successive.
        Defaults to 3.
    growth_rate : float, optional
        Growth rate for the selected growth scheme. Defaults to 1.2.
    symmetry : ValidSymmetry, optional
        Symmetry plane ('XY', 'XZ', 'YZ') for half-sections, or 'NONE' for
        full sections. Defaults to 'NONE'.
    cad_mesh : ValidCadMesh, optional
        Specifies whether to use the 'CAD' or 'MESH' body. Defaults to 'MESH'.

    Raises
    ------
    ValueError
        If any of the input parameters are invalid.

    Examples
    --------
    >>> # Create default automatic cross-sections
    >>> cad_create_auto_cross_sections()

    >>> # Create 50 cross-sections along the X-axis with uniform growth
    >>> cad_create_auto_cross_sections(
    ...     axis='X', sections=50, growth_scheme=1, growth_rate=1.0
    ... )
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be a positive integer value.")
    
    axis = normalize_option(axis, "axis")
    if axis not in VALID_AXIS_LIST:
        raise ValueError(f"`axis` should be one of {VALID_AXIS_LIST}. Received: {axis}")
    
    if not isinstance(sections, int) or sections <= 1:
        raise ValueError("`sections` should be an integer greater than 1.")
    
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("`body_index` should be a positive integer value.")
    
    if growth_scheme not in VALID_GROWTH_SCHEME_LIST:
        raise ValueError(f"`growth_scheme` should be one of {VALID_GROWTH_SCHEME_LIST}. Received: {growth_scheme}")
    
    if not isinstance(growth_rate, (int, float)) or growth_rate <= 0:
        raise ValueError("`growth_rate` should be a positive numeric value.")
    
    symmetry = normalize_option(symmetry, "symmetry")
    if symmetry not in VALID_SYMMETRY_LIST:
        raise ValueError(f"`symmetry` should be one of {VALID_SYMMETRY_LIST}. Received: {symmetry}")
    
    cad_mesh = normalize_option(cad_mesh, "cad_mesh")
    if cad_mesh not in VALID_CAD_MESH_LIST:
        raise ValueError(f"`cad_mesh` should be one of {VALID_CAD_MESH_LIST}. Received: {cad_mesh}")
    
    lines = [
        "#************************************************************************",
        "#****** Create a series of automatic cross-sections from mesh body ******",
        "#************************************************************************",
        f"CAD_CREATE_AUTO_CROSS_SECTIONS {frame} {axis} {sections} {body_index} {growth_scheme} {growth_rate} {symmetry} {cad_mesh}"
    ]

    script.append_lines(lines)
    return

def cad_create_cross_section(
    frame: int = 1,
    plane: ValidPlanes = 'XZ',
    offset: float = 0.0,
    body_index: int = 1,
    quadrant: ValidQuadrant = 3
) -> None:
    """
    Create a cross-section from an existing mesh body.

    This function appends a command to the script state to create a
    cross-section from an existing mesh body with specified parameters.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system to be used. Defaults to 1.
    plane : ValidPlanes, optional
        Plane of the coordinate system for slicing ('XY', 'XZ', 'YZ').
        Defaults to 'XZ'.
    offset : float, optional
        Offset distance of the plane along its normal axis. Defaults to 0.0.
    body_index : int, optional
        Index of the mesh body to use for creating the cross-section.
        Defaults to 1.
    quadrant : ValidQuadrant, optional
        Quadrant information for creating the cross-section.
        - YZ plane: 1 (+Y), 2 (-Y), 3 (+Z), 4 (-Z)
        - XZ plane: 1 (+X), 2 (-X), 3 (+Z), 4 (-Z)
        - XY plane: 1 (+X), 2 (-X), 3 (+Y), 4 (-Y)
        Defaults to 3.

    Raises
    ------
    ValueError
        If any of the input parameters are invalid.

    Examples
    --------
    >>> # Create a default cross-section
    >>> cad_create_cross_section()

    >>> # Create a cross-section on the YZ plane with a specific offset
    >>> cad_create_cross_section(plane='YZ', offset=5.0, quadrant=1)
    """
    
    # Type checks and validations
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("Frame should be an integer greater than 0.")
    
    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"Invalid plane value. Allowed values: {VALID_PLANE_LIST}.")
    
    if not isinstance(offset, (int, float)):
        raise ValueError("Offset should be a numeric value.")
    
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("Body index should be an integer greater than 0.")
    
    if quadrant not in VALID_QUADRANT_LIST:
        raise ValueError(f"Quadrant should be one of the following integer values: {VALID_QUADRANT_LIST}.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a cross-sections from an existing mesh body **********",
        "#************************************************************************",
        f"CAD_CREATE_CROSS_SECTION {frame} {plane} {offset} {body_index} {quadrant}"
    ]

    script.append_lines(lines)
    return

def cad_create_point_curve(x: float = 0.0, y: float = 1.0, z: float = 0.0) -> None:
    """
    Create a singular point curve in 3D space.

    This function appends a command to the script state to create a single
    point curve at the specified 3D coordinates.

    Parameters
    ----------
    x : float, optional
        The X-coordinate of the point curve. Defaults to 0.0.
    y : float, optional
        The Y-coordinate of the point curve. Defaults to 1.0.
    z : float, optional
        The Z-coordinate of the point curve. Defaults to 0.0.

    Raises
    ------
    ValueError
        If any of the coordinates are not numeric values.

    Examples
    --------
    >>> # Create a point curve at the default coordinates
    >>> cad_create_point_curve()

    >>> # Create a point curve at a custom location
    >>> cad_create_point_curve(x=10.5, y=-5.2, z=2.0)
    """
    
    # Type checks and validations
    if not all(isinstance(coord, (int, float)) for coord in [x, y, z]):
        raise ValueError("All coordinates (x, y, z) must be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a singular point curve (3D) **************************",
        "#************************************************************************",
        f"CAD_CREATE_CURVE_POINT {x} {y} {z}"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_arc(
    x0: float = 0.0, y0: float = 0.0, z0: float = 0.0,
    x1: float = -1.0, y1: float = 0.0, z1: float = 0.0,
    x2: float = 0.0, y2: float = 1.0, z2: float = 0.0
) -> None:
    """
    Create a circular arc curve in 3D space.

    This function appends a command to the script state to create a circular
    arc curve defined by an origin, a first vertex, and a second vertex.

    Parameters
    ----------
    x0, y0, z0 : float, optional
        Coordinates of the origin of the circular arc.
        Defaults to (0.0, 0.0, 0.0).
    x1, y1, z1 : float, optional
        Coordinates of the first vertex of the circular arc.
        Defaults to (-1.0, 0.0, 0.0).
    x2, y2, z2 : float, optional
        Coordinates of the second vertex of the circular arc.
        Defaults to (0.0, 1.0, 0.0).

    Raises
    ------
    ValueError
        If any of the coordinates are not numeric values.

    Examples
    --------
    >>> # Create a default circular arc
    >>> cad_create_curve_arc()

    >>> # Create a custom circular arc
    >>> cad_create_curve_arc(
    ...     x0=1, y0=1, z0=0,
    ...     x1=2, y1=1, z1=0,
    ...     x2=1, y2=2, z2=0
    ... )
    """
    
    # Type checks and validations
    coords = [x0, y0, z0, x1, y1, z1, x2, y2, z2]
    if not all(isinstance(coord, (int, float)) for coord in coords):
        raise ValueError("All provided coordinates should be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a circular arc curve (3D) ****************************",
        "#************************************************************************",
        f"CAD_CREATE_CURVE_ARC {x0} {y0} {z0} {x1} {y1} {z1} {x2} {y2} {z2}"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_select(curve_index: int = 1) -> None:
    """
    Select a CAD->Create drawing curve.

    This function appends a command to the script state to select one or all
    of the CAD->Create drawing curves.

    Parameters
    ----------
    curve_index : int, optional
        The index of the drawing curve to be selected. A value of -1 selects
        all curves. Must be a non-zero integer. Defaults to 1.

    Raises
    ------
    ValueError
        If `curve_index` is 0.

    Examples
    --------
    >>> # Select curve with index 2
    >>> cad_create_curve_select(curve_index=2)

    >>> # Select all curves
    >>> cad_create_curve_select(curve_index=-1)
    """
    
    # Type and value checking
    if not isinstance(curve_index, int) or curve_index == 0:
        raise ValueError("`curve_index` should be a non-zero integer value.")
    
    lines = [
        "#************************************************************************",
        "#********** Select one of the CAD-->Create drawing curves ***************",
        "#************************************************************************",
        f"CAD_CREATE_CURVE_SELECT {curve_index}"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_unselect(curve_index: int = 1) -> None:
    """
    Unselect a CAD->Create drawing curve.

    This function appends a command to the script state to unselect one or
    all of the CAD->Create drawing curves.

    Parameters
    ----------
    curve_index : int, optional
        The index of the drawing curve to be unselected. A value of -1
        unselects all curves. Must be a non-zero integer. Defaults to 1.

    Raises
    ------
    ValueError
        If `curve_index` is 0.

    Examples
    --------
    >>> # Unselect curve with index 1
    >>> cad_create_curve_unselect(curve_index=1)

    >>> # Unselect all curves
    >>> cad_create_curve_unselect(curve_index=-1)
    """
    
    # Type and value checking
    if not isinstance(curve_index, int) or curve_index == 0:
        raise ValueError("`curve_index` should be a non-zero integer value.")
    
    lines = [
        "#************************************************************************",
        "#********** Unselect specific CAD-->Create drawing curves by index ******",
        "#************************************************************************",
        f"CAD_CREATE_CURVE_UNSELECT {curve_index}"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_reverse(curve_index: int = 1) -> None:
    """
    Reverse a CAD->Create drawing curve.

    This function appends a command to the script state to reverse the
    direction of a specified CAD->Create drawing curve.

    Parameters
    ----------
    curve_index : int, optional
        The index of the drawing curve to be reversed. A value of -1 reverses
        all curves. Defaults to 1.

    Raises
    ------
    ValueError
        If `curve_index` is not an integer.

    Examples
    --------
    >>> # Reverse curve with index 2
    >>> cad_create_curve_reverse(curve_index=2)

    >>> # Reverse all curves
    >>> cad_create_curve_reverse(curve_index=-1)
    """

    # Type and value checking
    if not isinstance(curve_index, int):
        raise ValueError("`curve_index` should be an integer value.")

    lines = [
        "#************************************************************************",
        f"#********** Reverse {'ALL' if curve_index == -1 else 'specific'} CAD-->Create drawing curves{' by index' if curve_index != -1 else ''} *******",
        "#************************************************************************",
        f"CAD_CREATE_CURVE_REVERSE {curve_index}"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_delete_all() -> None:
    """
    Delete all CAD->Create drawing curves.

    This function appends a command to the script state to delete all
    existing CAD->Create drawing curves.

    Examples
    --------
    >>> # Delete all drawing curves
    >>> cad_create_curve_delete_all()
    """

    lines = [
        "#************************************************************************",
        "#********** Delete ALL of the CAD-->Create drawing curves ***************",
        "#************************************************************************",
        "CAD_CREATE_CURVE_DELETE_ALL"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_delete_selected() -> None:
    """
    Delete selected CAD->Create drawing curves.

    This function appends a command to the script state to delete only the
    selected CAD->Create drawing curves.

    Examples
    --------
    >>> # Delete all selected drawing curves
    >>> cad_create_curve_delete_selected()
    """
    
    lines = [
        "#************************************************************************",
        "#********** Delete only selected CAD-->Create drawing curves ************",
        "#************************************************************************",
        "CAD_CREATE_CURVE_DELETE_SELECTED"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_delete_unselected() -> None:
    """
    Delete unselected CAD->Create drawing curves.

    This function appends a command to the script state to delete only the
    unselected CAD->Create drawing curves.

    Examples
    --------
    >>> # Delete all unselected drawing curves
    >>> cad_create_curve_delete_unselected()
    """
    
    lines = [
        "#************************************************************************",
        "#********** Delete only unselected CAD-->Create drawing curves **********",
        "#************************************************************************",
        "CAD_CREATE_CURVE_DELETE_UNSELECTED"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_export_ccs(file_path: str) -> None:
    """
    Export selected CAD->Create drawing curves to a CCS file.

    This function appends a command to the script state to export the
    selected CAD->Create drawing curves to a specified CCS file.

    Parameters
    ----------
    file_path : str
        The absolute path to the output CCS file.

    Raises
    ------
    ValueError
        If `file_path` is not a string.

    Examples
    --------
    >>> # Export selected curves to a file
    >>> cad_create_curve_export_ccs(file_path='C:/path/to/exported_curves.ccs')
    """
    
    # Type and value checking
    if not isinstance(file_path, str):
        raise ValueError("`file_path` should be a string value.")
    
    lines = [
        "#************************************************************************",
        "#********* Export selected CAD-->Create drawing curves to CSV file ******",
        "#************************************************************************",
        "CAD_CREATE_CURVE_EXPORT_CCS",
        f"{file_path}"
    ]

    script.append_lines(lines)
    return

def cad_import_cad(
    cad_filepath: str,
    tessellation_density: str = 'MEDIUM',
    unreferenced_patches: bool = True,
    num_curvature: int = 80
) -> None:
    """
    Import a CAD geometry into the simulation.

    This function appends a command to the script state to import a CAD
    geometry from a specified file path, with tessellation density,
    unreferenced patch import, and curvature refinement controls.

    Parameters
    ----------
    cad_filepath : str
        The absolute path to the CAD file.
    tessellation_density : str, optional
        Density of tessellation used for CAD faces ('LOW', 'MEDIUM', 'HIGH').
        Defaults to 'MEDIUM'.
    unreferenced_patches : bool, optional
        Whether to import unreferenced patches. Defaults to True.
    num_curvature : int, optional
        Curvature refinement as subdivisions around a circle (> 0).
        Defaults to 80.

    Raises
    ------
    FileNotFoundError
        If `cad_filepath` does not exist.
    ValueError
        If `tessellation_density` is invalid, `unreferenced_patches` is not
        a boolean, or `num_curvature` is not a positive integer.

    Examples
    --------
    >>> # Import a CAD file using default import settings
    >>> cad_import_cad(cad_filepath='C:/path/to/geometry.igs')

    >>> # Import a CAD file with custom tessellation and curvature settings
    >>> cad_import_cad(
    ...     cad_filepath='C:/path/to/geometry.step',
    ...     tessellation_density='HIGH',
    ...     unreferenced_patches=False,
    ...     num_curvature=120
    ... )
    """
    check_file_existence(cad_filepath)

    valid_tessellation_densities = ['LOW', 'MEDIUM', 'HIGH']
    tessellation_density = normalize_option(tessellation_density, "tessellation_density")
    if tessellation_density not in valid_tessellation_densities:
        raise ValueError(
            f"`tessellation_density` should be one of {valid_tessellation_densities}. "
            f"Received: {tessellation_density}"
        )

    if not isinstance(unreferenced_patches, bool):
        raise ValueError("`unreferenced_patches` should be a boolean value (True or False).")

    if not isinstance(num_curvature, int) or num_curvature <= 0:
        raise ValueError("`num_curvature` should be an integer value greater than zero.")

    unreferenced_patches_token = 'TRUE' if unreferenced_patches else 'FALSE'

    lines = [
        "#************************************************************************",
        "#******************* Import a geometry into the simulation **************",
        "#************************************************************************",
        f"IMPORT_CAD {tessellation_density} {unreferenced_patches_token} {num_curvature}",
        cad_filepath
    ]

    script.append_lines(lines)
    return

def convert_cad_to_mesh(model_index: int) -> None:
    """
    Transfer a CAD model mesh to the Mesh node of the simulation.

    This function appends a command to the script state to transfer the mesh
    of a specified CAD model to the Mesh node of the simulation.

    Parameters
    ----------
    model_index : int
        The index of the CAD model to be transferred. Must be a positive
        integer.

    Raises
    ------
    ValueError
        If `model_index` is not a positive integer.

    Examples
    --------
    >>> # Convert CAD model with index 1 to a mesh
    >>> convert_cad_to_mesh(model_index=1)
    """
    
    # Type and value checking
    if not isinstance(model_index, int) or model_index <= 0:
        raise ValueError("`model_index` should be a positive integer value.")
    
    lines = [
        "#************************************************************************",
        "#****** Transfer CAD model mesh to the Mesh node of the simulation ******",
        "#************************************************************************",
        f"CONVERT_CAD_TO_MESH {model_index}"
    ]
    
    script.append_lines(lines)
    return


def cad_create_auto_annular_cross_sections(
    frame: int = 1,
    sections: int = 20,
    body_index: int = 1
) -> None:
    """
    Create a series of automatic annular cross-sections.

    This function appends a command to the script state to create a series
    of automatic annular cross-sections from a specified mesh body.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system to be used. Defaults to 1.
    sections : int, optional
        Number of cross-sections to create (> 1). Defaults to 20.
    body_index : int, optional
        Index of the mesh body to use for creating cross-sections.
        Defaults to 1.

    Raises
    ------
    ValueError
        If `frame`, `sections`, or `body_index` are not valid integers.

    Examples
    --------
    >>> # Create default annular cross-sections
    >>> cad_create_auto_annular_cross_sections()

    >>> # Create 30 annular cross-sections for body index 2
    >>> cad_create_auto_annular_cross_sections(sections=30, body_index=2)
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer greater than 0.")
    
    if not isinstance(sections, int) or sections <= 1:
        raise ValueError("`sections` should be an integer greater than 1.")
    
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("`body_index` should be an integer greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****** Create a series of automatic annular cross-sections *************",
        "#************************************************************************",
        f"CAD_CREATE_AUTO_ANNULAR_CROSS_SECTIONS {frame} {sections} {body_index}"
    ]
    
    script.append_lines(lines)
    return


def body_rotate(
    body_index: int = 1,
    axis: ValidAxis = 'X',
    angle: float = 0.0
) -> None:
    """
    Rotate a CAD body about an axis of the reference coordinate system.

    This function appends a command to the script state to rotate a specified
    CAD body by a given angle about an axis of the reference frame.

    Parameters
    ----------
    body_index : int, optional
        Index of the CAD body to rotate (> 0). Defaults to 1.
    axis : ValidAxis, optional
        Rotation axis ('X', 'Y', or 'Z'). Defaults to 'X'.
    angle : float, optional
        Rotation angle in degrees. Defaults to 0.0.

    Raises
    ------
    ValueError
        If `body_index` is not a positive integer, `axis` is invalid,
        or `angle` is not numeric.

    Examples
    --------
    >>> body_rotate(body_index=1, axis='Z', angle=90.0)
    """
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("`body_index` should be an integer value greater than zero.")

    axis = normalize_option(axis, "axis")
    if axis not in VALID_AXIS_LIST:
        raise ValueError(f"`axis` should be one of {VALID_AXIS_LIST}. Received: {axis}")

    if not isinstance(angle, (int, float)):
        raise ValueError("`angle` should be a numeric value.")

    lines = [
        "#************************************************************************",
        "#*********************** Rotate selected CAD body ************************",
        "#************************************************************************",
        f"CAD_BODY_ROTATE {body_index} {axis} {angle}"
    ]

    script.append_lines(lines)
    return


def body_translate(
    body_index: int = 1,
    x: float = 0.0,
    y: float = 0.0,
    z: float = 0.0,
    units: ValidUnits = 'METER'
) -> None:
    """
    Translate a CAD body by a specified vector.

    This function appends a command to the script state to translate a
    specified CAD body by a given vector in the reference coordinate system.

    Parameters
    ----------
    body_index : int, optional
        Index of the CAD body to translate (> 0). Defaults to 1.
    x : float, optional
        Translation vector X component. Defaults to 0.0.
    y : float, optional
        Translation vector Y component. Defaults to 0.0.
    z : float, optional
        Translation vector Z component. Defaults to 0.0.
    units : ValidUnits, optional
        Length units for the translation vector. Defaults to 'METER'.

    Raises
    ------
    ValueError
        If `body_index` is not a positive integer, any coordinate is not
        numeric, or `units` is invalid.

    Examples
    --------
    >>> body_translate(body_index=1, x=1.0)
    """
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("`body_index` should be an integer value greater than zero.")

    for value, label in [(x, 'x'), (y, 'y'), (z, 'z')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    units = check_valid_length_units(units)

    lines = [
        "#************************************************************************",
        "#********************* Translate selected CAD body ***********************",
        "#************************************************************************",
        f"CAD_BODY_TRANSLATE {body_index} {x} {y} {z} {units}"
    ]

    script.append_lines(lines)
    return


def body_scale(
    body_index: int = 1,
    scale: float = 1.0
) -> None:
    """
    Scale a CAD body uniformly.

    This function appends a command to the script state to scale a specified
    CAD body by a uniform scaling factor.

    Parameters
    ----------
    body_index : int, optional
        Index of the CAD body to scale (> 0). Defaults to 1.
    scale : float, optional
        Uniform scaling factor (> 0). Defaults to 1.0.

    Raises
    ------
    ValueError
        If `body_index` is not a positive integer or `scale` is not
        a positive numeric value.

    Examples
    --------
    >>> body_scale(body_index=1, scale=2.0)
    """
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("`body_index` should be an integer value greater than zero.")

    if not isinstance(scale, (int, float)) or scale <= 0:
        raise ValueError("`scale` should be a numeric value greater than zero.")

    lines = [
        "#************************************************************************",
        "#************************ Scale selected CAD body ************************",
        "#************************************************************************",
        f"CAD_BODY_SCALE {body_index} {scale}"
    ]

    script.append_lines(lines)
    return


def body_mirror(
    body_index: int = 1,
    plane: ValidPlanes = 'XZ'
) -> None:
    """
    Mirror a CAD body about a plane of the reference coordinate system.

    This function appends a command to the script state to mirror a specified
    CAD body about a plane of the reference coordinate system.

    Parameters
    ----------
    body_index : int, optional
        Index of the CAD body to mirror (> 0). Defaults to 1.
    plane : ValidPlanes, optional
        Mirror plane ('XY', 'XZ', or 'YZ'). Defaults to 'XZ'.

    Raises
    ------
    ValueError
        If `body_index` is not a positive integer or `plane` is invalid.

    Examples
    --------
    >>> body_mirror(body_index=1, plane='XZ')
    """
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("`body_index` should be an integer value greater than zero.")

    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}. Received: {plane}")

    lines = [
        "#************************************************************************",
        "#*********************** Mirror selected CAD body ************************",
        "#************************************************************************",
        f"CAD_BODY_MIRROR {body_index} {plane}"
    ]

    script.append_lines(lines)
    return


def body_delete(
    body_index: int = -1
) -> None:
    """
    Delete a CAD body from the simulation.

    This function appends a command to the script state to delete a specified
    CAD body, or all CAD bodies if `body_index` is -1.

    Parameters
    ----------
    body_index : int, optional
        Index of the CAD body to delete (> 0), or -1 to delete all bodies.
        Defaults to -1.

    Raises
    ------
    ValueError
        If `body_index` is not a positive integer or -1.

    Examples
    --------
    >>> # Delete all CAD bodies
    >>> body_delete()

    >>> # Delete CAD body 2
    >>> body_delete(body_index=2)
    """
    if not isinstance(body_index, int):
        raise ValueError("`body_index` should be an integer value.")
    if body_index == 0 or body_index < -1:
        raise ValueError("`body_index` should be -1 (all) or a positive integer value.")

    lines = [
        "#************************************************************************",
        "#*********************** Delete selected CAD body ************************",
        "#************************************************************************",
        f"CAD_BODY_DELETE {body_index}"
    ]

    script.append_lines(lines)
    return


def body_select_by_threshold(
    frame: int = 1,
    parameter: ValidAxis = 'Y',
    value: float = 0.0,
    logic: str = 'BELOW',
    action: str = 'SELECT'
) -> None:
    """
    Select or delete CAD body faces by a geometric threshold criterion.

    This function appends a command to the script state to select or delete
    CAD faces in a body that satisfy a threshold along a coordinate axis.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    parameter : ValidAxis, optional
        Threshold coordinate axis ('X', 'Y', or 'Z'). Defaults to 'Y'.
    value : float, optional
        Threshold value along the specified axis. Defaults to 0.0.
    logic : str, optional
        Threshold comparison logic ('ABOVE' or 'BELOW'). Defaults to 'BELOW'.
    action : str, optional
        Action to perform on matching faces ('SELECT' or 'DELETE').
        Defaults to 'SELECT'.

    Raises
    ------
    ValueError
        If any parameter fails validation.

    Examples
    --------
    >>> body_select_by_threshold(parameter='Y', value=0.0, logic='BELOW', action='DELETE')
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    parameter = normalize_option(parameter, "parameter")
    if parameter not in VALID_AXIS_LIST:
        raise ValueError(f"`parameter` should be one of {VALID_AXIS_LIST}. Received: {parameter}")

    if not isinstance(value, (int, float)):
        raise ValueError("`value` should be a numeric value.")

    valid_logic = ['ABOVE', 'BELOW']
    logic = normalize_option(logic, "logic")
    if logic not in valid_logic:
        raise ValueError(f"`logic` should be one of {valid_logic}. Received: {logic}")

    valid_actions = ['SELECT', 'DELETE']
    action = normalize_option(action, "action")
    if action not in valid_actions:
        raise ValueError(f"`action` should be one of {valid_actions}. Received: {action}")

    lines = [
        "#************************************************************************",
        "#***************** Select CAD body by threshold criterion ****************",
        "#************************************************************************",
        f"CAD_BODY_SELECT_BY_THRESHOLD {frame} {parameter} {value} {logic} {action}"
    ]

    script.append_lines(lines)
    return


def set_cad_create_merge_tolerance(
    tolerance: float = 1.0
) -> None:
    """
    Set the merge tolerance for CAD geometry creation.

    This function appends a command to the script state to set the merge
    tolerance used during CAD geometry creation, expressed as a percentage
    of the reference curve length.

    Parameters
    ----------
    tolerance : float, optional
        Merge tolerance as a percentage of curve length (> 0). Defaults to 1.0.

    Raises
    ------
    ValueError
        If `tolerance` is not a positive numeric value.

    Examples
    --------
    >>> set_cad_create_merge_tolerance(tolerance=0.5)
    """
    if not isinstance(tolerance, (int, float)) or tolerance <= 0:
        raise ValueError("`tolerance` should be a numeric value greater than zero.")

    lines = [
        "#************************************************************************",
        "#******************* Set CAD create merge tolerance **********************",
        "#************************************************************************",
        f"SET_CAD_CREATE_MERGE_TOLERANCE {tolerance}"
    ]

    script.append_lines(lines)
    return


def set_cad_create_spline_segments(
    num_pts: int = 200
) -> None:
    """
    Set the number of spline nodes used in CAD geometry creation.

    This function appends a command to the script state to set the number
    of spline nodes or segments used during CAD geometry creation.

    Parameters
    ----------
    num_pts : int, optional
        Number of spline nodes/segments (> 10). Defaults to 200.

    Raises
    ------
    ValueError
        If `num_pts` is not an integer greater than 10.

    Examples
    --------
    >>> set_cad_create_spline_segments(num_pts=400)
    """
    if not isinstance(num_pts, int) or num_pts <= 10:
        raise ValueError("`num_pts` should be an integer value greater than 10.")

    lines = [
        "#************************************************************************",
        "#******************* Set CAD create spline segments **********************",
        "#************************************************************************",
        f"SET_CAD_CREATE_SPLINE_SEGMENTS {num_pts}"
    ]

    script.append_lines(lines)
    return


def set_cad_create_spline_loft(
    loft_type: str = 'C2'
) -> None:
    """
    Set the spline loft type for CAD geometry creation.

    This function appends a command to the script state to set the spline
    loft continuity type used during CAD geometry creation.

    Parameters
    ----------
    loft_type : str, optional
        Spline loft continuity type ('C2' or 'C0'). Defaults to 'C2'.

    Raises
    ------
    ValueError
        If `loft_type` is not 'C2' or 'C0'.

    Examples
    --------
    >>> set_cad_create_spline_loft(loft_type='C0')
    """
    valid_loft_types = ['C2', 'C0']
    loft_type = normalize_option(loft_type, "loft_type")
    if loft_type not in valid_loft_types:
        raise ValueError(f"`loft_type` should be one of {valid_loft_types}. Received: {loft_type}")

    lines = [
        "#************************************************************************",
        "#********************* Set CAD create spline loft ************************",
        "#************************************************************************",
        f"SET_CAD_CREATE_SPLINE_LOFT {loft_type}"
    ]

    script.append_lines(lines)
    return


def set_cad_curvature_refinement(
    num_pts_per_circle: int = 80
) -> None:
    """
    Set the curvature refinement resolution for CAD geometry.

    This function appends a command to the script state to set the number
    of subdivisions around a full circle used for curvature-based
    CAD geometry refinement.

    Parameters
    ----------
    num_pts_per_circle : int, optional
        Number of subdivisions around a circle for curvature refinement (> 0).
        Defaults to 80.

    Raises
    ------
    ValueError
        If `num_pts_per_circle` is not a positive integer.

    Examples
    --------
    >>> set_cad_curvature_refinement(num_pts_per_circle=120)
    """
    if not isinstance(num_pts_per_circle, int) or num_pts_per_circle <= 0:
        raise ValueError("`num_pts_per_circle` should be an integer value greater than zero.")

    lines = [
        "#************************************************************************",
        "#********************* Set CAD curvature refinement **********************",
        "#************************************************************************",
        f"SET_CAD_CURVATURE_REFINEMENT {num_pts_per_circle}"
    ]

    script.append_lines(lines)
    return


def create_box(
    frame: int = 1,
    x: float = 0.0,
    y: float = 0.0,
    z: float = 0.0,
    len_x: float = 1.0,
    len_y: float = 1.0,
    len_z: float = 1.0
) -> None:
    """
    Create a CAD box geometry.

    This function appends a command to the script state to create a rectangular
    box CAD body defined by an origin corner vertex and edge lengths.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    x : float, optional
        X coordinate of the first corner vertex. Defaults to 0.0.
    y : float, optional
        Y coordinate of the first corner vertex. Defaults to 0.0.
    z : float, optional
        Z coordinate of the first corner vertex. Defaults to 0.0.
    len_x : float, optional
        Box edge length along the X axis. Defaults to 1.0.
    len_y : float, optional
        Box edge length along the Y axis. Defaults to 1.0.
    len_z : float, optional
        Box edge length along the Z axis. Defaults to 1.0.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer or any coordinate/length
        is not numeric.

    Examples
    --------
    >>> # Create a unit box at the origin
    >>> create_box()

    >>> # Create a 2×1×0.5 box offset in Y
    >>> create_box(x=0.0, y=1.0, z=0.0, len_x=2.0, len_y=1.0, len_z=0.5)
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    for value, label in [(x, 'x'), (y, 'y'), (z, 'z'), (len_x, 'len_x'), (len_y, 'len_y'), (len_z, 'len_z')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    lines = [
        "#************************************************************************",
        "#************************** Create CAD box *******************************",
        "#************************************************************************",
        f"CAD_CREATE_BOX {frame} {x} {y} {z} {len_x} {len_y} {len_z}"
    ]

    script.append_lines(lines)
    return


def create_sphere(
    frame: int = 1,
    x: float = 0.0,
    y: float = 0.0,
    z: float = 0.0,
    radius: float = 1.0
) -> None:
    """
    Create a CAD sphere geometry.

    This function appends a command to the script state to create a spherical
    CAD body defined by an origin and radius.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    x : float, optional
        X coordinate of the sphere center. Defaults to 0.0.
    y : float, optional
        Y coordinate of the sphere center. Defaults to 0.0.
    z : float, optional
        Z coordinate of the sphere center. Defaults to 0.0.
    radius : float, optional
        Sphere radius (> 0). Defaults to 1.0.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer, any coordinate is not numeric,
        or `radius` is not a positive numeric value.

    Examples
    --------
    >>> # Create a unit sphere at the origin
    >>> create_sphere()

    >>> # Create a sphere of radius 2 centered at (1, 2, 3)
    >>> create_sphere(x=1.0, y=2.0, z=3.0, radius=2.0)
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    for value, label in [(x, 'x'), (y, 'y'), (z, 'z')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("`radius` should be a numeric value greater than zero.")

    lines = [
        "#************************************************************************",
        "#************************ Create CAD sphere ******************************",
        "#************************************************************************",
        f"CAD_CREATE_SPHERE {frame} {x} {y} {z} {radius}"
    ]

    script.append_lines(lines)
    return


def create_cylinder(
    frame: int = 1,
    x: float = 0.0,
    y: float = 0.0,
    z: float = 0.0,
    r1: float = 1.0,
    r2: float = 1.0,
    length: float = 1.0
) -> None:
    """
    Create a CAD cylinder or truncated cone geometry.

    This function appends a command to the script state to create a cylindrical
    or conical CAD body defined by an origin, radii at each end, and a length.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    x : float, optional
        X coordinate of the cylinder origin. Defaults to 0.0.
    y : float, optional
        Y coordinate of the cylinder origin. Defaults to 0.0.
    z : float, optional
        Z coordinate of the cylinder origin. Defaults to 0.0.
    r1 : float, optional
        Radius at the beginning of the cylinder axis (> 0). Defaults to 1.0.
    r2 : float, optional
        Radius at the end of the cylinder axis (> 0). Defaults to 1.0.
    length : float, optional
        Cylinder length along its axis (> 0). Defaults to 1.0.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer, any coordinate is not numeric,
        or `r1`, `r2`, or `length` are not positive numeric values.

    Examples
    --------
    >>> # Create a unit cylinder at the origin
    >>> create_cylinder()

    >>> # Create a tapered cone of length 5
    >>> create_cylinder(r1=1.0, r2=0.5, length=5.0)
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    for value, label in [(x, 'x'), (y, 'y'), (z, 'z'), (r1, 'r1'), (r2, 'r2'), (length, 'length')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    if r1 <= 0 or r2 <= 0 or length <= 0:
        raise ValueError("`r1`, `r2`, and `length` should be greater than zero.")

    lines = [
        "#************************************************************************",
        "#************************ Create CAD cylinder ****************************",
        "#************************************************************************",
        f"CAD_CREATE_CYLINDER {frame} {x} {y} {z} {r1} {r2} {length}"
    ]

    script.append_lines(lines)
    return


def create_sheet(
    frame: int = 1,
    plane: ValidPlanes = 'XZ',
    offset: float = 0.0,
    len1: float = 1.0,
    len2: float = 1.0
) -> None:
    """
    Create a planar sheet CAD geometry.

    This function appends a command to the script state to create a flat
    rectangular sheet CAD body in a specified coordinate plane.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    plane : ValidPlanes, optional
        Coordinate plane for the sheet ('XY', 'XZ', or 'YZ'). Defaults to 'XZ'.
    offset : float, optional
        Offset of the sheet along the plane normal direction. Defaults to 0.0.
    len1 : float, optional
        Sheet length in the first direction of the plane. Defaults to 1.0.
    len2 : float, optional
        Sheet length in the second direction of the plane. Defaults to 1.0.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer, `plane` is invalid,
        or any length/offset is not numeric.

    Examples
    --------
    >>> # Create a unit sheet in the XZ plane
    >>> create_sheet()

    >>> # Create a 4×2 sheet in the XY plane at offset 1.0
    >>> create_sheet(plane='XY', offset=1.0, len1=4.0, len2=2.0)
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}. Received: {plane}")

    for value, label in [(offset, 'offset'), (len1, 'len1'), (len2, 'len2')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    lines = [
        "#************************************************************************",
        "#************************* Create CAD sheet ******************************",
        "#************************************************************************",
        f"CAD_CREATE_SHEET {frame} {plane} {offset} {len1} {len2}"
    ]

    script.append_lines(lines)
    return


def create_import_curve_p3d(
    p3d_filepath: str,
    units: ValidUnits = 'METER',
    swap_direction: str = 'FALSE',
    frame: int = 1,
    component_index: int = -1
) -> None:
    """
    Import drawing curves from a P3D file.

    This function appends a command to the script state to import drawing
    curves from a Plot3D (.p3d) file into the CAD create pane.

    Parameters
    ----------
    p3d_filepath : str
        Path to the P3D curve file.
    units : ValidUnits, optional
        Length unit type for the imported curves. Defaults to 'METER'.
    swap_direction : str, optional
        Direction swap flag for curve orientation ('TRUE' or 'FALSE').
        Defaults to 'FALSE'.
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    component_index : int, optional
        Component index to import (> 0), or -1 to import all components.
        Defaults to -1.

    Raises
    ------
    FileNotFoundError
        If `p3d_filepath` does not exist.
    ValueError
        If `units`, `swap_direction`, `frame`, or `component_index` are invalid.

    Examples
    --------
    >>> create_import_curve_p3d('path/to/curves.p3d')

    >>> create_import_curve_p3d('curves.p3d', units='INCH', swap_direction='TRUE', component_index=2)
    """
    check_file_existence(p3d_filepath)

    units = check_valid_length_units(units)

    valid_swap = ['TRUE', 'FALSE']
    swap_direction = normalize_option(swap_direction, "swap_direction")
    if swap_direction not in valid_swap:
        raise ValueError(f"`swap_direction` should be one of {valid_swap}. Received: {swap_direction}")

    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    if not isinstance(component_index, int) or component_index == 0 or component_index < -1:
        raise ValueError("`component_index` should be -1 (all) or a positive integer value.")

    lines = [
        "#************************************************************************",
        "#***************** Import CAD create curve from P3D file ****************",
        "#************************************************************************",
        f"CAD_CREATE_IMPORT_CURVE_P3D {units} {swap_direction} {frame} {component_index}",
        p3d_filepath
    ]

    script.append_lines(lines)
    return


def create_self_median_from_curves() -> None:
    """
    Create a self-median surface from selected curves.

    This function appends a command to the script state to create a self-median
    surface from the currently selected drawing curves in the CAD create pane.

    Examples
    --------
    >>> create_self_median_from_curves()
    """

    lines = [
        "#************************************************************************",
        "#**************** Create self median from selected curves ****************",
        "#************************************************************************",
        "CAD_CREATE_SELF_MEDIAN_FROM_CURVES"
    ]

    script.append_lines(lines)
    return


def create_connect_curves() -> None:
    """
    Connect selected drawing curves into a single curve.

    This function appends a command to the script state to connect the
    currently selected drawing curves in the CAD create pane.

    Examples
    --------
    >>> create_connect_curves()
    """

    lines = [
        "#************************************************************************",
        "#*********************** Connect selected curves *************************",
        "#************************************************************************",
        "CAD_CREATE_CONNECT_CURVES"
    ]

    script.append_lines(lines)
    return


def create_rotate_curves(
    frame: int = 1,
    axis: ValidRotationAxis = 'X',
    angle: float = 0.0,
    retain_curve: str = 'DELETE'
) -> None:
    """
    Rotate selected drawing curves about a coordinate axis.

    This function appends a command to the script state to rotate the
    currently selected drawing curves by a given angle, with an option
    to retain or delete the source curves.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    axis : ValidRotationAxis, optional
        Rotation axis ('X', 'Y', 'Z', '1', '2', or '3'). Defaults to 'X'.
    angle : float, optional
        Rotation angle in degrees. Defaults to 0.0.
    retain_curve : str, optional
        Whether to retain or delete the source curves after the operation
        ('RETAIN' or 'DELETE'). Defaults to 'DELETE'.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer, `axis` is invalid, `angle`
        is not numeric, or `retain_curve` is invalid.

    Examples
    --------
    >>> create_rotate_curves(axis='Z', angle=45.0)
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    axis = normalize_option(axis, "axis")
    if axis not in VALID_ROTATION_AXIS_LIST:
        raise ValueError(f"`axis` should be one of {VALID_ROTATION_AXIS_LIST}. Received: {axis}")

    if not isinstance(angle, (int, float)):
        raise ValueError("`angle` should be a numeric value.")

    valid_retain_curve = ['RETAIN', 'DELETE']
    retain_curve = normalize_option(retain_curve, "retain_curve")
    if retain_curve not in valid_retain_curve:
        raise ValueError(f"`retain_curve` should be one of {valid_retain_curve}. Received: {retain_curve}")

    lines = [
        "#************************************************************************",
        "#*********************** Rotate selected curves **************************",
        "#************************************************************************",
        f"CAD_CREATE_ROTATE_CURVES {frame} {axis} {angle} {retain_curve}"
    ]

    script.append_lines(lines)
    return


def create_translate_curves(
    x: float = 0.0,
    y: float = 0.0,
    z: float = 0.0,
    retain_curve: str = 'DELETE'
) -> None:
    """
    Translate selected drawing curves by a vector.

    This function appends a command to the script state to translate the
    currently selected drawing curves by a specified translation vector,
    with an option to retain or delete the source curves.

    Parameters
    ----------
    x : float, optional
        Translation vector X component. Defaults to 0.0.
    y : float, optional
        Translation vector Y component. Defaults to 0.0.
    z : float, optional
        Translation vector Z component. Defaults to 0.0.
    retain_curve : str, optional
        Whether to retain or delete the source curves after the operation
        ('RETAIN' or 'DELETE'). Defaults to 'DELETE'.

    Raises
    ------
    ValueError
        If any coordinate is not numeric or `retain_curve` is invalid.

    Examples
    --------
    >>> create_translate_curves(y=1.0)
    """
    for value, label in [(x, 'x'), (y, 'y'), (z, 'z')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    valid_retain_curve = ['RETAIN', 'DELETE']
    retain_curve = normalize_option(retain_curve, "retain_curve")
    if retain_curve not in valid_retain_curve:
        raise ValueError(f"`retain_curve` should be one of {valid_retain_curve}. Received: {retain_curve}")

    lines = [
        "#************************************************************************",
        "#********************* Translate selected curves *************************",
        "#************************************************************************",
        f"CAD_CREATE_TRANSLATE_CURVES {x} {y} {z} {retain_curve}"
    ]

    script.append_lines(lines)
    return


def create_scale_curves(
    scale: float = 1.0,
    retain_curve: str = 'DELETE'
) -> None:
    """
    Scale selected drawing curves by a uniform factor.

    This function appends a command to the script state to scale the
    currently selected drawing curves uniformly, with an option to retain
    or delete the source curves.

    Parameters
    ----------
    scale : float, optional
        Uniform scaling factor (> 0). Defaults to 1.0.
    retain_curve : str, optional
        Whether to retain or delete the source curves after the operation
        ('RETAIN' or 'DELETE'). Defaults to 'DELETE'.

    Raises
    ------
    ValueError
        If `scale` is not a positive numeric value or `retain_curve` is invalid.

    Examples
    --------
    >>> create_scale_curves(scale=2.0)
    """
    if not isinstance(scale, (int, float)) or scale <= 0:
        raise ValueError("`scale` should be a numeric value greater than zero.")

    valid_retain_curve = ['RETAIN', 'DELETE']
    retain_curve = normalize_option(retain_curve, "retain_curve")
    if retain_curve not in valid_retain_curve:
        raise ValueError(f"`retain_curve` should be one of {valid_retain_curve}. Received: {retain_curve}")

    lines = [
        "#************************************************************************",
        "#*********************** Scale selected curves ***************************",
        "#************************************************************************",
        f"CAD_CREATE_SCALE_CURVES {scale} {retain_curve}"
    ]

    script.append_lines(lines)
    return


def create_mirror_curves(
    frame: int = 1,
    plane: ValidPlanes = 'XZ',
    retain_curves: str = 'DELETE'
) -> None:
    """
    Mirror selected drawing curves about a coordinate plane.

    This function appends a command to the script state to mirror the
    currently selected drawing curves about a specified coordinate plane,
    with an option to retain or delete the source curves.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    plane : ValidPlanes, optional
        Mirror plane ('XY', 'XZ', or 'YZ'). Defaults to 'XZ'.
    retain_curves : str, optional
        Whether to retain or delete the source curves after the operation
        ('RETAIN' or 'DELETE'). Defaults to 'DELETE'.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer, `plane` is invalid,
        or `retain_curves` is invalid.

    Examples
    --------
    >>> # Mirror and delete originals (default)
    >>> create_mirror_curves()

    >>> # Mirror XY plane and retain originals
    >>> create_mirror_curves(plane='XY', retain_curves='RETAIN')
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}. Received: {plane}")

    valid_retain_curves = ['RETAIN', 'DELETE']
    retain_curves = normalize_option(retain_curves, "retain_curves")
    if retain_curves not in valid_retain_curves:
        raise ValueError(f"`retain_curves` should be one of {valid_retain_curves}. Received: {retain_curves}")

    lines = [
        "#************************************************************************",
        "#********************** Mirror selected curves ****************************",
        "#************************************************************************",
        f"CAD_CREATE_MIRROR_CURVES {frame} {plane} {retain_curves}"
    ]

    script.append_lines(lines)
    return


def create_project_curve(
    curve_index: int,
    frame: int = 1,
    plane: ValidPlanes = 'XZ',
    nx: float = 0.0,
    ny: float = 0.0,
    nz: float = 0.0,
    retain_curve: str = 'RETAIN'
) -> None:
    """
    Project a drawing curve onto a CAD surface.

    This function appends a command to the script state to project a specified
    drawing curve onto surfaces along a projection vector, with an option to
    retain or delete the source curve.

    Parameters
    ----------
    curve_index : int
        Index of the drawing curve to project (> 0), or -1 for all curves.
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    plane : ValidPlanes, optional
        Projection plane ('XY', 'XZ', or 'YZ'). Defaults to 'XZ'.
    nx : float, optional
        Projection vector X component. Defaults to 0.0.
    ny : float, optional
        Projection vector Y component. Defaults to 0.0.
    nz : float, optional
        Projection vector Z component. Defaults to 0.0.
    retain_curve : str, optional
        Whether to retain or delete the source curve after the operation
        ('RETAIN' or 'DELETE'). Defaults to 'RETAIN'.

    Raises
    ------
    ValueError
        If `curve_index` is invalid, `frame` is not a positive integer,
        `plane` is invalid, any projection vector component is not numeric,
        or `retain_curve` is invalid.

    Examples
    --------
    >>> create_project_curve(curve_index=1)
    """
    if not isinstance(curve_index, int) or curve_index == 0 or curve_index < -1:
        raise ValueError("`curve_index` should be -1 or a positive integer value.")

    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}. Received: {plane}")

    for value, label in [(nx, 'nx'), (ny, 'ny'), (nz, 'nz')]:
        if not isinstance(value, (int, float)):
            raise ValueError(f"`{label}` should be a numeric value.")

    valid_retain_curve = ['RETAIN', 'DELETE']
    retain_curve = normalize_option(retain_curve, "retain_curve")
    if retain_curve not in valid_retain_curve:
        raise ValueError(f"`retain_curve` should be one of {valid_retain_curve}. Received: {retain_curve}")

    lines = [
        "#************************************************************************",
        "#********************** Project selected curve ***************************",
        "#************************************************************************",
        f"CAD_CREATE_PROJECT_CURVE {curve_index} {frame} {plane} {nx} {ny} {nz} {retain_curve}"
    ]

    script.append_lines(lines)
    return


def create_project_multi_curve(
    curve_index_1: int,
    curve_index_2: int,
    frame: int = 1,
    plane: ValidPlanes = 'XZ',
    retain_curve: str = 'RETAIN'
) -> None:
    """
    Project multiple drawing curves onto a CAD surface.

    This function appends a command to the script state to project two drawing
    curves (a primary and a guide) onto surfaces, with an option to retain
    or delete the source curves.

    Parameters
    ----------
    curve_index_1 : int
        Index of the primary drawing curve to project (> 0).
    curve_index_2 : int
        Index of the guide drawing curve (> 0).
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    plane : ValidPlanes, optional
        Projection plane ('XY', 'XZ', or 'YZ'). Defaults to 'XZ'.
    retain_curve : str, optional
        Whether to retain or delete the source curves after the operation
        ('RETAIN' or 'DELETE'). Defaults to 'RETAIN'.

    Raises
    ------
    ValueError
        If either curve index is not a positive integer, `frame` is invalid,
        `plane` is invalid, or `retain_curve` is invalid.

    Examples
    --------
    >>> create_project_multi_curve(curve_index_1=1, curve_index_2=2)
    """
    for value, label in [(curve_index_1, 'curve_index_1'), (curve_index_2, 'curve_index_2')]:
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"`{label}` should be an integer value greater than zero.")

    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    plane = normalize_option(plane, "plane")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}. Received: {plane}")

    valid_retain_curve = ['RETAIN', 'DELETE']
    retain_curve = normalize_option(retain_curve, "retain_curve")
    if retain_curve not in valid_retain_curve:
        raise ValueError(f"`retain_curve` should be one of {valid_retain_curve}. Received: {retain_curve}")

    lines = [
        "#************************************************************************",
        "#******************* Project multiple selected curves ********************",
        "#************************************************************************",
        f"CAD_CREATE_PROJECT_MULTI_CURVE {curve_index_1} {curve_index_2} {frame} {plane} {retain_curve}"
    ]

    script.append_lines(lines)
    return


def create_reorder_curves(
    frame: int = 1,
    sorting_direction: str = '+Y'
) -> None:
    """
    Reorder selected drawing curves along a sorting direction.

    This function appends a command to the script state to reorder the
    currently selected drawing curves by sorting them along a specified
    coordinate direction.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system. Defaults to 1.
    sorting_direction : str, optional
        Sorting direction ('+X', '+Y', '+Z', '-X', '-Y', or '-Z').
        Defaults to '+Y'.

    Raises
    ------
    ValueError
        If `frame` is not a positive integer or `sorting_direction` is invalid.

    Examples
    --------
    >>> # Reorder curves along +Y (default)
    >>> create_reorder_curves()

    >>> # Reorder curves along -X
    >>> create_reorder_curves(sorting_direction='-X')
    """
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer value greater than zero.")

    valid_sorting_directions = ['+X', '+Y', '+Z', '-X', '-Y', '-Z']
    sorting_direction = normalize_option(sorting_direction, "sorting_direction")
    if sorting_direction not in valid_sorting_directions:
        raise ValueError(f"`sorting_direction` should be one of {valid_sorting_directions}. Received: {sorting_direction}")

    lines = [
        "#************************************************************************",
        "#********************** Reorder selected curves **************************",
        "#************************************************************************",
        f"CAD_CREATE_REORDER_CURVES {frame} {sorting_direction}"
    ]

    script.append_lines(lines)
    return
