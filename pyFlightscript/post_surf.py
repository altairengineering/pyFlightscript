from .utils import *    
from .script import script
from .types import *

from typing import List, Union
from . import script
from .types import VALID_PLANE_LIST, RunOptions, VALID_RUN_OPTIONS

def create_new_surface_section(
    frame: int = 1,
    plane: str = 'XZ',
    offset: float = 1.0,
    plot_direction: int = 1,
    symmetry: RunOptions = 'DISABLE',
    surfaces: Union[int, List[int]] = -1
) -> None:
    """
    Create a new surface section.

    This function appends a command to the script state to create a single
    surface section defined by a plane and offset.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system for this section, by default 1.
    plane : str, optional
        Section plane, by default 'XZ'. Must be one of `VALID_PLANE_LIST`.
    offset : float, optional
        Offset distance of the plane, by default 1.0.
    plot_direction : int, optional
        Plotting direction of the surface section (1 or 2), by default 1.
    symmetry : RunOptions, optional
        Symmetry option, by default 'DISABLE'. Must be one of `VALID_RUN_OPTIONS`.
    surfaces : Union[int, List[int]], optional
        List of geometry surfaces for the section, or -1 for all, by default -1.

    Examples
    --------
    >>> # Create a section on all boundaries
    >>> create_new_surface_section(plane='YZ', offset=2.5)

    >>> # Create a section on specific surfaces
    >>> create_new_surface_section(surfaces=[1, 4, 5])
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}")
    if not isinstance(offset, (int, float)):
        raise ValueError("`offset` should be a numeric value.")
    if plot_direction not in [1, 2]:
        raise ValueError("`plot_direction` must be 1 or 2.")
    if symmetry not in VALID_RUN_OPTIONS:
        raise ValueError(f"`symmetry` must be one of {VALID_RUN_OPTIONS}")

    surface_count = -1
    surface_list = []
    if isinstance(surfaces, list):
        if not all(isinstance(s, int) for s in surfaces):
            raise ValueError("`surfaces` list must contain only integers.")
        surface_count = len(surfaces)
        surface_list = surfaces
    elif not isinstance(surfaces, int) or surfaces != -1:
        raise ValueError("`surfaces` must be -1 or a list of integers.")

    lines = [
        "#************************************************************************",
        f"#****************** Create new surface section ************************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_SURFACE_SECTION {frame} {plane} {offset} {plot_direction} {symmetry} {surface_count}"
    ]

    if surface_list:
        lines.append(" ".join(map(str, surface_list)))

    script.append_lines(lines)
    return

def new_surface_section_distribution(
    frame: int = 1,
    plane: str = 'XZ',
    num_sections: int = 20,
    plot_direction: int = 1,
    surfaces: List[int] = [1, 4, 5]
) -> None:
    """
    Create a new surface section distribution.

    This function appends a command to the script state to create multiple
    surface sections distributed along a specified plane.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system for the sections, by default 1.
    plane : str, optional
        Section plane, by default 'XZ'. Must be one of `VALID_PLANE_LIST`.
    num_sections : int, optional
        Number of sections to create, by default 20.
    plot_direction : int, optional
        Plotting direction (1 or 2), by default 1.
    surfaces : List[int], optional
        List of geometry surfaces for the sections, by default [1, 4, 5].

    Examples
    --------
    >>> # Create a distribution of 30 sections on specific surfaces
    >>> new_surface_section_distribution(num_sections=30, surfaces=[1, 2, 3])
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    if plane not in VALID_PLANE_LIST:
        raise ValueError(f"`plane` should be one of {VALID_PLANE_LIST}")
    if not isinstance(num_sections, int) or num_sections <= 0:
        raise ValueError("`num_sections` must be a positive integer.")
    if plot_direction not in [1, 2]:
        raise ValueError("`plot_direction` must be 1 or 2.")
    if not isinstance(surfaces, list) or not all(isinstance(s, int) for s in surfaces):
        raise ValueError("`surfaces` must be a list of integers.")

    lines = [
        "#************************************************************************",
        "#****************** Create new surface section distribution *************",
        "#************************************************************************",
        "#",
        "NEW_SURFACE_SECTION_DISTRIBUTION",
        f"FRAME {frame}",
        f"PLANE {plane}",
        f"NUM_SECTIONS {num_sections}",
        f"PLOT_DIRECTION {plot_direction}",
        f"SURFACES {len(surfaces)}",
        " ".join(map(str, surfaces))
    ]
    script.append_lines(lines)
    return

