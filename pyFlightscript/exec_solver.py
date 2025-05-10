from .utils import *    
from .script import script    

def start_solver():
    """
    Appends lines to script state to start the solver.
    


    Example usage:
    start_solver()
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

def clear_solution():
    """
    Appends lines to script state to clear the existing solution.
    


    Example usage:
    clear_solution()
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

def close_flightstream():
    """
    Appends lines to script state to close FlightStream and exit.



    Example usage:
        close_flightstream()
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
