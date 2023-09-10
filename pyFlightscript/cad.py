from .utils import *    
from .script_state import script

def cad_create_new_model(model_name):
    """
    Appends lines to script state to create a new CAD-->Model.
    

    :param model_name: Name of the new CAD model.
    """
    lines = [
        "#************************************************************************",
        "#****************** Create a new CAD-->Model ****************************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_NEW_MODEL {model_name}"
    ]

    script.append_lines(lines)
    return

def cad_create_initialize(model_index=1):
    """
    Appends lines to script state to initialize the CAD-->Create pane window.
    

    :param model_index: Input model_index for CAD_CREATE_INITIALIZE to which the CAD-->Create pane is linked.
    """
    lines = [
        "#************************************************************************",
        "#****************** Initialize the CAD-->Create pane window *************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_INITIALIZE {model_index}"
    ]

    script.append_lines(lines)
    return

def cad_create_import_curve_txt(txt_filepath, units='METER', dimension='2D', frame=1, plane='YZ'):
    """
    Appends lines to script state to import a CAD-->Create drawing curve from a txt file.
    

    :param units: Units for CAD_CREATE_IMPORT_CURVE_TXT (must be one of the specified units).
    :param dimension: Dimension (either "2D" or "3D").
    :param frame: Frame as an integer.
    :param plane: Plane orientation (one of "YZ", "XZ", "XY").
    :param filepath: Path to the txt file to import.
    """
    check_file_existence(txt_filepath)

    
    valid_dimensions = ["2D", "3D"]
    valid_planes = ["YZ", "XZ", "XY"]
    
    check_valid_length_units(units)
    
    if dimension not in valid_dimensions:
        raise ValueError(f"Invalid dimension: {dimension}. Must be one of {', '.join(valid_dimensions)}.")
    
    if plane not in valid_planes:
        raise ValueError(f"Invalid plane: {plane}. Must be one of {', '.join(valid_planes)}.")

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

def cad_create_import_ccs(ccs_filepath):
    """
    Appends lines to script state to import a CAD-->Create drawing curve from a csv file.
    

    :param ccs_filepath: Path to the csv file to import.
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

def cad_create_auto_cross_sections(frame=1, axis='Y', sections=20, body_index=1, 
                               growth_scheme=3, growth_rate=1.2, symmetry='NONE'):
    """
    Appends lines to script state to create a series of automatic cross-sections from mesh body.
    

    :param frame: Index of coordinate system to be used.
    :param axis: Sweep direction for creating cross-section curves (X, Y, Z).
    :param sections: Number of cross-sections requested.
    :param body_index: Index of the mesh body to be used for creating cross-sections.
    :param growth_scheme: Clustering scheme to be used when positioning cross-sections along the sweep axis.
    :param growth_rate: Growth rate to be used with the selected growth_scheme.
    :param symmetry: Symmetry plane to be used for creating half-section curves (YZ, XZ, XY) or NONE for full section.
    """
    
    lines = [
        "#************************************************************************",
        "#****** Create a series of automatic cross-sections from mesh body ******",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_AUTO_CROSS_SECTIONS {frame} {axis} {sections} {body_index} {growth_scheme} {growth_rate} {symmetry}"
    ]

    script.append_lines(lines)
    return

def cad_create_cross_section(frame=1, plane='XZ', offset=0.0, body_index=1, quadrant=3):
    """
    Appends lines to script state to create a cross-section from an existing mesh body.
    

    :param frame: Index of coordinate system to be used.
    :param plane: Plane of the selected coordinate system to use for slicing the mesh faces (YZ, XZ, XY).
    :param offset: Offset distance of the selected plane along the normal axis of the plane.
    :param body_index: Index of the mesh body to be used for creating cross-section.
    :param quadrant: Quadrant information for creating cross-section.

    Value YZ  XZ  XY 
        1 +Y +X +X
        2 -Y -X -X
        3 +Z +Z +Y
        4 -Z -Z -Y   
    """
    
    # Type checks and validations
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("Frame should be an integer greater than 0.")
    
    if plane not in ['YZ', 'XZ', 'XY']:
        raise ValueError("Invalid plane value. Allowed values: YZ, XZ, XY.")
    
    if not isinstance(offset, (int, float)):
        raise ValueError("Offset should be a numeric value.")
    
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("Body index should be an integer greater than 0.")
    
    if not isinstance(quadrant, int) or quadrant not in [1, 2, 3, 4]:
        raise ValueError("Quadrant should be one of the following integer values: 1, 2, 3, 4.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a cross-sections from an existing mesh body **********",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_CROSS_SECTION {frame} {plane} {offset} {body_index} {quadrant}"
    ]

    script.append_lines(lines)
    return

def cad_create_point_curve(x=0.0, y=1.0, z=0.0):
    """
    Appends lines to script state to create a singular point curve in 3D.
    

    :param x: X coordinate of the point curve.
    :param y: Y coordinate of the point curve.
    :param z: Z coordinate of the point curve.
    """
    
    # Type checks and validations
    if not isinstance(x, (int, float)):
        raise ValueError("X should be a numeric value.")
    
    if not isinstance(y, (int, float)):
        raise ValueError("Y should be a numeric value.")
    
    if not isinstance(z, (int, float)):
        raise ValueError("Z should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a singular point curve (3D) **************************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_CURVE_POINT {x} {y} {z}"
    ]

    script.append_lines(lines)
    return

def cad_create_curve_arc(x0=0.0, y0=0.0, z0=0.0, x1=-1.0, y1=0.0, z1=0.0, x2=0.0, y2=1.0, z2=0.0):
    """
    Appends lines to script state to create a circular arc curve in 3D.
    

    :param x0, y0, z0: Vertex coordinates of the origin of the circular arc.
    :param x1, y1, z1: Vertex coordinates of the first vertex of the circular arc curve.
    :param x2, y2, z2: Vertex coordinates of the second vertex of the circular arc curve.
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

