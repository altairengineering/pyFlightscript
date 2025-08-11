from . import script
from .types import VALID_PLOT_TYPE_LIST

def set_plot_type(plot_type: str) -> None:
    """
    Set the type of plot to be displayed.

    This function appends a command to the script state to change the plot type.

    Parameters
    ----------
    plot_type : str
        The type of plot to be generated. Must be one of `VALID_PLOT_TYPE_LIST`.

    Examples
    --------
    >>> # Set the plot type to display lift coefficient vs. angle of attack
    >>> set_plot_type('CL_AXIS_X')

    >>> # Set the plot type to display unsteady forces
    >>> set_plot_type('UNSTEADY')
    """
    if plot_type not in VALID_PLOT_TYPE_LIST:
        raise ValueError(f"`plot_type` should be one of {VALID_PLOT_TYPE_LIST}")
    
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

def save_plot_to_file(filename: str) -> None:
    """
    Save the current plot to a file.

    This function appends a command to the script state to save the plot to an
    external file. The format is determined by the file extension.

    Parameters
    ----------
    filename : str
        The full path and name of the file to save the plot.

    Examples
    --------
    >>> # Save the plot to a text file
    >>> save_plot_to_file('C:/Users/user/Documents/Test_Plot.txt')

    >>> # Save the plot to a different location
    >>> save_plot_to_file('D:/Analysis/Results/force_plot.dat')
    """
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string.")

    lines = [
        "#************************************************************************",
        "#****************** Save plot to file ***********************************",
        "#************************************************************************",
        "SAVE_PLOT_TO_FILE",
        filename
    ]
    script.append_lines(lines)
    return
