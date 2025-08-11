from .utils import *    
from .script import script
from .types import *

from typing import List
from .script import script

def wrapper_set_input(num_surfaces: int, surface_indices: List[int]) -> None:
    """
    Set the input surfaces for the wrapping operation.

    This function appends a command to the script state to define which
    geometry surfaces will be used for the wrapping process.

    Parameters
    ----------
    num_surfaces : int
        The number of geometry surfaces to be used for wrapping.
    surface_indices : List[int]
        A list of the index values for the geometry surfaces.

    Examples
    --------
    >>> # Set three surfaces (indices 1, 2, 5) as input for wrapping
    >>> wrapper_set_input(3, [1, 2, 5])
    """
    if not isinstance(num_surfaces, int) or num_surfaces <= 0:
        raise ValueError("`num_surfaces` must be a positive integer.")
    
    if not isinstance(surface_indices, list) or len(surface_indices) != num_surfaces:
        raise ValueError("`surface_indices` must be a list with a length equal to `num_surfaces`.")
    
    if not all(isinstance(val, int) and val > 0 for val in surface_indices):
        raise ValueError("All `surface_indices` must be positive integers.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set wrapping input surfaces *************************",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_INPUT {num_surfaces}",
        ",".join(map(str, surface_indices))
    ]

    script.append_lines(lines)

def wrapper_set_global_size(target_size: float = 0.15) -> None:
    """
    Set the global target size for the wrapping operation.

    This function appends a command to the script state to define the global
    target edge length for the triangles in the wrapped geometry.

    Parameters
    ----------
    target_size : float, optional
        The target triangle edge length for the wrapping process, by default 0.15.

    Examples
    --------
    >>> # Set the global target size for wrapping to 0.2
    >>> wrapper_set_global_size(0.2)

    >>> # Use the default global target size
    >>> wrapper_set_global_size()
    """
    if not isinstance(target_size, (int, float)):
        raise ValueError("`target_size` must be a numeric value.")
    
    if target_size <= 0:
        raise ValueError("`target_size` must be greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set wrapping global target size *********************",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_GLOBAL_SIZE {target_size}"
    ]

    script.append_lines(lines)

from .types import RunOptions

def wrapper_set_vertex_projection(state: RunOptions = 'ENABLE') -> None:
    """
    Enable or disable wrapping vertex projection.

    This function appends a command to the script state to control whether
    vertex projection is enabled or disabled during the wrapping process.

    Parameters
    ----------
    state : RunOptions, optional
        The state of the vertex projection, either 'ENABLE' or 'DISABLE', 
        by default 'ENABLE'.

    Examples
    --------
    >>> # Disable wrapping vertex projection
    >>> wrapper_set_vertex_projection('DISABLE')

    >>> # Enable wrapping vertex projection
    >>> wrapper_set_vertex_projection('ENABLE')
    """
    if state not in ('ENABLE', 'DISABLE'):
        raise ValueError("`state` must be either 'ENABLE' or 'DISABLE'.")
    
    lines = [
        "#************************************************************************",
        "#****************** Enable/disable wrapping vertex projection ***********",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_VERTEX_PROJECTION {state}"
    ]

    script.append_lines(lines)

def wrapper_set_anisotropy(x: float = 2.0, y: float = 1.0, z: float = 1.0) -> None:
    """
    Set the wrapping anisotropy.

    This function appends a command to the script state to define the
    anisotropy for the wrapping process in the X, Y, and Z directions.

    Parameters
    ----------
    x : float, optional
        The wrapper anisotropy in the X direction, by default 2.0.
    y : float, optional
        The wrapper anisotropy in the Y direction, by default 1.0.
    z : float, optional
        The wrapper anisotropy in the Z direction, by default 1.0.

    Examples
    --------
    >>> # Set custom wrapping anisotropy
    >>> wrapper_set_anisotropy(x=3.0, y=1.5, z=1.5)

    >>> # Use default wrapping anisotropy
    >>> wrapper_set_anisotropy()
    """
    if not all(isinstance(val, (int, float)) and val > 0 for val in [x, y, z]):
        raise ValueError("Anisotropy values for x, y, and z must be positive numbers.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set wrapping anisotropy *****************************",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_ANISOTROPY {x} {y} {z}"
    ]

    script.append_lines(lines)

