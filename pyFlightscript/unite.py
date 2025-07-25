import os
from .utils import *    
from .script import script
from .types import *

def boolean_unite_mesh(num_bodies, bodies_info=None):
    """
    Generates lines to unite mesh bodies either selectively or all bodies with positive volume.

    :param num_bodies: An integer indicating the number of mesh bodies to unite, or -1 to unite all with positive volume.
    :param bodies_info: Optional list of tuples where each tuple contains the index and the volume type ('POSITIVE' or 'NEGATIVE')
                        for each body when num_bodies is not -1.
    """
    
    # Header for the script block
    lines = [
        "#************************************************************************",
        "#************* Unite a selection of mesh bodies *************************",
        "#************************************************************************",
    ]
    
    # Handling all bodies with a positive unite volume
    if num_bodies == -1:
        lines.append("BOOLEAN_UNITE_MESH -1")
    else:
        # Type and value checking
        if not isinstance(num_bodies, int):
            raise ValueError("`num_bodies` should be an integer.")
        
        if bodies_info is None or not all(isinstance(body, tuple) and len(body) == 2 for body in bodies_info):
            raise ValueError("`bodies_info` must be a list of tuples (index, volume type).")
        
        if len(bodies_info) != num_bodies:
            raise ValueError("The length of `bodies_info` must match `num_bodies`.")

        # Append the command to unite specified bodies
        lines.append(f"BOOLEAN_UNITE_MESH {num_bodies}")
        for index, volume_type in bodies_info:
            if not isinstance(index, int) or volume_type not in {'POSITIVE', 'NEGATIVE'}:
                raise ValueError("Each body info must be a tuple of an integer and a string 'POSITIVE' or 'NEGATIVE'.")
            lines.append(f"{index} {volume_type.upper()}")
    
    script.append_lines(lines)
    return

def boolean_unite_path(openvsp_path):
    """
    Sets the path to the OpenVSP executable used for the CompGeom unite function.

    :param openvsp_path: The file path to the OpenVSP executable.
    """
    
    # Check if the path is a string and not empty
    if not isinstance(openvsp_path, str) or not openvsp_path:
        raise ValueError("`openvsp_path` should be a non-empty string.")

    # Formatting script lines with the specified OpenVSP path
    lines = [
        "#************************************************************************",
        "#************* Specify the OpenVSP path for the Unite function **********",
        "#************************************************************************",
        "BOOLEAN_UNITE_PATH",
        f"OPENVSP_PATH {openvsp_path}"
    ]

    script.append_lines(lines)
    return

def boolean_unite_geometry(bodies, openvsp_path, bodies_values=None):
    """
    Appends lines to script state to boolean unite a selection of geometry bodies.
    

    :param bodies: Number of geometry bodies being Boolean-united. Can be -1 to specifiy all.
    :param openvsp_path: Path to OpenVSP executable used for the CompGeom unite function call.
    :param bodies_values: List of tuples containing index values of the geometry surfaces 
                          and their volume types.

    Example usage:
    boolean_unite_geometry(, 5, r"\C\Test_folder\...\VSP\", 
                          bodies_values=[(1, 'POSITIVE'), (2, 'POSITIVE'), 
                                         (3, 'NEGATIVE'), (4, 'NEGATIVE'), (5, 'POSITIVE')])
                          
    """
    
    # Type and value checking
    if not isinstance(bodies, int):
        raise ValueError("`bodies` should be a positive integer value.")
    
    check_file_existence(openvsp_path)
    
    if bodies_values:
        if len(bodies_values) != bodies:
            raise ValueError("`bodies_values` list should match the number specified in `bodies`.")
        
        for item in bodies_values:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in `bodies_values` should be a tuple of size 2.")
            
            index, volume_type = item
            if not isinstance(index, int) or index <= 0:
                raise ValueError("Index value in each tuple of `bodies_values` should be a positive integer.")
            
            valid_volume_types = ['POSITIVE', 'NEGATIVE']
            if volume_type not in valid_volume_types:
                raise ValueError(f"Volume type in each tuple of `bodies_values` should be one of {valid_volume_types}")
    
    lines = [
        "#************************************************************************",
        "#************* Boolean unite a selection of geometry bodies *************",
        "#************************************************************************",
        "#",
        "BOOLEAN_UNITE_GEOMETRY",
        f"BODIES {bodies}"
    ]

    # Add bodies values if provided
    if bodies_values:
        for index, volume_type in bodies_values:
            lines.append(f"{index} {volume_type}")

    lines.append(f"OPENVSP_PATH {openvsp_path}")

    script.append_lines(lines)
    return


