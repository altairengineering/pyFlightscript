import os
from .utils import *    
from .script import script
from .types import *

def physics(auto_trail_edges=False, auto_wake_nodes=False, end=True):
    """
    Appends lines to script state to set the physics conditions.

    :param auto_trail_edges: If True, launches trailing-edge auto-detection tool.
    :param auto_wake_nodes: If True, launches wake termination node auto-detection tool.
    :param end: If True, adds an "END" line.

    Example usage:
    physics(auto_trail_edges=True, auto_wake_nodes=True)
    """
    
    # List to store the lines
    lines = [
        "#************************************************************************",
        "#****************** Set the physics conditions if needed ****************",
        "#************************************************************************",
        "#",
        "PHYSICS"
    ]

    if auto_trail_edges:
        lines.append("AUTO_TRAIL_EDGES")

    if auto_wake_nodes:
        lines.append("AUTO_WAKE_NODES")

    if end:
        lines.append("END")

    script.append_lines(lines)
    return

def detect_trailing_edges_by_surface(surfaces=[1]):
    """
    Example usage:
    detect_trailing_edges_by_surface(, [2, 4])

    Appends lines to script state to detect trailing edges by surface.

    :param surfaces: List of surface indices to be checked for trailing edge detection.
    """

    # Type and value checking
    if not isinstance(surfaces, list) or not all(isinstance(s, int) for s in surfaces):
        raise ValueError("`surfaces` should be a list of integer values.")

    lines = [
        "#************************************************************************",
        "#****************** Detect Trailing Edges by Surface ********************",
        "#************************************************************************",
        "#",
        "DETECT_TRAILING_EDGES_BY_SURFACE",
        f"SURFACES {len(surfaces)}",
        ",".join(map(str, surfaces))
    ]

    script.append_lines(lines)
    return

def trailing_edges_import(file_path: str):
    """
    Appends lines to script state to import trailing edges from a given file.

    :Example usage:
    trailing_edges_import('C:/.../Custom_TE.txt')
        
    :param file_path: Path to the CSV text file containing the vertices on which the trailing edges are to be marked.

    Sample File Format: 
    10
    MILLIMETER
    1,X1,Y1,Z1
    2,X2,Y2,Z2
    3,X3,Y3,Z3
    ...
    10,X10,Y10,Z10
    
    UNIT_TYPE is one of the following:
    INCH, MILLIMETER, FEET, MILE, METER, KILOMETER, MILS, MICRON, CENTIMETER, MICROINCH
    """
    
    # Type and value checking
    if not isinstance(file_path, str):
        raise ValueError("`file_path` should be a string value.")
    
    # Check if the file path has the correct extension
    if not file_path.lower().endswith('.txt'):
        raise ValueError("`file_path` should end with '.txt'")
    
    lines = [
        "#************************************************************************",
        "#************** Import custom trailing edge marking from file ***********",
        "#************************************************************************",
        "#",
        "TRAILING_EDGES_IMPORT",
        file_path
    ]

    script.append_lines(lines)
    return

def detect_wake_termination_nodes_by_surface(surface_id=1):
    """
    Appends lines to script state to detect wake termination nodes by surface.

    Example usage:
    detect_wake_termination_nodes_by_surface()
    
    :param surface_id: Index of the surface on which the wake termination nodes should be detected.
    """
    
    # Type and value checking
    if not isinstance(surface_id, int):
        raise ValueError("`surface_id` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Detect wake termination nodes by surface ************",
        "#************************************************************************",
        "#",
        f"DETECT_WAKE_TERMINATION_NODES_BY_SURFACE {surface_id}"
    ]

    script.append_lines(lines)
    return
