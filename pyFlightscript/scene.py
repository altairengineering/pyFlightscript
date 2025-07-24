from .utils import *    
from .script import script

def view_resize() -> None:
    """
    Resize the view in the scene.

    This function appends a command to the script state to resize the view,
    which may be useful after changing the window size or layout.

    Examples
    --------
    >>> # Resize the scene view
    >>> view_resize()
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Resizing the view in the scene **********************",
        "#************************************************************************",
        "#",
        "VIEW_RESIZE"
    ]

    script.append_lines(lines)
    return

def change_scene_to(scene):
    """
    Appends lines to script state to change the scene.
    

    :param scene: string to change the scene. Must be one of CAD, GEOMETRY, SOLVER, PLOTS
    
    Example usage:
    change_scene_to(, 'CAD')
    """

    valid_options = ["CAD", "GEOMETRY", "SOLVER", "PLOTS"]
    if scene not in valid_options:
        raise ValueError(f"Invalid scene: {scene}. Must be one of {', '.join(valid_options)}.")
    
    lines = [
        "#************************************************************************",
        "#************************ Change the Scene To ***************************",
        "#************************************************************************",
        "#",
        f"CHANGE_SCENE_TO_{scene}"
    ]

    script.append_lines(lines)
    return

def save_scene_as_image(filename):
    """
    Appends a command to the script to save the current scene as an image file.

    :param filename: The full path with the filename where the image will be saved.
    """
    
    # Validate the filename
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string representing the file path.")
    
    if not filename.endswith(('.bmp', '.png', '.jpg', '.jpeg', '.tiff', '.gif')):
        raise ValueError("The filename must end with a valid image file extension (.bmp, .png, .jpg, .jpeg, .tiff, .gif).")
    
    lines = [
        "#************************************************************************",
        "#****************** Save scene as image file ****************************",
        "#************************************************************************",
        "#",
        "SAVE_SCENE_AS_IMAGE",
        filename
    ]

    script.append_lines(lines)
    return

def set_scene_view(view_option='DEFAULTVIEW'):
    """
    Appends lines to script state to set the scene view.
    

    :param view_option: Option for the view which can be one of the following:
                        'DEFAULTVIEW', 'XY_POSITIVE', 'XY_NEGATIVE', 
                        'XZ_POSITIVE', 'XZ_NEGATIVE', 'YZ_POSITIVE', 'YZ_NEGATIVE'
                        
    Example Usage:
    set_scene_view(, 'DEFAULTVIEW')
    set_scene_view(, 'XY_NEGATIVE')
    """
    
    # Define a dictionary to match the view_option to the appropriate function name
    view_commands = {
        'DEFAULTVIEW': 'SET_SCENE_DEFAULTVIEW',
        'XY_POSITIVE': 'SET_SCENE_XY_POSITIVE',
        'XY_NEGATIVE': 'SET_SCENE_XY_NEGATIVE',
        'XZ_POSITIVE': 'SET_SCENE_XZ_POSITIVE',
        'XZ_NEGATIVE': 'SET_SCENE_XZ_NEGATIVE',
        'YZ_POSITIVE': 'SET_SCENE_YZ_POSITIVE',
        'YZ_NEGATIVE': 'SET_SCENE_YZ_NEGATIVE'
    }
    
    # Check the view option validity
    if view_option not in view_commands:
        raise ValueError(f"Invalid view_option provided. Must be one of {list(view_commands.keys())}")
    
    # Write the command lines to the script
    lines = [
        "#************************************************************************",
        f"#****************** Setting Scene to {view_option} ************************",
        "#************************************************************************",
        "#",
        view_commands[view_option]
    ]

    script.append_lines(lines)
    return

def set_scene_colormap_type(colormap='PRIMARY', 
                            type_value='BLACKBODY_STANDARD'):
    """
    Appends lines to script state to set the solver colormap type.
    

    :param colormap: Either PRIMARY or SECONDARY.
    :param type_value: Type of colormap.
    
    Example usage:
    set_scene_colormap_type(, 'PRIMARY', 'BLACKBODY_STANDARD')
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    valid_types = ['RAINBOW_STANDARD', 'GRAYSCALE', 'BENT_HOTCOOL', 
                   'BLACKBODY_STANDARD', 'BLACKBODY_EXTENDED', 'KINDLMANN',
                   'RAINBOW_LONG', 'BROWNBLUE', 'HOTCOOL']
    if type_value not in valid_types:
        raise ValueError(f"`type_value` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap type ****************************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_TYPE",
        f"COLORMAP {colormap}",
        f"TYPE {type_value}"
    ]
    
    script.append_lines(lines)
    return

