from .utils import *    
from .script import script
from .types import *

def set_plot_type(plot_type):
    """
    Appends lines to script state to change the plot type.
    

    :param plot_type: Type of plot.
    
    Example usage:
    set_plot_type(, 'FORCE_Z_AXIS_Y')
    """
    valid_plot_types = [
        'CL_AXIS_X', 'CL_AXIS_Y', 'CL_AXIS_Z', 'CDI_AXIS_X', 'CDI_AXIS_Y',
        'CDI_AXIS_Z', 'CY_AXIS_X', 'CY_AXIS_Y', 'CY_AXIS_Z', 'FORCE_X_AXIS_X',
        'FORCE_X_AXIS_Y', 'FORCE_X_AXIS_Z', 'FORCE_Y_AXIS_X', 'FORCE_Y_AXIS_Y',
        'FORCE_Y_AXIS_Z', 'FORCE_Z_AXIS_X', 'FORCE_Z_AXIS_Y', 'FORCE_Z_AXIS_Z',
        'RESIDUALS', 'LOADS', 'SECTIONS_CP', 'SECTIONS_MACH', 'UNSTEADY'
    ]
    
    if plot_type not in valid_plot_types:
        raise ValueError(f"`plot_type` should be one of {valid_plot_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Change the plot type ********************************",
        "#************************************************************************",
        "#",
        "SET_PLOT_TYPE",
        plot_type
    ]
    script.append_lines(lines)
    return

def save_plot_to_file(filename):
    """
    Appends lines to script state to save the plot to an external file.
    

    :param filename: Full path and name of the file to save the plot.
    
    Example usage:
    save_plot_to_file(, 'C:/.../Test_Plot.txt')
    """
    lines = [
        "#************************************************************************",
        "#****************** Save scene as image file ****************************",
        "#************************************************************************",
        "SAVE_PLOT_TO_FILE",
        filename
    ]
    script.append_lines(lines)
    return