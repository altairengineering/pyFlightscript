import os
from .utils import *    
from .script import script
from .types import *

from typing import List, Tuple, Literal
from .script import script

# Define a type for volume options
VolumeType = Literal['POSITIVE', 'NEGATIVE']

def boolean_unite_mesh(
    num_bodies: int, 
    bodies_info: List[Tuple[int, VolumeType]] = None
) -> None:
    """
    Unite mesh bodies, either selectively or all bodies with positive volume.

    This function appends a command to the script state to unite mesh bodies.
    It can unite a specified number of bodies with given volume types or unite
    all bodies that have a positive volume.

    Parameters
    ----------
    num_bodies : int
        The number of mesh bodies to unite. If -1, all bodies with a positive
        unite volume are targeted.
    bodies_info : List[Tuple[int, VolumeType]], optional
        A list of tuples, where each tuple contains the body's index and its
        volume type ('POSITIVE' or 'NEGATIVE'). This is required if `num_bodies`
        is not -1.

    Examples
    --------
    >>> # Unite all mesh bodies with a positive volume
    >>> boolean_unite_mesh(-1)

    >>> # Unite specific mesh bodies with defined volume types
    >>> bodies_to_unite = [(1, 'POSITIVE'), (2, 'NEGATIVE')]
    >>> boolean_unite_mesh(2, bodies_to_unite)
    """
    lines = [
        "#************************************************************************",
        "#************* Unite a selection of mesh bodies *************************",
        "#************************************************************************",
    ]
    
    if num_bodies == -1:
        lines.append("BOOLEAN_UNITE_MESH -1")
    else:
        if not isinstance(num_bodies, int):
            raise ValueError("`num_bodies` should be an integer.")
        
        if bodies_info is None:
            raise ValueError("`bodies_info` must be provided when `num_bodies` is not -1.")
        
        if not all(isinstance(body, tuple) and len(body) == 2 for body in bodies_info):
            raise ValueError("`bodies_info` must be a list of tuples, each with an index and volume type.")
        
        if len(bodies_info) != num_bodies:
            raise ValueError("The length of `bodies_info` must match `num_bodies`.")

        lines.append(f"BOOLEAN_UNITE_MESH {num_bodies}")
        for index, volume_type in bodies_info:
            if not isinstance(index, int) or volume_type not in ('POSITIVE', 'NEGATIVE'):
                raise ValueError("Each body must have an integer index and a volume type of 'POSITIVE' or 'NEGATIVE'.")
            lines.append(f"{index} {volume_type.upper()}")
    
    script.append_lines(lines)

def boolean_unite_path(openvsp_path: str) -> None:
    """
    Set the path to the OpenVSP executable for the CompGeom unite function.

    This function appends a command to the script state to specify the file
    path for the OpenVSP executable, which is used in the unite operations.

    Parameters
    ----------
    openvsp_path : str
        The file path to the OpenVSP executable.

    Examples
    --------
    >>> # Set the OpenVSP path for the unite function
    >>> boolean_unite_path("C:/path/to/openvsp.exe")
    """
    if not isinstance(openvsp_path, str) or not openvsp_path:
        raise ValueError("`openvsp_path` must be a non-empty string.")

    lines = [
        "#************************************************************************",
        "#************* Specify the OpenVSP path for the Unite function **********",
        "#************************************************************************",
        "BOOLEAN_UNITE_PATH",
        f'OPENVSP_PATH "{openvsp_path}"'
    ]

    script.append_lines(lines)

def boolean_unite_geometry(
    bodies: int, 
    openvsp_path: str, 
    bodies_values: List[Tuple[int, VolumeType]] = None
) -> None:
    """
    Boolean unite a selection of geometry bodies.

    This function appends a command to the script state to perform a Boolean
    unite operation on a selection of geometry bodies. It requires specifying
    the number of bodies, their volume types, and the path to the OpenVSP
    executable.

    Parameters
    ----------
    bodies : int
        The number of geometry bodies to be Boolean-united. Use -1 to specify all.
    openvsp_path : str
        The path to the OpenVSP executable used for the CompGeom unite function.
    bodies_values : List[Tuple[int, VolumeType]], optional
        A list of tuples, each containing the index of a geometry surface and
        its volume type ('POSITIVE' or 'NEGATIVE'). Required if `bodies` is not -1.

    Examples
    --------
    >>> # Unite all geometry bodies
    >>> boolean_unite_geometry(-1, "C:/path/to/openvsp.exe")

    >>> # Unite a specific selection of geometry bodies
    >>> body_values = [(1, 'POSITIVE'), (2, 'NEGATIVE'), (3, 'POSITIVE')]
    >>> boolean_unite_geometry(3, "C:/path/to/openvsp.exe", body_values)
    """
    if not isinstance(bodies, int):
        raise ValueError("`bodies` must be an integer.")
    
    if not isinstance(openvsp_path, str) or not openvsp_path:
        raise ValueError("`openvsp_path` must be a non-empty string.")

    if bodies != -1:
        if bodies_values is None:
            raise ValueError("`bodies_values` must be provided when `bodies` is not -1.")
        
        if len(bodies_values) != bodies:
            raise ValueError("The length of `bodies_values` must match `bodies`.")
        
        for item in bodies_values:
            if not (isinstance(item, tuple) and len(item) == 2 and
                    isinstance(item[0], int) and item[1] in ('POSITIVE', 'NEGATIVE')):
                raise ValueError("Each item in `bodies_values` must be a tuple of (index, 'POSITIVE'/'NEGATIVE').")

    lines = [
        "#************************************************************************",
        "#************* Boolean unite a selection of geometry bodies *************",
        "#************************************************************************",
        "#",
        "BOOLEAN_UNITE_GEOMETRY",
        f"BODIES {bodies}"
    ]

    if bodies_values:
        for index, volume_type in bodies_values:
            lines.append(f"{index} {volume_type}")

    lines.append(f'OPENVSP_PATH "{openvsp_path}"')

    script.append_lines(lines)