def wrapper_create_local_control() -> None:
    """
    Create a new wrapping local control.

    This function appends a command to the script state to create a new local
    control for the wrapping process. This allows for defining specific
    meshing parameters on different parts of the geometry.

    Examples
    --------
    >>> # Create a new local control for wrapping
    >>> wrapper_create_local_control()
    """
    lines = [
        "#************************************************************************",
        "#****************** Create new wrapping local control *******************",
        "#************************************************************************",
        "#",
        "WRAPPER_CREATE_LOCAL_CONTROL"
    ]
    script.append_lines(lines)

def wrapper_edit_local_control(
    control_id: int, 
    surfaces: List[int], 
    target_size: float
) -> None:
    """
    Edit a wrapping local control.

    This function appends a command to the script state to modify an existing
    local control by specifying the surfaces it applies to and the target
    triangle edge length.

    Parameters
    ----------
    control_id : int
        The ID of the local control to be edited.
    surfaces : List[int]
        A list of surface indices to be added to the local control.
    target_size : float
        The target triangle edge length for this local control.

    Examples
    --------
    >>> # Edit local control 1 to apply to surfaces 3 and 4 with a target size of 0.1
    >>> wrapper_edit_local_control(1, [3, 4], 0.1)
    """
    if not isinstance(control_id, int) or control_id <= 0:
        raise ValueError("`control_id` must be a positive integer.")
    
    if not isinstance(surfaces, list) or not all(isinstance(s, int) and s > 0 for s in surfaces):
        raise ValueError("`surfaces` must be a list of positive integers.")
    
    if not isinstance(target_size, (int, float)) or target_size <= 0:
        raise ValueError("`target_size` must be a positive number.")
    
    lines = [
        "#************************************************************************",
        "#****************** Edit wrapping local control *************************",
        "#************************************************************************",
        "#",
        f"WRAPPER_EDIT_LOCAL_CONTROL {control_id}",
        f"SURFACES {len(surfaces)}",
        ",".join(map(str, surfaces)),
        f"TARGET_SIZE {target_size}"
    ]
    script.append_lines(lines)

from typing import Tuple

