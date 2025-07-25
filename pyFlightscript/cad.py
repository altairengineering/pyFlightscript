from .utils import *    
from .script import script
from .types import *
from .types import *
from typing import Union, Optional, Literal, List

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
        "#",
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

    if units not in VALID_UNITS_LIST:
        raise ValueError(f"Invalid units: {units}. Must be one of {VALID_UNITS_LIST}.")
    
    if dimension not in VALID_DIMENSIONS_LIST:
        raise ValueError(f"Invalid dimension: {dimension}. Must be one of {VALID_DIMENSIONS_LIST}.")
    
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"Invalid plane: {plane}. Must be one of {VALID_PLANE_LIST}.")

    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` must be a positive integer.")

    lines = [
        "#************************************************************************",
        "#*************** Import a CAD-->Create drawing curve from txt file ******",
        "#************************************************************************",
        "#",
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
        "#",
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
    symmetry: ValidSymmetryPlanes = 'NONE',
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
    symmetry : ValidSymmetryPlanes, optional
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
    
    if symmetry not in VALID_SYMMETRY_PLANE_LIST:
        raise ValueError(f"`symmetry` should be one of {VALID_SYMMETRY_PLANE_LIST}. Received: {symmetry}")
    
    if cad_mesh not in VALID_CAD_MESH_LIST:
        raise ValueError(f"`cad_mesh` should be one of {VALID_CAD_MESH_LIST}. Received: {cad_mesh}")
    
    lines = [
        "#************************************************************************",
        "#****** Create a series of automatic cross-sections from mesh body ******",
        "#************************************************************************",
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
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
        "#",
        "CAD_CREATE_CURVE_EXPORT_CCS",
        f"{file_path}"
    ]

    script.append_lines(lines)
    return

def cad_import_cad(cad_filepath: str) -> None:
    """
    Import a CAD geometry into the simulation.

    This function appends a command to the script state to import a CAD
    geometry from a specified file path.

    Parameters
    ----------
    cad_filepath : str
        The absolute path to the CAD file.

    Raises
    ------
    FileNotFoundError
        If `cad_filepath` does not exist.

    Examples
    --------
    >>> # Import a CAD file
    >>> cad_import_cad(cad_filepath='C:/path/to/geometry.igs')
    """
    check_file_existence(cad_filepath)

    lines = [
        "#************************************************************************",
        "#******************* Import a geometry into the simulation **************",
        "#************************************************************************",
        "#",
        "IMPORT_CAD",
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
        "#",
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
        "#",
        f"CAD_CREATE_AUTO_ANNULAR_CROSS_SECTIONS {frame} {sections} {body_index}"
    ]
    
    script.append_lines(lines)
    return
