import os
from .utils import *    
from .script import script
from .types import *

def create_new_inlet(surface_id: int, velocity: float) -> None:
    """
    Create a new inlet boundary with specified velocity along the surface normal.

    This function appends a command to the script state to create a new inlet
    boundary with a specified velocity.

    Parameters
    ----------
    surface_id : int
        The index of the boundary surface to be marked as an inlet. Must be > 0.
    velocity : float
        The velocity magnitude along the surface normal vector of the inlet faces.
        Positive or negative values control the direction of flow.

    Returns
    -------
    None

    Examples
    --------
    >>> # Create a new inlet with surface_id 3 and velocity 101.0
    >>> create_new_inlet(3, 101.0)
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

def set_inlet_custom_profile(inlet_id: int, motion_filepath: str) -> None:
    """
    Set a custom inlet profile using an external file.

    This function appends a command to the script state to set a custom inlet
    profile using an external file.

    Parameters
    ----------
    inlet_id : int
        The index of the inlet boundary.
    motion_filepath : str
        The path to the file containing the motion data.

    Returns
    -------
    None

    Examples
    --------
    >>> # Set a custom inlet profile for inlet_id 1
    >>> set_inlet_custom_profile(1, 'C:/Users/Desktop/Models/custom_inlet_profile.txt')
    """
    
    # Type and value checking
    if not isinstance(inlet_id, int) or inlet_id <= 0:
        raise ValueError("`inlet_id` should be an integer value greater than 0.")
    
    if not isinstance(motion_filepath, str):
        raise ValueError("`motion_filepath` should be a string.")
    
    check_file_existence(motion_filepath)
    
    lines = [
        "#************************************************************************",
        "#******* Upload custom velocity inlet profile from external file ********",
        "#************************************************************************",
        "#",
        "SET_INLET_CUSTOM_PROFILE",
        f"{inlet_id}",
        f"{motion_filepath}"
    ]

    script.append_lines(lines)
    return

def remesh_inlet(inlet: int, inner_radius: float = 0.0, elements: int = 10, 
                 growth_scheme: int = 2, growth_rate: float = 1.2) -> None:
    """
    Radially mesh an existing inlet boundary.

    This function appends a command to the script state to radially mesh an
    existing inlet boundary.

    Parameters
    ----------
    inlet : int
        The index of the inlet boundary to be meshed.
    inner_radius : float, optional
        The inner radius of the inlet boundary, by default 0.0.
    elements : int, optional
        The number of mesh faces in the radial direction, by default 10.
    growth_scheme : int, optional
        The growth scheme type (1 or 2), by default 2.
    growth_rate : float, optional
        The growth rate for the radial distribution of mesh faces, by default 1.2.

    Returns
    -------
    None

    Examples
    --------
    >>> # Remesh an inlet with default parameters
    >>> remesh_inlet(1)

    >>> # Remesh an inlet with custom parameters
    >>> remesh_inlet(1, inner_radius=0.1, elements=20, growth_scheme=1, growth_rate=1.1)
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

def delete_inlet(inlet: int) -> None:
    """
    Delete an existing inlet boundary.

    This function appends a command to the script state to delete an existing
    inlet boundary.

    Parameters
    ----------
    inlet : int
        The index of the inlet boundary to be deleted.

    Returns
    -------
    None

    Examples
    --------
    >>> # Delete inlet 1
    >>> delete_inlet(1)
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


