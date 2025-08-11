from .utils import *    
from .script import script
from .types import *

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

def change_scene_to(scene: str) -> None:
    """
    Change the active scene.

    This function appends a command to the script state to switch the main
    view to a different scene.

    Parameters
    ----------
    scene : str
        The scene to change to. Must be one of `VALID_SCENE_LIST`.

    Examples
    --------
    >>> # Change the scene to the solver view
    >>> change_scene_to('SOLVER')
    """
    if scene not in VALID_SCENE_LIST:
        raise ValueError(f"Invalid scene: {scene}. Must be one of {VALID_SCENE_LIST}.")

    lines = [
        "#************************************************************************",
        "#************************ Change the Scene To ***************************",
        "#************************************************************************",
        "#",
        f"CHANGE_SCENE_TO_{scene}"
    ]
    script.append_lines(lines)
    return

def save_scene_as_image(filename: str) -> None:
    """
    Save the current scene as an image file.

    This function appends a command to the script to save the current view to
    an image file. The supported formats are .bmp, .png, .jpg, .jpeg, .tiff,
    and .gif.

    Parameters
    ----------
    filename : str
        The absolute path and filename for the saved image.

    Examples
    --------
    >>> # Save the scene as a PNG image
    >>> save_scene_as_image('C:/data/my_scene.png')
    """
    if not isinstance(filename, str):
        raise ValueError("`filename` must be a string representing the file path.")
    if not any(filename.lower().endswith(ext) for ext in ['.bmp', '.png', '.jpg', '.jpeg', '.tiff', '.gif']):
        raise ValueError("The filename must have a valid image extension.")

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

def set_scene_view(view_option: str = 'DEFAULTVIEW') -> None:
    """
    Set the scene view to a predefined orientation.

    This function appends a command to the script state to change the camera's
    viewpoint to a standard orientation.

    Parameters
    ----------
    view_option : str, optional
        The view to set, by default 'DEFAULTVIEW'. Must be one of
        `VALID_SCENE_VIEW_LIST`.

    Examples
    --------
    >>> # Set the scene to the default view
    >>> set_scene_view()

    >>> # Set the scene to a negative YZ view
    >>> set_scene_view('YZ_NEGATIVE')
    """
    if view_option not in VALID_SCENE_VIEW_LIST:
        raise ValueError(f"Invalid view_option. Must be one of {VALID_SCENE_VIEW_LIST}")

    view_commands = {
        'DEFAULTVIEW': 'SET_SCENE_DEFAULTVIEW',
        'XY_POSITIVE': 'SET_SCENE_XY_POSITIVE',
        'XY_NEGATIVE': 'SET_SCENE_XY_NEGATIVE',
        'XZ_POSITIVE': 'SET_SCENE_XZ_POSITIVE',
        'XZ_NEGATIVE': 'SET_SCENE_XZ_NEGATIVE',
        'YZ_POSITIVE': 'SET_SCENE_YZ_POSITIVE',
        'YZ_NEGATIVE': 'SET_SCENE_YZ_NEGATIVE'
    }

    lines = [
        "#************************************************************************",
        f"#****************** Setting Scene to {view_option} ************************",
        "#************************************************************************",
        "#",
        view_commands[view_option]
    ]
    script.append_lines(lines)
    return

def set_scene_colormap_type(
    colormap: str = 'PRIMARY',
    type_value: str = 'BLACKBODY_STANDARD'
) -> None:
    """
    Set the solver colormap type.

    This function appends a command to the script state to define the color
    scheme for either the primary or secondary colormap.

    Parameters
    ----------
    colormap : str, optional
        The colormap to modify, by default 'PRIMARY'. Must be one of
        `VALID_COLORMAP_LIST`.
    type_value : str, optional
        The type of colormap to apply, by default 'BLACKBODY_STANDARD'. Must be
        one of `VALID_COLORMAP_TYPE_LIST`.

    Examples
    --------
    >>> # Set the primary colormap to rainbow
    >>> set_scene_colormap_type('PRIMARY', 'RAINBOW_STANDARD')
    """
    if colormap not in VALID_COLORMAP_LIST:
        raise ValueError(f"`colormap` must be one of {VALID_COLORMAP_LIST}")
    if type_value not in VALID_COLORMAP_TYPE_LIST:
        raise ValueError(f"`type_value` must be one of {VALID_COLORMAP_TYPE_LIST}")

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

def set_scene_colormap_size(
    colormap: str = 'PRIMARY',
    thickness: int = 300,
    height: int = 15
) -> None:
    """
    Set the solver colormap size.

    This function appends a command to the script state to adjust the size of
    the specified colormap legend in pixels.

    Parameters
    ----------
    colormap : str, optional
        The colormap to modify, by default 'PRIMARY'. Must be one of
        `VALID_COLORMAP_LIST`.
    thickness : int, optional
        The thickness of the colormap legend in pixels, by default 300.
    height : int, optional
        The height of the colormap legend in pixels, by default 15.

    Examples
    --------
    >>> # Set the size of the secondary colormap
    >>> set_scene_colormap_size('SECONDARY', 400, 20)
    """
    if colormap not in VALID_COLORMAP_LIST:
        raise ValueError(f"`colormap` must be one of {VALID_COLORMAP_LIST}")
    if not isinstance(thickness, int):
        raise ValueError("`thickness` must be an integer.")
    if not isinstance(height, int):
        raise ValueError("`height` must be an integer.")

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

