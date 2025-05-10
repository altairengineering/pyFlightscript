import os
from .utils import *    
from .script import script

def create_new_inlet(surface_id, velocity):
    """
    Creates a new inlet boundary with specified velocity along the surface normal.
    
    Args:
        surface_id (int): Index of the boundary surface to be marked as inlet (must be > 0)
        velocity (float): Velocity magnitude along the surface normal vector of the inlet faces.
                         Positive or negative values control the direction of flow.
    
    Example usage:
        create_new_inlet(3, 101.0)
    """
    
    # Type and value checking
    if not isinstance(surface_id, int) or surface_id <= 0:
        raise ValueError("`surface_id` should be an integer value greater than 0.")
    
    if not isinstance(velocity, (int, float)):
        raise ValueError("`velocity` should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#*********************** Create a new inlet boundary ********************",
        "#************************************************************************",
        f"CREATE_NEW_INLET {surface_id} {velocity}"
    ]
    
    script.append_lines(lines)
    return

def set_inlet_custom_profile(inlet_id, motion_filpath):
    """
    Appends lines to script state to set a custom inlet profile 
    using an external file.
    
    Example usage:
    set_inlet_custom_profile(, 1, 'C:\\Users\\Desktop\\Models\\custom_inlet_profile.txt')
    
    :param inlet_id: Index of the inlet boundary.
    :param motion_filpath: Path to the file containing the motion data.
    """
    
    # Type and value checking
    if not isinstance(inlet_id, int) or inlet_id <= 0:
        raise ValueError("`inlet_id` should be an integer value greater than 0.")
    
    if not isinstance(motion_filpath, str):
        raise ValueError("`motion_filpath` should be a string.")
    
    check_file_existence(motion_filpath)
    
    lines = [
        "#************************************************************************",
        "#******* Upload custom velocity inlet profile from external file ********",
        "#************************************************************************",
        "#",
        "SET_INLET_CUSTOM_PROFILE",
        f"{inlet_id}",
        f"{motion_filpath}"
    ]

    script.append_lines(lines)
    return

def remesh_inlet(inlet, inner_radius=0.0, elements=10, 
                 growth_scheme=2, growth_rate=1.2):
    """
    Appends lines to script state to radial mesh an existing inlet boundary.
    
    Example usage:
    remesh_inlet(, 1)
    

    :param inlet: Index of inlet boundary to be meshed.
    :param inner_radius: Inner radius of the inlet boundary.
    :param elements: Number of mesh faces in the radial direction.
    :param growth_scheme: Growth scheme type (1 or 2).
    :param growth_rate: Growth rate for radial distribution of mesh faces.
    """
    
    # Type and value checking
    if not isinstance(inlet, int) or inlet < 1:
        raise ValueError("`inlet` should be an integer value greater than or equal to 1.")
    
    if not isinstance(inner_radius, (int, float)) or inner_radius < 0.0:
        raise ValueError("`inner_radius` should be a non-negative integer or float value.")
    
    if not isinstance(elements, int) or elements < 1:
        raise ValueError("`elements` should be a positive integer value.")
    
    if growth_scheme not in [1, 2]:
        raise ValueError("`growth_scheme` should be either 1 (Successive) or 2 (Dual-side).")
    
    if not isinstance(growth_rate, (int, float)) or growth_rate <= 0:
        raise ValueError("`growth_rate` should be a positive integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Radial mesh an existing inlet boundary **************",
        "#************************************************************************",
        "#",
        "REMESH_INLET",
        f"INLET {inlet}",
        f"INNER_RADIUS {inner_radius}",
        f"ELEMENTS {elements}",
        f"GROWTH_SCHEME {growth_scheme}",
        f"GROWTH_RATE {growth_rate}"
    ]

    script.append_lines(lines)
    return

def delete_inlet(inlet):
    """
    Appends lines to script state to delete an existing inlet boundary.
    
    Example usage:
    delete_inlet(, 1)
    

    :param inlet: Index of the inlet boundary to be deleted.
    """
    
    # Type and value checking
    if not isinstance(inlet, int) or inlet <= 0:
        raise ValueError("`inlet` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an existing inlet boundary *******************",
        "#************************************************************************",
        "#",
        f"DELETE INLET {inlet}"
    ]

    script.append_lines(lines)
    return