def set_scene_colormap_size(colormap='PRIMARY', 
                            thickness=300, height=15):
    """
    Appends lines to script state to set the solver colormap size.
    

    :param colormap: Either PRIMARY or SECONDARY.
    :param thickness: Thickness value in pixels.
    :param height: Height value in pixels.
    
    Example usage:
    set_scene_colormap_size(, 'PRIMARY', 300, 15)
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    if not isinstance(thickness, int):
        raise ValueError("`thickness` should be an integer value.")
    
    if not isinstance(height, int):
        raise ValueError("`height` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap size ****************************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_SIZE",
        f"COLORMAP {colormap}",
        f"THICKNESS {thickness}",
        f"HEIGHT {height}"
    ]
    
    script.append_lines(lines)
    return

def set_scene_colormap_position(colormap='PRIMARY', x=450, y=75):
    """
    Appends lines to script state to set the solver colormap position.
    
    Example usage:
        set_scene_colormap_position(, colormap='PRIMARY', x=450, y=75)
    

    :param colormap: Either 'PRIMARY' or 'SECONDARY'.
    :param x: Value in pixels for the X-coordinate.
    :param y: Value in pixels for the Y-coordinate.
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")

    if not isinstance(x, int):
        raise ValueError("`x` should be an integer value.")

    if not isinstance(y, int):
        raise ValueError("`y` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap position ************************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_POSITION",
        f"COLORMAP {colormap}",
        f"X {x}",
        f"Y {y}"
    ]

    script.append_lines(lines)
    return

def set_scene_colormap_shading(colormap='PRIMARY', reverse='DISABLE', smooth='ENABLE'):
    """
    Appends lines to script state to set the solver colormap shading.
    
    Example usage:
        set_scene_colormap_shading(, colormap='PRIMARY', reverse='DISABLE', smooth='ENABLE')
    

    :param colormap: Either 'PRIMARY' or 'SECONDARY'.
    :param reverse: Either 'ENABLE' or 'DISABLE'.
    :param smooth: Either 'ENABLE' or 'DISABLE'.
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")

    valid_settings = ['ENABLE', 'DISABLE']
    if reverse not in valid_settings:
        raise ValueError(f"`reverse` should be one of {valid_settings}")

    if smooth not in valid_settings:
        raise ValueError(f"`smooth` should be one of {valid_settings}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap shading *************************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_SHADING",
        f"COLORMAP {colormap}",
        f"REVERSE {reverse}",
        f"SMOOTH {smooth}"
    ]

    script.append_lines(lines)
    return

def set_scene_colormap_custom_mode(colormap='PRIMARY', custom_range='ENABLE'):
    """
    Appends lines to script state to set the colormap custom mode.
    

    :param colormap: Can be either 'PRIMARY' or 'SECONDARY'.
    :param custom_range: Can be either 'ENABLE' or 'DISABLE'.
    
    Example usage:
        set_scene_colormap_custom_mode()
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    valid_custom_ranges = ['ENABLE', 'DISABLE']
    if custom_range not in valid_custom_ranges:
        raise ValueError(f"`custom_range` should be one of {valid_custom_ranges}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap custom range mode ***************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_CUSTOM_MODE",
        f"COLORMAP {colormap}",
        f"CUSTOM_RANGE {custom_range}"
    ]

    script.append_lines(lines)
    return 

def set_scene_colormap_custom_range(colormap='PRIMARY', cut_off_mode='OFF', 
                                   maximum=1.0, minimum=-1.5):
    """
    Appends lines to script state to set the colormap custom range.
    

    :param colormap: Can be either 'PRIMARY' or 'SECONDARY'.
    :param cut_off_mode: Mode for the custom range cut off.
    :param maximum: Maximum value of the custom range.
    :param minimum: Minimum value of the custom range.
    
    Example usage:
        set_scene_colormap_custom_range()
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    valid_cut_off_modes = ['OFF', 'ABOVE_AND_BELOW', 'ABOVE_MAX', 'BELOW_MIN']
    if cut_off_mode not in valid_cut_off_modes:
        raise ValueError(f"`cut_off_mode` should be one of {valid_cut_off_modes}")
    
    if not isinstance(maximum, (int, float)):
        raise ValueError("`maximum` should be an integer or float value.")
    
    if not isinstance(minimum, (int, float)):
        raise ValueError("`minimum` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap custom range ********************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_CUSTOM_MODE",
        f"COLORMAP {colormap}",
        f"CUT_OFF_MODE {cut_off_mode}",
        f"MAXIMUM {maximum}",
        f"MINIMUM {minimum}"
    ]

    script.append_lines(lines)
    return

