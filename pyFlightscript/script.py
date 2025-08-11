from typing import List, Union, Optional
import os
import subprocess

class State:
    """
    Manages the state of the FlightStream script being generated.
    """
    def __init__(self) -> None:
        """
        Initializes the State object with an empty list of lines.
        """
        self.lines: List[str] = []

    def append_lines(self, lines: Union[str, List[str]]) -> None:
        """
        Append lines to the existing script.

        Parameters
        ----------
        lines : Union[str, List[str]]
            A single line or a list of lines to be appended to the script.
        """
        if isinstance(lines, str):
            self.lines.append(lines)
        elif isinstance(lines, list):
            self.lines.extend(lines)

    def display_lines(self) -> None:
        """
        Print each line stored in the script to the console.
        """
        for line in self.lines:
            print(line)

    def write_to_file(self, filename: str = "script_out.txt") -> None:
        """
        Write the script content to a file for use in FlightStream.

        Parameters
        ----------
        filename : str, optional
            The name of the file to write to, by default "script_out.txt".
        """
        with open(filename, 'w') as file:
            for line in self.lines:
                file.write(line + '\n')
            file.write('\n')

    def clear_lines(self) -> None:
        """
        Clear all lines from the current script state.
        """
        self.lines = []

# Create a global instance of State to hold the script lines
script = State()

def display_lines() -> None:
    """
    Print each line stored in the global script state to the console.
    """
    script.display_lines()

def write_to_file(filename: str = "script_out.txt") -> None:
    """
    Write the global script content to a file.

    Parameters
    ----------
    filename : str, optional
        The name of the file to write to, by default "script_out.txt".
    """
    script.write_to_file(filename)
    print(f"pyscript lines written to: {filename}")

def clear_lines() -> None:
    """
    Clear all lines from the global script state.
    """
    script.clear_lines()
    print("pyscript lines cleared")

def hard_reset(filename: str = "script_out.txt") -> None:
    """
    Reset the script and delete the specified output file.

    This function clears all lines from the script and removes the output file
    from the filesystem if it exists.

    Parameters
    ----------
    filename : str, optional
        The name of the output file to delete, by default "script_out.txt".
    """
    script.clear_lines()
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}")

def run_script(
    fsexe_path: str,
    script_path: str = r'.\script_out.txt',
    hidden: bool = False
) -> subprocess.CompletedProcess:
    """
    Run a script using the FlightStream executable.

    Parameters
    ----------
    fsexe_path : str
        The path to the FlightStream executable.
    script_path : str, optional
        The path to the script file to run, by default r'.\script_out.txt'.
    hidden : bool, optional
        If True, runs FlightStream in hidden mode, by default False.

    Returns
    -------
    subprocess.CompletedProcess
        The result of the subprocess run command.
    """
    command = [fsexe_path]
    if hidden:
        command.append('-hidden')
    command.extend(['-script', script_path])
    result = subprocess.run(command, capture_output=True, text=True)
    return result