def compute_surface_sectional_loads(units: ValidForceUnits = 'NEWTONS') -> None:
    """
    Compute sectional loads on existing surface sections.

    This function appends a command to the script state to calculate the
    aerodynamic loads on all currently defined surface sections.

    Parameters
    ----------
    units : ValidForceUnits, optional
        The units for the computed loads, by default 'NEWTONS'. Must be one
        of `VALID_FORCE_UNITS_LIST`.

    Examples
    --------
    >>> # Compute sectional loads in Newtons
    >>> compute_surface_sectional_loads()

    >>> # Compute sectional loads as coefficients
    >>> compute_surface_sectional_loads(units='COEFFICIENTS')
    """
    if units not in VALID_FORCE_UNITS_LIST:
        raise ValueError(f"`units` must be one of {VALID_FORCE_UNITS_LIST}")

    lines = [
        "#************************************************************************",
        "#********** Compute sectional loads on existing surface sections ********",
        "#************************************************************************",
        "#",
        f"COMPUTE_SURFACE_SECTIONAL_LOADS {units}"
    ]
    script.append_lines(lines)
    return

def export_surface_sectional_loads(filename: str) -> None:
    """
    Export sectional loads on existing surface sections.

    This function appends a command to the script state to export the
    previously computed sectional loads to a file.

    Parameters
    ----------
    filename : str
        The absolute path of the file to export the loads to.

    Examples
    --------
    >>> # Export sectional loads to a file
    >>> export_surface_sectional_loads('C:/data/sectional_loads.txt')
    """
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string.")

    lines = [
        "#************************************************************************",
        "#********** Export sectional loads on existing surface sections *********",
        "#************************************************************************",
        "#",
        "EXPORT_SURFACE_SECTIONAL_LOADS",
        f"{filename}"
    ]
    script.append_lines(lines)
    return

def update_all_surface_sections():
    """
    Appends lines to script state to update the surface sections.

    Examples
    --------
    >>> # Update the surface sections
    >>> update_all_surface_sections()
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Update the surface sections *************************",
        "#************************************************************************",
        "#",
        "UPDATE_ALL_SURFACE_SECTIONS"
    ]

    script.append_lines(lines)
    return

def export_all_surface_sections(filename: str) -> None:
    """
    Appends lines to script state to export all surface sections to a file.
    
    Parameters
    ----------
    filename : str
        Filename with path for the surface sections.
    
    Examples
    --------
    >>> # Export all surface sections to a file
    >>> export_all_surface_sections('C:/.../Test_surface_sections.txt')
    """
    
    # Type and value checking
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export all surface sections to file *****************",
        "#************************************************************************",
        "#",
        "EXPORT_ALL_SURFACE_SECTIONS",
        f"{filename}"
    ]
    
    script.append_lines(lines)
    return

def delete_surface_section(index: int) -> None:
    """
    Appends lines to script state to delete a surface section.
    
    Parameters
    ----------
    index : int
        Index of the surface section to be deleted.
    
    Examples
    --------
    >>> # Delete surface section 2
    >>> delete_surface_section(2)
    """
    
    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete a surface section ****************************",
        "#************************************************************************",
        "#",
        f"DELETE_SURFACE_SECTION {index}"
    ]
    
    script.append_lines(lines)
    return

def delete_all_surface_sections():
    """
    Appends lines to script state to delete all existing probe points.
    
    Examples
    --------
    >>> # Delete all surface sections
    >>> delete_all_surface_sections()
    """
    
    lines = [
        "#************************************************************************",
        "#******************** Delete all surface sections ***********************",
        "#************************************************************************",
        "#",
        "DELETE_ALL_SURFACE_SECTIONS"
    ]

    script.append_lines(lines)
    return
