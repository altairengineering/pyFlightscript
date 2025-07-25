from .utils import *    
from .script import script
from .types import *    

def start_solver() -> None:
    """
    Start the solver.

    This function appends a command to the script state to begin the
    solver execution.

    Examples
    --------
    >>> # Start the solver
    >>> start_solver()
    """
    
    lines = [
        "#************************************************************************",
        "#********* Run the solver ***********************************************",
        "#************************************************************************",
        "#",
        "START_SOLVER"
    ]
    
    script.append_lines(lines)
    return

def clear_solution() -> None:
    """
    Clear the existing solution.

    This function appends a command to the script state to clear the
    current solution data.

    Examples
    --------
    >>> # Clear the solution
    >>> clear_solution()
    """
    
    lines = [
        "#************************************************************************",
        "#********* Clear the existing solution **********************************",
        "#************************************************************************",
        "#",
        "CLEAR_SOLUTION"
    ]
    
    script.append_lines(lines)
    return

def close_flightstream() -> None:
    """
    Appends lines to script state to close FlightStream and exit.

    This function appends a command to the script state to close FlightStream
    and exit the application.

    Examples
    --------
    >>> # Close FlightStream and exit
    >>> close_flightstream()
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Close FlightStream and exit *************************",
        "#************************************************************************",
        "#",
        "CLOSE_FLIGHTSTREAM"
    ]

    script.append_lines(lines)
    return
