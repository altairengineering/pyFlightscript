from . import actuators
from . import analysis
from . import base
from . import boundary_layer
from . import cad
from . import csys
from . import exec_solver
from . import export_data
from . import freestream
from . import mesh
from . import fsinit
from . import inlets
from . import log
from . import motion
from . import plots
from . import post_points
from . import post_surf
from . import post_volume
from . import post_streamlines
from . import scene
from . import set_solver
from . import solver
from . import tools
from . import unite
from . import wake
from . import wrapper
from . import script

from .actuators import *
from .analysis import *
from .base import *
from .boundary_layer import *
from .cad import *
from .csys import *
from .exec_solver import *
from .export_data import *
from .freestream import *
from .mesh import *
from .fsinit import *
from .inlets import *
from .log import *
from .motion import *
from .plots import *
from .post_points import *
from .post_surf import *
from .post_volume import *
from .post_streamlines import *
from .scene import *
from .set_solver import *
from .solver import *
from .tools import *
from .unite import *
from .wake import *
from .wrapper import *
from .script import *

import os
import subprocess

def execute_fsm_script(script_path=".\script_out.txt", fsexe_path=None, hidden=False):
    """
    Execute a fligthscript script using the specified script path and FSM executable path.
    
    :param script_path (str): The path to the FSM script file.
    :param fsexe_path (str, optional): The path to the FSM executable. If not provided, the function will
            attempt to retrieve the path from the FS_EXE environment variable. Defaults to None.
    
    Returns:
        subprocess.CompletedProcess: The result of running the FSM script.
    
    Raises:
        ValueError: If neither fsexe_path argument nor FS_EXE environment variable is set.
        FileNotFoundError: If the specified FSM executable file is not found.
    """
    if fsexe_path is None:
        fsexe_path = os.environ.get('FS_EXE')
        if fsexe_path is None:
            raise ValueError("Neither fsexe_path argument nor FS_EXE environment variable is set.")
    
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The specified file '{script_path}' does not exist on path.")
    
    try:
        command = [fsexe_path]
        if hidden:
            command.append('-hidden')
        command.extend(['-script', script_path])
        result = subprocess.run(command, capture_output=True, text=True)
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {fsexe_path} was not found.")

