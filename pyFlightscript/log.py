from .utils import *    
from .script import script

def clear():
    """
    Appends lines to script state to clear the log.
    
    Example usage:
    clear_log()
    """
    
    lines = ["CLEAR_LOG"]
    script.append_lines(lines)
    return


def output_settings_and_status(output_filename):
    """
    Appends lines to script state to output fluid properties and solver status.
    
    Args:
        output_filename (str): Path to the output file.
    
    Example usage:
    output_settings_and_status('C:/path/to/output.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#************** Output fluid properties and solver status ***************",
        "#************************************************************************",
        "#",
        "OUTPUT_SETTINGS_AND_STATUS",
        output_filename
    ]
    
    script.append_lines(lines)
    return
    
def export(log_filepath):
    """
    Appends lines to script state to export log window messages.
    

    :param log_filepath: Path to the output log file.
    
    Example usage:
    export_log(, 'C:/.../Output_log.txt')
    """

    lines = [
        "#************************************************************************",
        "#****************** Export log window messages to file ******************",
        "#************************************************************************",
        "#",
        "EXPORT_LOG",
        log_filepath
    ]
    
    script.append_lines(lines)
    return

