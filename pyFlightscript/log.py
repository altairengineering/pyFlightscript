from .script import script

def clear_log() -> None:
    """
    Clear the log.

    This function appends a command to the script state to clear the log.

    Examples
    --------
    >>> clear_log()
    """
    
    lines = ["CLEAR_LOG"]
    script.append_lines(lines)
    return


def output_settings_and_status(output_filename: str) -> None:
    """
    Output fluid properties and solver status.

    This function appends a command to the script state to output fluid
    properties and solver status to a specified file.

    Parameters
    ----------
    output_filename : str
        Path to the output file.

    Examples
    --------
    >>> output_settings_and_status('C:/path/to/output.txt')
    """
    if not isinstance(output_filename, str):
        raise TypeError("`output_filename` must be a string.")

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


def export_log(log_filepath: str) -> None:
    """
    Export log window messages.

    This function appends a command to the script state to export log window
    messages to a specified file.

    Parameters
    ----------
    log_filepath : str
        Path to the output log file.

    Examples
    --------
    >>> export_log('C:/.../Output_log.txt')
    """
    if not isinstance(log_filepath, str):
        raise TypeError("`log_filepath` must be a string.")

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

