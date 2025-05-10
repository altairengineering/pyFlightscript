import os
from .utils import *    
from .script import script

def create_new_base_region(surface, base_type='EMPIRICAL', base_pressure_coefficient=-0.2):
    """
    Appends lines to script state to create a new base region.

    :param surface: Index of the boundary surface to be marked as base region boundary.
    :param base_type: Type of base region calculation. Options are 'EMPIRICAL' or 'CONSTANT'. Defaults to 'EMPIRICAL'.
    :param base_pressure_coefficient: Pressure coefficient to be applied in base regions. Defaults to -0.2.

    Example usage:
    create_new_base_region(3, base_type='EMPIRICAL', base_pressure_coefficient=-0.2)
    """
    
    # Type and value checking
    if not isinstance(surface, int) or surface <= 0:
        raise ValueError("`surface` should be an integer value greater than 0.")
    
    if not isinstance(base_pressure_coefficient, (int, float)):
        raise ValueError("`base_pressure_coefficient` should be an integer or float value.")
    
    if base_type not in ['EMPIRICAL', 'CONSTANT']:
        raise ValueError("`base_type` should be either 'EMPIRICAL' or 'CONSTANT'.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new base region ****************************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_BASE_REGION {surface} {base_type} {base_pressure_coefficient}",
    ]

    script.append_lines(lines)
    return

def auto_detect_base_regions():
    """
    Appends lines to script state to auto-detect base regions on the geometry.

    Example usage:
    auto_detect_base_regions()


    """
    
    lines = [
        "#************************************************************************",
        "#****************** Auto-detect base regions on the geometry ************",
        "#************************************************************************",
        "#",
        "AUTO_DETECT_BASE_REGIONS"
    ]

    script.append_lines(lines)
    return

def detect_base_regions_by_surface(boundary_index=1):
    """
    Example usage:
    detect_base_regions_by_surface()
    
    Appends lines to script state to detect base regions by surface index.
    

    :param boundary_index: Index of the mesh boundary to use for marking base regions.
    """
    
    # Type and value checking
    if not isinstance(boundary_index, int) or boundary_index <= 0:
        raise ValueError("`boundary_index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Detect base regions by surface index ****************",
        "#************************************************************************",
        "#",
        f"DETECT_BASE_REGIONS_BY_SURFACE {boundary_index}"
    ]

    script.append_lines(lines)
    return

def set_base_region_trailing_edges(base_region_boundary=-1):
    """
    Example usage:
    set_base_region_trailing_edges()

    Appends lines to script state to set base region trailing edges.


    :param base_region_boundary: Index of the base region boundary to use for marking trailing edges.
    """
    
    # Type and value checking
    if not isinstance(base_region_boundary, int):
        raise ValueError("`base_region_boundary` should be an integer value.")
    if base_region_boundary == 0:
        raise ValueError("`base_region_boundary` should be greater than 0 or -1.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set base region trailing edges **********************",
        "#************************************************************************",
        "#",
        f"SET_BASE_REGION_TRAILING_EDGES {base_region_boundary}"
    ]

    script.append_lines(lines)
    return

def delete_base_region(base_region_index):
    """
    Example usage:
    delete_base_region(2)
    
    Appends lines to script state to delete an existing base region.
    

    :param base_region_index: Index of the base region boundary to be deleted.
    """
    
    # Type and value checking
    if not isinstance(base_region_index, int) or base_region_index <= 0:
        raise ValueError("`base_region_index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an existing base region **********************",
        "#************************************************************************",
        "#",
        f"DELETE_BASE_REGION {base_region_index}"
    ]

    script.append_lines(lines)
    return

def select_base_region(base_region_index):
    """
    Example usage:
    select_base_region(2)
    
    Appends lines to script state to select an existing base region.
    
    :param base_region_index: Index of the base region boundary to be deleted.
    """
    
    # Type and value checking
    if not isinstance(base_region_index, int) or base_region_index <= 0:
        raise ValueError("`base_region_index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Select an existing base region **********************",
        "#************************************************************************",
        "#",
        f"SELECT_BASE_REGION_FACES {base_region_index}"
    ]

    script.append_lines(lines)
    return