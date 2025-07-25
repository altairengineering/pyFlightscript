import os
from .utils import *    
from .script import script
from .types import *
from typing import Union, Optional, Literal, List

def create_new_base_region(
    surface: int,
    base_type: str = 'EMPIRICAL',
    base_pressure_coefficient: float = -0.2
) -> None:
    """
    Create a new base region.

    This function appends a command to the script state to create a new base
    region with a specified surface, base type, and pressure coefficient.

    Parameters
    ----------
    surface : int
        The index of the boundary surface to be marked as a base region boundary.
        Must be an integer greater than 0.
    base_type : str, optional
        The type of base region calculation. Can be either 'EMPIRICAL' or
        'CONSTANT'. Defaults to 'EMPIRICAL'.
    base_pressure_coefficient : float, optional
        The pressure coefficient to be applied in the base regions.
        Defaults to -0.2.

    Raises
    ------
    ValueError
        If `surface` is not a positive integer, if `base_type` is not a
        valid base region type, or if `base_pressure_coefficient` is not a
        numeric value.

    Examples
    --------
    >>> # Create a new base region with default parameters
    >>> create_new_base_region(surface=3)

    >>> # Create a new base region with a constant base type
    >>> create_new_base_region(surface=4, base_type='CONSTANT', base_pressure_coefficient=-0.15)
    """
    
    # Type and value checking
    if not isinstance(surface, int) or surface <= 0:
        raise ValueError("`surface` should be an integer value greater than 0.")
    
    
        
    if not isinstance(base_pressure_coefficient, (int, float)):
        raise ValueError("`base_pressure_coefficient` should be a numeric value.")
    
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

    Examples
    --------
    >>> #auto_detect_base_regions()

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

def detect_base_regions_by_surface(boundary_index: int = 1) -> None:
    """
    Detect base regions by surface index.

    This function appends a command to the script state to detect base regions
    using a specified mesh boundary index.

    Parameters
    ----------
    boundary_index : int, optional
        The index of the mesh boundary to use for marking base regions.
        Must be a positive integer. Defaults to 1.

    Raises
    ------
    ValueError
        If `boundary_index` is not an integer greater than 0.

    Examples
    --------
    >>> # Detect base regions using boundary index 2
    >>> detect_base_regions_by_surface(boundary_index=2)

    >>> # Detect base regions using the default boundary index
    >>> detect_base_regions_by_surface()
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

def set_base_region_trailing_edges(base_region_boundary: int = -1) -> None:
    """
    Set base region trailing edges.

    This function appends a command to the script state to set the trailing
    edges for a specified base region boundary.

    Parameters
    ----------
    base_region_boundary : int, optional
        The index of the base region boundary to use for marking trailing edges.
        A value of -1 indicates all base region boundaries. Must not be 0.
        Defaults to -1.

    Raises
    ------
    ValueError
        If `base_region_boundary` is not an integer or is equal to 0.

    Examples
    --------
    >>> # Set trailing edges for base region boundary 3
    >>> set_base_region_trailing_edges(base_region_boundary=3)

    >>> # Set trailing edges for all base region boundaries
    >>> set_base_region_trailing_edges()
    """
    
    # Type and value checking
    if not isinstance(base_region_boundary, int):
        raise ValueError("`base_region_boundary` should be an integer value.")
    if base_region_boundary == 0:
        raise ValueError("`base_region_boundary` cannot be 0. It must be a positive integer or -1.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set base region trailing edges **********************",
        "#************************************************************************",
        "#",
        f"SET_BASE_REGION_TRAILING_EDGES {base_region_boundary}"
    ]

    script.append_lines(lines)
    return

def delete_base_region(base_region_index: int) -> None:
    """
    Delete an existing base region.

    This function appends a command to the script state to delete an existing
    base region by its index.

    Parameters
    ----------
    base_region_index : int
        The index of the base region to be deleted. Must be a positive integer.

    Raises
    ------
    ValueError
        If `base_region_index` is not an integer greater than 0.

    Examples
    --------
    >>> # Delete the base region with index 2
    >>> delete_base_region(base_region_index=2)
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

def select_base_region(base_region_index: int) -> None:
    """
    Select an existing base region.

    This function appends a command to the script state to select the faces
    of an existing base region by its index.

    Parameters
    ----------
    base_region_index : int
        The index of the base region to be selected. Must be a positive integer.

    Raises
    ------
    ValueError
        If `base_region_index` is not an integer greater than 0.

    Examples
    --------
    >>> # Select the base region with index 2
    >>> select_base_region(base_region_index=2)
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