def cad_create_curve_select(curve_index=1):
    """
    Appends lines to script state to select one of the CAD-->Create drawing curves.
    

    :param curve_index: Index of the drawing curve to be selected.
    
    Example usage:
    cad_create_curve_select(, 2)
    cad_create_curve_select(, -1)  # To select ALL curves
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

def cad_create_curve_unselect(curve_index=1):
    """
    Appends lines to script state to unselect one of the CAD-->Create drawing curves.
    

    :param curve_index: Index of the drawing curve to be unselected.
    
    Example usage:
    cad_create_curve_unselect(, 1)
    cad_create_curve_unselect(, -1)  # To unselect ALL curves
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

def cad_create_curve_reverse(curve_index=1):
    """
    Appends lines to script state to reverse CAD->Create drawing curves by index.


    :param curve_index: Index of the drawing curve to be reversed.

    Example usage:
    cad_create_curve_reverse(, 2)
    """

    # Type and value checking
    if not isinstance(curve_index, int):
        raise ValueError("`curve_index` should be an integer value.")

    if curve_index == -1:
        lines = [
            "#************************************************************************",
            "#********** Reverse ALL of the CAD-->Create drawing curves **************",
            "#************************************************************************",
            "#",
            "CAD_CREATE_CURVE_REVERSE -1"
        ]
    else:
        lines = [
            "#************************************************************************",
            "#********** Reverse specific CAD-->Create drawing curves by index *******",
            "#************************************************************************",
            "#",
            f"CAD_CREATE_CURVE_REVERSE {curve_index}"
        ]

    script.append_lines(lines)
    return


def cad_create_curve_delete_all():
    """
    Appends lines to script state to delete all CAD->Create drawing curves.



    Example usage:
    cad_create_curve_delete_all()
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

def cad_create_curve_delete_selected():
    """
    Appends lines to script state to delete only selected CAD-->Create drawing curves.


    
    Example usage:
    cad_create_curve_delete_selected()
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

def cad_create_curve_delete_unselected():
    """
    Appends lines to script state to delete only unselected CAD-->Create drawing curves.


    
    Example usage:
    cad_create_curve_delete_unselected()
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

def cad_create_curve_export_ccs(file_path):
    """
    Appends lines to script state to export selected CAD-->Create drawing curves to CSV file.


    :param file_path: File name with the path to the file.
    
    Example usage:
    cad_create_curve_export_ccs(, 'C:\\Users\\Desktop\\Geometries\\sample_CCS_export.csv')
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

def import_cad(cad_filepath):
    """
    Appends lines to script state to import a CAD geometry into the simulation.
    

    :param cad_filepath: Path to the CAD file.
    
    Example usage:
    import_cad(, 'C:\\Users\\Desktop\\Geometries\\sample.igs')
    """

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

def convert_cad_to_mesh(model_index):
    """
    Appends lines to script state to transfer CAD model mesh to the 
    Mesh node of the simulation.
    

    :param model_index: Index of the CAD model to be transferred to the mesh node.
    
    Example usage:
    convert_cad_to_mesh(, 1)
    """
    
    # Type and value checking
    if not isinstance(model_index, int):
        raise ValueError("`model_index` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****** Transfer CAD model mesh to the Mesh node of the simulation ******",
        "#************************************************************************",
        "#",
        f"CONVERT_CAD_TO_MESH {model_index}"
    ]
    
    script.append_lines(lines)
    return

