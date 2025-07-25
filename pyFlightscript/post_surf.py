from .utils import *    
from .script import script
from .types import *

def create_new_surface_section(frame=1, plane='XZ', offset=1.0, 
                               plot_direction=1, symmetry='DISABLE', surfaces=-1):
    """
    Appends lines to script state to create a new surface section.
    

    :param frame: Index of the coordinate system used for this surface section.
    :param plane: Section plane. One of the following: XY, XZ or YZ.
    :param offset: Offset distance of the plane in the coordinate system.
    :param plot_direction: Value to describe the plotting direction of the surface section.
    :param symmetry: Symmetry option. One of the following: ENABLE or DISABLE.
    :param surfaces: List of geometry surfaces assigned to the surface section, or -1 for all boundaries.
    
    Example usage:
        create_new_surface_section(frame=1, plane='XZ', offset=1.0, 
                                 plot_direction=1, symmetry='DISABLE', surfaces=[1,4,5])
        # Or for all boundaries:
        create_new_surface_section(frame=1, plane='XZ', offset=1.0, 
                                 plot_direction=1, symmetry='DISABLE', surfaces=-1)
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_planes = ['XY', 'XZ', 'YZ']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")
    
    if not isinstance(offset, (int, float)):
        raise ValueError("`offset` should be an integer or float value.")
    
    if plot_direction not in [1, 2]:
        raise ValueError("`plot_direction` should be 1 or 2.")
    
    # Modified validation for surfaces parameter
    if surfaces == -1:
        surface_count = -1
        surface_list = []
    else:
        if not all(isinstance(surface, int) for surface in surfaces):
            raise ValueError("`surfaces` should be a list of integer values or -1.")
        surface_count = len(surfaces)
        surface_list = surfaces

    # Modified header text based on surfaces input
    header_text = "all boundaries" if surfaces == -1 else "selected boundaries"
    
    lines = [
        "#************************************************************************",
        f"#****************** Create new surface section (selected boundaries) ****",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_SURFACE_SECTION {frame} {plane} {offset} {plot_direction} {symmetry} {surface_count}"
    ]

    # Add surface list only if not using -1
    if surfaces != -1:
        lines.append(" ".join(map(str, surface_list)))

    script.append_lines(lines)
    return

def new_surface_section_distribution(frame=1, plane='XZ', 
                                     num_sections=20, plot_direction=1, surfaces=[1, 4, 5]):
    """
    Appends lines to script state to create new surface section distribution.
    
    Example usage:
    >>> new_surface_section_distribution()
    

    :param frame: Index of the coordinate system to be used for this surface section.
    :param plane: Section plane.
    :param num_sections: Number of sections to be created.
    :param plot_direction: Plotting direction of the surface section.
    :param surfaces: List of geometry surfaces assigned to the surface section.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_planes = ['XY', 'XZ', 'YZ']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")

    if not isinstance(num_sections, int) or num_sections <= 0:
        raise ValueError("`num_sections` should be a positive integer value.")
    
    if plot_direction not in [1, 2]:
        raise ValueError("`plot_direction` should be 1 or 2.")
    
    if not isinstance(surfaces, list) or not all(isinstance(s, int) for s in surfaces):
        raise ValueError("`surfaces` should be a list of integer values.")
    
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

def compute_surface_sectional_loads(units='NEWTONS'):
    """
    Appends lines to script state to compute sectional loads on existing surface sections.
    
    Example usage:
    >>> compute_surface_sectional_loads()
    

    :param units: Unit type.
    """
    
    check_valid_force_units(units)
    
    lines = [
        "#************************************************************************",
        "#********** Compute sectional loads on existing surface sections ********",
        "#************************************************************************",
        "#",
        f"COMPUTE_SURFACE_SECTIONAL_LOADS {units}"
    ]

    script.append_lines(lines)
    return

def export_surface_sectional_loads(filename):
    """
    Appends lines to script state to export sectional loads on existing surface sections.
    

    :param filename: Filename with path.
    
    Example usage:
    export_surface_sectional_loads('path_to_script_1.txt')
    """
    
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
    

    
    Example usage:
    update_all_surface_sections('path_to_script_2.txt')
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

def export_all_surface_sections(filename):
    """
    Appends lines to script state to export all surface sections to a file.
    

    :param filename: Filename with path for the surface sections.
    
    Example usage:
    export_all_surface_sections(, 'C:/.../Test_surface_sections.txt')
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

def delete_surface_section(index):
    """
    Appends lines to script state to delete a surface section.
    

    :param index: Index of the surface section to be deleted.
    
    Example usage:
    delete_surface_section(, 2)
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
    

    
    Example usage:
        delete_probe_points()
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
