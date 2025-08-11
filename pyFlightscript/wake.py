import os
from .utils import *    
from .script import script
from .types import *

from typing import List
from .script import script

def physics(
    auto_trail_edges: bool = False, 
    auto_wake_nodes: bool = False, 
    end: bool = True
) -> None:
    """
    Set the physics conditions for the simulation.

    This function appends a command to the script state to define the physics
    conditions, with options to enable auto-detection for trailing edges and
    wake termination nodes.

    Parameters
    ----------
    auto_trail_edges : bool, optional
        If True, launches the trailing-edge auto-detection tool, by default False.
    auto_wake_nodes : bool, optional
        If True, launches the wake termination node auto-detection tool, by default False.
    end : bool, optional
        If True, adds an "END" line to conclude the physics definition, by default True.

    Examples
    --------
    >>> # Enable auto-detection for trailing edges and wake nodes
    >>> physics(auto_trail_edges=True, auto_wake_nodes=True)

    >>> # Set physics conditions without auto-detection
    >>> physics()
    """
    if not all(isinstance(arg, bool) for arg in [auto_trail_edges, auto_wake_nodes, end]):
        raise ValueError("All arguments must be boolean values.")

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

def detect_trailing_edges_by_surface(surfaces: List[int]) -> None:
    """
    Detect trailing edges for a given list of surfaces.

    This function appends a command to the script state to initiate trailing
    edge detection on the specified surfaces.

    Parameters
    ----------
    surfaces : List[int]
        A list of surface indices for which trailing edges are to be detected.

    Examples
    --------
    >>> # Detect trailing edges on surfaces 1, 2, and 5
    >>> detect_trailing_edges_by_surface([1, 2, 5])

    >>> # Detect trailing edges on a single surface
    >>> detect_trailing_edges_by_surface([3])
    """
    if not isinstance(surfaces, list) or not all(isinstance(s, int) for s in surfaces):
        raise ValueError("`surfaces` must be a list of integers.")

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

def trailing_edges_import(file_path: str) -> None:
    """
    Import trailing edges from a specified file.

    This function appends a command to the script state to import trailing
    edges from a text file. The file should contain the vertices where
    trailing edges are to be marked.

    Parameters
    ----------
    file_path : str
        The path to the .txt file containing the trailing edge vertices.

    Examples
    --------
    >>> # Import trailing edges from a custom file
    >>> trailing_edges_import('C:/data/custom_trailing_edges.txt')

    Notes
    -----
    The file format should be as follows:
    <number_of_vertices>
    <UNIT_TYPE>
    1,X1,Y1,Z1
    2,X2,Y2,Z2
    ...

    UNIT_TYPE can be one of: INCH, MILLIMETER, FEET, MILE, METER, KILOMETER,
    MILS, MICRON, CENTIMETER, MICROINCH.
    """
    if not isinstance(file_path, str):
        raise ValueError("`file_path` must be a string.")
    
    if not file_path.lower().endswith('.txt'):
        raise ValueError("`file_path` must be a .txt file.")
    
    lines = [
        "#************************************************************************",
        "#************** Import custom trailing edge marking from file ***********",
        "#************************************************************************",
        "#",
        "TRAILING_EDGES_IMPORT",
        f'"{file_path}"'
    ]

    script.append_lines(lines)

def detect_wake_termination_nodes_by_surface(surface_id: int) -> None:
    """
    Detect wake termination nodes on a specified surface.

    This function appends a command to the script state to detect wake
    termination nodes on a given surface index.

    Parameters
    ----------
    surface_id : int
        The index of the surface for wake termination node detection.

    Examples
    --------
    >>> # Detect wake termination nodes on surface 3
    >>> detect_wake_termination_nodes_by_surface(3)
    """
    if not isinstance(surface_id, int):
        raise ValueError("`surface_id` must be an integer.")
    
    lines = [
        "#************************************************************************",
        "#****************** Detect wake termination nodes by surface ************",
        "#************************************************************************",
        "#",
        f"DETECT_WAKE_TERMINATION_NODES_BY_SURFACE {surface_id}"
    ]

    script.append_lines(lines)
