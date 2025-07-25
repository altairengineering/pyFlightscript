from .utils import *    
from .script import script
from .types import *

def wrapper_set_input(num_surfaces, surface_indices):
    """
    Appends lines to script state to set wrapping input surfaces.
    

    :param num_surfaces: Number of geometry surfaces being used for wrapping.
    :param surface_indices: List of index values of the geometry surfaces to be used for wrapping.
    """
    
    # Type and value checking
    if not isinstance(num_surfaces, int) or num_surfaces <= 0:
        raise ValueError("`num_surfaces` should be a positive integer value.")
    
    if not isinstance(surface_indices, list) or len(surface_indices) != num_surfaces:
        raise ValueError("`surface_indices` should be a list with `num_surfaces` elements.")
    
    if not all(isinstance(val, int) and val > 0 for val in surface_indices):
        raise ValueError("All values in `surface_indices` should be positive integers.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set wrapping input surfaces *************************",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_INPUT {num_surfaces}",
        ",".join(map(str, surface_indices))
    ]

    script.append_lines(lines)
    return

def wrapper_set_global_size(target_size=0.15):
    """
    Appends lines to script state to set wrapping global target size.
    

    :param target_size: Geometry triangle edge length to be used for wrapping.
    """
    
    # Type and value checking
    if not isinstance(target_size, (int, float)):
        raise ValueError("`target_size` should be an integer or float value.")
    
    if target_size <= 0:
        raise ValueError("`target_size` should be greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set wrapping global target size *********************",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_GLOBAL_SIZE {target_size}"
    ]

    script.append_lines(lines)
    return

def wrapper_set_vertex_projection(state='ENABLE'):
    """
    Appends lines to script state to enable or disable wrapping vertex projection.
    

    :param state: State of wrapping vertex projection, can be either 'ENABLE' or 'DISABLE'.
    """
    
    # Type and value checking
    valid_states = ['ENABLE', 'DISABLE']
    if state not in valid_states:
        raise ValueError(f"`state` should be one of {valid_states}")
    
    lines = [
        "#************************************************************************",
        "#****************** Enable/disable wrapping vertex projection ***********",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_VERTEX_PROJECTION {state}"
    ]

    script.append_lines(lines)
    return

def wrapper_set_anisotropy(x=2, y=1, z=1):
    """
    Appends lines to script state to set wrapping anisotropy.
    

    :param x: Wrapper anisotropy in X direction.
    :param y: Wrapper anisotropy in Y direction.
    :param z: Wrapper anisotropy in Z direction.
    """
    
    # Type and value checking
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise ValueError("The values of x, y, and z should be integers or floats.")
    
    if not all(val > 0 for val in [x, y, z]):
        raise ValueError("The values of x, y, and z should be greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set wrapping anisotropy *****************************",
        "#************************************************************************",
        "#",
        f"WRAPPER_SET_ANISOTROPY {x} {y} {z}"
    ]

    script.append_lines(lines)
    return

def wrapper_create_local_control():
    """
    Appends lines to script state to create a new wrapping local control.
    

    """
    
    lines = [
        "#************************************************************************",
        "#****************** Create new wrapping local control *******************",
        "#************************************************************************",
        "#",
        "WRAPPER_CREATE_LOCAL_CONTROL"
    ]

    script.append_lines(lines)
    return

def wrapper_edit_local_control(control_id, surfaces, target_size):
    """
    Appends lines to script state to edit wrapping local control.


    :param control_id: ID of the local control being edited.
    :param surfaces: List of surfaces being added to the local control.
    :param target_size: Geometry triangle edge length to be used for wrapping.
    """
    
    # Type and value checking
    if not isinstance(control_id, int) or control_id <= 0:
        raise ValueError("`control_id` should be an integer value greater than 0.")
    
    if not isinstance(surfaces, list) or not all(isinstance(s, int) and s > 0 for s in surfaces):
        raise ValueError("`surfaces` should be a list of integer values greater than 0.")
    
    if not isinstance(target_size, (int, float)) or target_size <= 0:
        raise ValueError("`target_size` should be a positive integer or float value.")
    
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
    return

def wrapper_delete_all_local_controls():
    """
    Appends lines to script state to delete all wrapper surface controls.
    

    """
    
    lines = [
        "#************************************************************************",
        "#****************** Delete all wrapper surface controls *****************",
        "#************************************************************************",
        "#",
        "WRAPPER_DELETE_ALL_LOCAL_CONTROLS"
    ]

    script.append_lines(lines)
    return

def wrapper_new_volume_control(frame=1, vertex_1=(0.5, 0.3, 1.0), 
                               vertex_2=(1.5, 0.6, 2.3), target_size=0.25, 
                               name="Airplane_nose"):
    """
    Appends lines to script state to create a new wrapping volume control.
    

    :param frame: Coordinate system ID used for creating the volume control box.
    :param vertex_1: X,Y,Z values of the first corner of the volume box.
    :param vertex_2: X,Y,Z values of the second corner of the volume box.
    :param target_size: Triangle edge length used for wrapping by this local control.
    :param name: Name of the volume control.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if not isinstance(vertex_1, tuple) or len(vertex_1) != 3:
        raise ValueError("`vertex_1` should be a tuple of three numerical values.")
    
    if not isinstance(vertex_2, tuple) or len(vertex_2) != 3:
        raise ValueError("`vertex_2` should be a tuple of three numerical values.")
    
    if not isinstance(target_size, (int, float)) or target_size <= 0:
        raise ValueError("`target_size` should be a positive numerical value.")
    
    if not isinstance(name, str):
        raise ValueError("`name` should be a string value.")
    
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
        f"NAME {name}"
    ]

    script.append_lines(lines)
    return

def wrapper_delete_all_volume_controls():
    """
    Appends lines to script state to delete all wrapper volume controls.
    

    """
    
    lines = [
        "#************************************************************************",
        "#****************** Delete all wrapper volume controls ******************",
        "#************************************************************************",
        "#",
        "WRAPPER_DELETE_ALL_VOLUME_CONTROLS"
    ]

    script.append_lines(lines)
    return

def wrapper_execute():
    """
    Appends lines to script state to execute the geometry wrapping operation.
    

    """
    
    lines = [
        "#************************************************************************",
        "#****************** Execute the geometry wrapping operation *************",
        "#************************************************************************",
        "#",
        "WRAPPER_EXECUTE"
    ]

    script.append_lines(lines)
    return

def wrapper_transfer(source_treatment='REPLACE'):
    """
    Appends lines to script state to transfer the wrapped geometry output.
    

    :param source_treatment: Option to either delete/replace the original wrapper source 
                             geometries or retain them.
    """
    
    # Type and value checking
    valid_treatments = ['REPLACE', 'RETAIN']
    if source_treatment not in valid_treatments:
        raise ValueError(f"`source_treatment` should be one of {valid_treatments}")
    
    lines = [
        "#************************************************************************",
        "#****************** Transfer the wrapped geometry output ****************",
        "#************************************************************************",
        "#",
        f"WRAPPER_TRANSFER {source_treatment}"
    ]

    script.append_lines(lines)
    return