def set_scene_colormap_position(
    colormap: str = 'PRIMARY',
    x: int = 450,
    y: int = 75
) -> None:
    """
    Set the solver colormap position.

    This function appends a command to the script state to place the specified
    colormap legend at a given pixel coordinate.

    Parameters
    ----------
    colormap : str, optional
        The colormap to modify, by default 'PRIMARY'. Must be one of
        `VALID_COLORMAP_LIST`.
    x : int, optional
        The x-coordinate in pixels, by default 450.
    y : int, optional
        The y-coordinate in pixels, by default 75.

    Examples
    --------
    >>> # Reposition the primary colormap
    >>> set_scene_colormap_position('PRIMARY', 100, 50)
    """
    if colormap not in VALID_COLORMAP_LIST:
        raise ValueError(f"`colormap` must be one of {VALID_COLORMAP_LIST}")
    if not isinstance(x, int):
        raise ValueError("`x` must be an integer.")
    if not isinstance(y, int):
        raise ValueError("`y` must be an integer.")

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

def set_scene_colormap_shading(
    colormap: str = 'PRIMARY',
    reverse: RunOptions = 'DISABLE',
    smooth: RunOptions = 'ENABLE'
) -> None:
    """
    Set the solver colormap shading options.

    This function appends a command to the script state to configure the
    shading properties of the specified colormap.

    Parameters
    ----------
    colormap : str, optional
        The colormap to modify, by default 'PRIMARY'. Must be one of
        `VALID_COLORMAP_LIST`.
    reverse : RunOptions, optional
        Reverse the colormap direction, by default 'DISABLE'. Must be one of
        `VALID_RUN_OPTIONS`.
    smooth : RunOptions, optional
        Enable or disable smooth shading, by default 'ENABLE'. Must be one of
        `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Reverse the secondary colormap and disable smooth shading
    >>> set_scene_colormap_shading('SECONDARY', 'ENABLE', 'DISABLE')
    """
    if colormap not in VALID_COLORMAP_LIST:
        raise ValueError(f"`colormap` must be one of {VALID_COLORMAP_LIST}")
    if reverse not in VALID_RUN_OPTIONS:
        raise ValueError(f"`reverse` must be one of {VALID_RUN_OPTIONS}")
    if smooth not in VALID_RUN_OPTIONS:
        raise ValueError(f"`smooth` must be one of {VALID_RUN_OPTIONS}")

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

def set_scene_colormap_custom_mode(
    colormap: str = 'PRIMARY',
    custom_range: RunOptions = 'ENABLE'
) -> None:
    """
    Set the colormap custom range mode.

    This function appends a command to the script state to enable or disable
    the custom range mode for the specified colormap.

    Parameters
    ----------
    colormap : str, optional
        The colormap to modify, by default 'PRIMARY'. Must be one of
        `VALID_COLORMAP_LIST`.
    custom_range : RunOptions, optional
        Enable or disable custom range, by default 'ENABLE'. Must be one of
        `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Disable custom range for the primary colormap
    >>> set_scene_colormap_custom_mode('PRIMARY', 'DISABLE')
    """
    if colormap not in VALID_COLORMAP_LIST:
        raise ValueError(f"`colormap` must be one of {VALID_COLORMAP_LIST}")
    if custom_range not in VALID_RUN_OPTIONS:
        raise ValueError(f"`custom_range` must be one of {VALID_RUN_OPTIONS}")

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

def set_scene_colormap_custom_range(
    colormap: str = 'PRIMARY',
    cut_off_mode: str = 'OFF',
    maximum: float = 1.0,
    minimum: float = -1.5
) -> None:
    """
    Set the colormap custom range.

    This function appends a command to the script state to define a custom
    range for the specified colormap, including min/max values and cut-off mode.

    Parameters
    ----------
    colormap : str, optional
        The colormap to modify, by default 'PRIMARY'. Must be one of
        `VALID_COLORMAP_LIST`.
    cut_off_mode : str, optional
        The cut-off mode for the custom range, by default 'OFF'. Must be one
        of `VALID_CUT_OFF_MODE_LIST`.
    maximum : float, optional
        The maximum value of the custom range, by default 1.0.
    minimum : float, optional
        The minimum value of the custom range, by default -1.5.

    Examples
    --------
    >>> # Set a custom range for the primary colormap
    >>> set_scene_colormap_custom_range('PRIMARY', 'ABOVE_AND_BELOW', 2.0, -1.0)
    """
    if colormap not in VALID_COLORMAP_LIST:
        raise ValueError(f"`colormap` must be one of {VALID_COLORMAP_LIST}")
    if cut_off_mode not in VALID_CUT_OFF_MODE_LIST:
        raise ValueError(f"`cut_off_mode` must be one of {VALID_CUT_OFF_MODE_LIST}")
    if not isinstance(maximum, (int, float)):
        raise ValueError("`maximum` must be a numeric value.")
    if not isinstance(minimum, (int, float)):
        raise ValueError("`minimum` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap custom range ********************",
        "#************************************************************************",
        "#",
        "SET_SCENE_COLORMAP_CUSTOM_RANGE",
        f"COLORMAP {colormap}",
        f"CUT_OFF_MODE {cut_off_mode}",
        f"MAXIMUM {maximum}",
        f"MINIMUM {minimum}"
    ]
    script.append_lines(lines)
    return