def wrapper_delete_all_local_controls() -> None:
    """
    Delete all wrapper surface controls.

    This function appends a command to the script state to remove all
    existing local controls defined for the wrapping process.

    Examples
    --------
    >>> # Delete all local wrapping controls
    >>> wrapper_delete_all_local_controls()
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all wrapper surface controls *****************",
        "#************************************************************************",
        "#",
        "WRAPPER_DELETE_ALL_LOCAL_CONTROLS"
    ]
    script.append_lines(lines)

def wrapper_new_volume_control(
    frame: int = 1, 
    vertex_1: Tuple[float, float, float] = (0.5, 0.3, 1.0), 
    vertex_2: Tuple[float, float, float] = (1.5, 0.6, 2.3), 
    target_size: float = 0.25, 
    name: str = "Airplane_nose"
) -> None:
    """
    Create a new wrapping volume control.

    This function appends a command to the script state to create a new
    volume control box for the wrapping process. This allows for refining
    the mesh size within a specified volume.

    Parameters
    ----------
    frame : int, optional
        The coordinate system ID for the volume control box, by default 1.
    vertex_1 : Tuple[float, float, float], optional
        The (X, Y, Z) coordinates of the first corner of the volume box, 
        by default (0.5, 0.3, 1.0).
    vertex_2 : Tuple[float, float, float], optional
        The (X, Y, Z) coordinates of the second corner of the volume box, 
        by default (1.5, 0.6, 2.3).
    target_size : float, optional
        The target triangle edge length for this volume control, by default 0.25.
    name : str, optional
        The name of the volume control, by default "Airplane_nose".

    Examples
    --------
    >>> # Create a new volume control with custom parameters
    >>> wrapper_new_volume_control(
    ...     frame=2, 
    ...     vertex_1=(0.0, 0.0, 0.0), 
    ...     vertex_2=(1.0, 1.0, 1.0), 
    ...     target_size=0.1, 
    ...     name="wing_box"
    ... )
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` must be an integer.")
    
    if not (isinstance(vertex_1, tuple) and len(vertex_1) == 3 and all(isinstance(v, (int, float)) for v in vertex_1)):
        raise ValueError("`vertex_1` must be a tuple of three numbers.")
        
    if not (isinstance(vertex_2, tuple) and len(vertex_2) == 3 and all(isinstance(v, (int, float)) for v in vertex_2)):
        raise ValueError("`vertex_2` must be a tuple of three numbers.")
    
    if not isinstance(target_size, (int, float)) or target_size <= 0:
        raise ValueError("`target_size` must be a positive number.")
    
    if not isinstance(name, str):
        raise ValueError("`name` must be a string.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create new wrapping volume control ******************",
        "#************************************************************************",
        "#",
        "WRAPPER_NEW_VOLUME_CONTROL",
        f"FRAME {frame}",
        f"VERTEX_1 {' '.join(map(str, vertex_1))}",
        f"VERTEX_2 {' '.join(map(str, vertex_2))}",
        f"TARGET_SIZE {target_size}",
        f'NAME "{name}"'
    ]
    script.append_lines(lines)

def wrapper_delete_all_volume_controls() -> None:
    """
    Delete all wrapper volume controls.

    This function appends a command to the script state to remove all
    existing volume controls defined for the wrapping process.

    Examples
    --------
    >>> # Delete all volume wrapping controls
    >>> wrapper_delete_all_volume_controls()
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all wrapper volume controls ******************",
        "#************************************************************************",
        "#",
        "WRAPPER_DELETE_ALL_VOLUME_CONTROLS"
    ]
    script.append_lines(lines)

def wrapper_execute() -> None:
    """
    Execute the geometry wrapping operation.

    This function appends a command to the script state to initiate the
    geometry wrapping process based on the previously defined settings.

    Examples
    --------
    >>> # Execute the wrapping operation
    >>> wrapper_execute()
    """
    lines = [
        "#************************************************************************",
        "#****************** Execute the geometry wrapping operation *************",
        "#************************************************************************",
        "#",
        "WRAPPER_EXECUTE"
    ]
    script.append_lines(lines)

from typing import Literal

def wrapper_transfer(source_treatment: Literal['REPLACE', 'RETAIN'] = 'REPLACE') -> None:
    """
    Transfer the wrapped geometry output.

    This function appends a command to the script state to handle the output
    of the wrapping operation, with an option to either replace the original
    source geometries or retain them.

    Parameters
    ----------
    source_treatment : Literal['REPLACE', 'RETAIN'], optional
        Defines how to treat the original source geometries after wrapping.
        'REPLACE' deletes the original, while 'RETAIN' keeps it. 
        By default 'REPLACE'.

    Examples
    --------
    >>> # Transfer wrapped geometry and retain the original source
    >>> wrapper_transfer(source_treatment='RETAIN')

    >>> # Transfer wrapped geometry and replace the original source
    >>> wrapper_transfer('REPLACE')
    """
    if source_treatment not in ('REPLACE', 'RETAIN'):
        raise ValueError("`source_treatment` must be either 'REPLACE' or 'RETAIN'.")
    
    lines = [
        "#************************************************************************",
        "#****************** Transfer the wrapped geometry output ****************",
        "#************************************************************************",
        "#",
        f"WRAPPER_TRANSFER {source_treatment}"
    ]
    script.append_lines(lines)


