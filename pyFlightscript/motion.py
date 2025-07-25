from .utils import *    
from .script import script
from .types import *

def create_new_motion(motion_type):
    """
    Appends lines to script state to create a new motion definition based on the motion type.
    
    :param motion_type: Type of the motion. One of: 'EUCLIDEAN', 'CUSTOM', '6DOF'.
    
    Example usage:
        create_new_motion('EUCLIDEAN')
        create_new_motion('CUSTOM')
        create_new_motion('6DOF')
    """
    
    valid_types = ['EUCLIDEAN', 'CUSTOM', '6DOF']
    if motion_type not in valid_types:
        raise ValueError(f"`motion_type` should be one of {valid_types}")

    lines = [
        "#************************************************************************",
        f"#************** Create a new {motion_type} motion definition ********************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_MOTION {motion_type}"
    ]

    script.append_lines(lines)
    return

def set_motion_boundaries(motion_id, num_boundaries=-1, boundaries=None):
    """
    Appends lines to script state to specify motion boundaries.
    

    :param motion_id: Index of the motion definition.
    :param num_boundaries: Number of geometry boundaries being specified.
    :param boundaries: List of geometry boundaries if num_boundaries is not set to -1.
    
    Example usage:
    >>> set_motion_boundaries(, 1, 4, [1, 2, 3, 5])
    >>> set_motion_boundaries(, 1)
    """

    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` should be an integer value.")
    
    if num_boundaries != -1 and (boundaries is None or not isinstance(boundaries, list)):
        raise ValueError("`boundaries` should be provided and be a list if `num_boundaries` is not -1.")

    lines = [
        "#************************************************************************",
        "#*********** Specify motion definition boundaries *************",
        "#************************************************************************",
        "#",
        f"SET_MOTION_BOUNDARIES {motion_id} {num_boundaries}",
    ]
    if num_boundaries != -1:
        boundaries_str = ','.join(map(str, boundaries))
        lines.append(boundaries_str)

    script.append_lines(lines)
    return

def set_motion_moving_frames(motion_id, num_frames, frames_list=None):
    """
    Appends lines to script state to specify local frames to motion definition.
    
    # Example usage:
    # set_motion_moving_frames('path_to_script1.txt', 1, 4, [1,2,3,5])


    :param motion_id: Index of the motion definition.
    :param num_frames: Number of user-defined local coordinate frames.
    :param frames_list: List of frame indices. Only necessary if num_frames > 0.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(num_frames, int):
        raise ValueError("`num_frames` should be an integer value.")
    
    if num_frames > 0 and not isinstance(frames_list, list):
        raise ValueError("`frames_list` should be provided and be of type list when `num_frames` is greater than 0.")
    
    # Construct lines
    lines = [
        "#************************************************************************",
        "#*********** Specify specified local frames to motion definition ********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_MOVING_FRAMES {motion_id} {num_frames}"
    ]
    
    if frames_list:
        lines.append(",".join(map(str, frames_list)))

    script.append_lines(lines)
    return

def set_motion_coordinate_system(motion_id, coordinate_system_id):
    """
    Appends lines to script state to set the coordinate system for a motion definition.
    
    # Example usage:
    # set_motion_coordinate_system('path_to_script2.txt', 1, 3)


    :param motion_id: Index of the motion definition.
    :param coordinate_system_id: Index of the coordinate system.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(coordinate_system_id, int) or coordinate_system_id <= 0:
        raise ValueError("`coordinate_system_id` should be an integer value greater than 0.")
    
    # Construct lines
    lines = [
        "#************************************************************************",
        "#********** Set the coordinate system for a motion definition ***********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_COORDINATE_SYSTEM {motion_id} {coordinate_system_id}"
    ]

    script.append_lines(lines)
    return

def set_motion_start_time(motion_id, start_time=0.0):
    """
    Appends lines to script state to set the start time for a motion definition.
    

    :param motion_id: Index of the motion definition.
    :param start_time: Start time for the motion within the solver physical time.
    
    Example usage:
    set_motion_start_time(, 1, 2.5)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(start_time, float) or start_time < 0.0:
        raise ValueError("`start_time` should be a non-negative float value.")
    
    lines = [
        "#************************************************************************",
        "#************** Set the start time for a motion definition **************",
        "#************************************************************************",
        "#",
        f"SET_MOTION_START_TIME {motion_id} {start_time}"
    ]

    script.append_lines(lines)
    return

def set_motion_velocity(motion_id, vx=0.0, vy=0.0, vz=0.0):
    """
    Appends lines to script state to set the velocity vector for a motion definition.
    

    :param motion_id: Index of the motion definition.
    :param vx, vy, vz: Velocity vector components in the motion definition coordinate system.
    
    Example usage:
    set_motion_velocity(, 1, 30.0, -10.0, 0.0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(vx, (int, float)) or not isinstance(vy, (int, float)) or not isinstance(vz, (int, float)):
        raise ValueError("`vx`, `vy`, and `vz` should be either integer or float values.")
    
    lines = [
        "#************************************************************************",
        "#************** Set the velocity vector for a motion definition *********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_VELOCITY {motion_id} {vx} {vy} {vz}"
    ]

    script.append_lines(lines)
    return 

def set_motion_acceleration(motion_id, ax=0.0, ay=0.0, az=0.0):
    """
    Appends lines to script state to set the acceleration vector for a motion definition.
    

    :param motion_id: Index of the motion definition (> 0).
    :param ax: X component of the velocity vector.
    :param ay: Y component of the velocity vector.
    :param az: Z component of the velocity vector.
    
    Example usage:
    set_motion_acceleration(, 1, 0.5, -1.0, 2.5)
    """

    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer.")
    
    if not all(isinstance(val, (int, float)) for val in [ax, ay, az]):
        raise ValueError("`ax`, `ay`, and `az` should be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the acceleration vector for a motion definition ********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_ACCELERATION {motion_id} {ax} {ay} {az}"
    ]

    script.append_lines(lines)
    return

def set_motion_angular_velocity(motion_id, wx=0.0, wy=0.0, wz=0.0):
    """
    Appends lines to script state to set the angular velocity vector for a motion definition.
    

    :param motion_id: Index of the motion definition (> 0).
    :param wx: X component of the angular velocity vector.
    :param wy: Y component of the angular velocity vector.
    :param wz: Z component of the angular velocity vector.
    
    Example usage:
    set_motion_angular_velocity(, 1, -450.5, 0.0, 0.0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_ID` should be a positive integer.")
    
    if not all(isinstance(val, (int, float)) for val in [wx, wy, wz]):
        raise ValueError("`wx`, `wy`, and `wz` should be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the angular velocity vector for a motion definition ****",
        "#************************************************************************",
        "#",
        f"SET_MOTION_ANGULAR_VELOCITY {motion_id} {wx} {wy} {wz}"
    ]

    script.append_lines(lines)
    return

def set_motion_angular_acceleration(motion_id, wax=0.0, way=0.0, waz=0.0):
    """
    Appends lines to script state to set the angular acceleration vector 
    for a motion definition.
    

    :param motion_id: Index of the motion definition.
    :param wax: Angular acceleration in X.
    :param way: Angular acceleration in Y.
    :param waz: Angular acceleration in Z.
    
    Example usage:
        set_motion_angular_acceleration(, 1, 0.5, -1.0, 2.5)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(val, (int, float)) for val in [wax, way, waz]):
        raise ValueError("Angular acceleration values should be integer or float values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the acceleration vector for a motion definition ********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_ANGULAR_ACCELERATION {motion_id} {wax} {way} {waz}"
    ]
    
    script.append_lines(lines)
    return

def set_motion_is_rotor(motion_id, flag='ENABLE', axis='X'):
    """
    Appends lines to script state to specify if the motion definition 
    is a rotor or propeller.
    

    :param motion_id: Index of the motion definition.
    :param flag: ENABLE or DISABLE.
    :param axis: Axis specification (X, Y or Z).
    
    Example usage:
        set_motion_is_rotor(, 1, 'ENABLE', 'X')
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if flag not in ['ENABLE', 'DISABLE']:
        raise ValueError("`flag` should be either 'ENABLE' or 'DISABLE'.")
    
    if axis not in ['X', 'Y', 'Z']:
        raise ValueError("`axis` should be one of 'X', 'Y', 'Z'.")
    
    lines = [
        "#************************************************************************",
        "#*********** Specify if motion definition is a rotor/propeller **********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_IS_ROTOR {motion_id} {flag} {axis}"
    ]
    
    script.append_lines(lines)
    return

def set_motion_custom_table(motion_type='VELOCITY-TIME', motion_id=1, filename=None):
    """
    Appends lines to script state to specify a custom motion definition table.
    

    :param motion_type: Type of motion, either 'VELOCITY-TIME' or 'POSITION-TIME'.
    :param motion_id: Index of the motion definition (> 0).
    :param filename: Path to the text file containing the motion data.

    Example usage:
    set_motion_custom_table(, motion_type='VELOCITY-TIME', motion_id=1, 
                            filename='C:\\Users\\Desktop\\Models\\custom_motion.txt')
    """
    
    # Type and value checking
    valid_motion_types = ['VELOCITY-TIME', 'POSITION-TIME']
    if motion_type not in valid_motion_types:
        raise ValueError(f"`motion_type` should be one of {valid_motion_types}")

    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    if filename is None or not isinstance(filename, str):
        raise ValueError("`filename` should be a valid string path to the motion data.")
    
    lines = [
        "#************************************************************************",
        "#*********** Specify custom motion definition table ********************",
        "#************************************************************************",
        "#",
        f"SET_MOTION_CUSTOM_TABLE {motion_type} {motion_id}",
        filename
    ]

    script.append_lines(lines)
    return

def set_motion_mass_properties(motion_id, mass=0.0, ixx=0.0, iyy=0.0, izz=0.0, ixy=0.0, iyz=0.0, izx=0.0):
    """
    Appends lines to script state to specify motion mass properties.
    

    :param motion_id: Index of the motion definition (> 0).
    :param mass: Mass (kg) of the geometry.
    :param ixx, iyy, izz: Moment of inertia components.
    :param ixy, iyz, izx: Product of inertia components.

    Example usage:
    set_motion_mass_properties(, motion_id=1, mass=1200.5, ixx=12.5, 
                               iyy=45.3, izz=0.3, ixy=0.0, iyz=12.4, izx=13.5)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    if not all(isinstance(val, (int, float)) for val in [mass, ixx, iyy, izz, ixy, iyz, izx]):
        raise ValueError("Mass and inertia values should be numeric (int or float).")
    
    lines = [
        "#************************************************************************",
        "#*********** Specify motion mass properties ****************************",
        "#************************************************************************",
        "#",
        f"SET_MOTION_MASS_PROPERTIES {motion_id} {mass} {ixx} {iyy} {izz} {ixy} {iyz} {izx}"
    ]

    script.append_lines(lines)
    return

def set_motion_gravity(motion_id, gx=0, gy=0, gz=-9.81):
    """
    Appends lines to script state to set the gravity force for a 6DOF motion definition.
    

    :param motion_id: Index of the motion definition.
    :param gx: Gravity vector component in the reference coordinate system (X-direction).
    :param gy: Gravity vector component in the reference coordinate system (Y-direction).
    :param gz: Gravity vector component in the reference coordinate system (Z-direction).

    Example usage:
    set_motion_gravity(, 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(val, (int, float)) for val in [gx, gy, gz]):
        raise ValueError("Gravity components `gx`, `gy`, and `gz` should be integers or float values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the gravity force for a 6DOF motion definition *********",
        "#************************************************************************",
        "#",
        f"SET_MOTION_GRAVITY {motion_id} {gx} {gy} {gz}"
    ]

    script.append_lines(lines)
    return

def set_motion_6dof_initial_velocity(motion_id, vx=0.0, vy=0.0, vz=0.0):
    """
    Appends lines to script state to set the initial velocity conditions for a 6DOF motion.
    

    :param motion_id: Index of the motion definition.
    :param vx: Initial velocity vector component in the body coordinate system (X-direction).
    :param vy: Initial velocity vector component in the body coordinate system (Y-direction).
    :param vz: Initial velocity vector component in the body coordinate system (Z-direction).

    Example usage:
    set_motion_6dof_initial_velocity(, 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(val, (int, float)) for val in [vx, vy, vz]):
        raise ValueError("Velocity components `vx`, `vy`, and `vz` should be integers or float values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the initial velocity conditions for a 6DOF motion ******",
        "#************************************************************************",
        "#",
        f"SET_MOTION_6DOF_INITIAL_VELOCITY {motion_id} {vx} {vy} {vz}"
    ]

    script.append_lines(lines)
    return

def set_motion_6dof_initial_angular_velocity(motion_id, wx=0.0, wy=0.0, wz=0.0):
    """
    Appends lines to script state to set initial angular velocity conditions for a 6DOF motion.

    Example usage:
    set_motion_6dof_initial_angular_velocity(, 1, 0.0, 0, -0.25)
    

    :param motion_id: Index of the motion definition.
    :param wx: X component of the initial angular velocity vector.
    :param wy: Y component of the initial angular velocity vector.
    :param wz: Z component of the initial angular velocity vector.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(i, (int, float)) for i in [wx, wy, wz]):
        raise ValueError("Angular velocity components should be integer or float values.")
    
    lines = [
        "#************************************************************************",
        "#******* Set initial angular velocity conditions for a 6DOF motion ******",
        "#************************************************************************",
        "#",
        f"SET_MOTION_6DOF_INITIAL_ANGULAR_VELOCITY {motion_id} {wx} {wy} {wz}"
    ]

    script.append_lines(lines)
    return

def set_motion_6dof_active_variables(motion_id, u='DISABLE', v='DISABLE', 
                                     w='DISABLE', p='DISABLE', q='DISABLE', r='DISABLE'):
    """
    Appends lines to script state to set the 6DOF motion active variables.

    Example usage:
    set_motion_6dof_active_variables(, 1, u='DISABLE', v='DISABLE', 
                                     w='DISABLE', p='DISABLE', q='ENABLE', r='ENABLE')
    

    :param motion_id: Index of the motion definition.
    :param u: Enable or disable the U velocity component.
    :param v: Enable or disable the V velocity component.
    :param w: Enable or disable the W velocity component.
    :param p: Enable or disable the P angular velocity component.
    :param q: Enable or disable the Q angular velocity component.
    :param r: Enable or disable the R angular velocity component.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    valid_values = ['ENABLE', 'DISABLE']
    if any(i not in valid_values for i in [u, v, w, p, q, r]):
        raise ValueError(f"All parameters should be one of {valid_values}")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the 6DOF motion active variables ***********************",
        "#************************************************************************",
        "#",
        f"SET_MOTION_6DOF_ACTIVE_VARIABLES {motion_id}",
        f"U {u}",
        f"V {v}",
        f"W {w}",
        f"P {p}",
        f"Q {q}",
        f"R {r}"
    ]

    script.append_lines(lines)
    return

def set_6dof_motion_symmetry_loads(motion_id, symmetry_loads='ENABLE'):
    """
    Appends lines to script state to set 6DOF motion symmetry loads.
    

    :param motion_id: Index of the motion definition.
    :param symmetry_loads: ENABLE or DISABLE the symmetry boundary loads option.
    
    Example usage:
    >>> set_6dof_motion_symmetry_loads(, 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    valid_symmetry_loads = ['ENABLE', 'DISABLE']
    if symmetry_loads not in valid_symmetry_loads:
        raise ValueError(f"`symmetry_loads` should be one of {valid_symmetry_loads}")
    
    lines = [
        "#************************************************************************",
        "#*********** Convert the 6DOF motion into a longitudinal 3DOF ***********",
        "#************************************************************************",
        "#",
        f"SET_3DOF_MOTION {motion_id} {symmetry_loads}"
    ]
    script.append_lines(lines)
    return

def create_new_6dof_external_force(motion_id, x, y, z, t_start, delta_t, fx, fy, fz):
    """
    Appends lines to script state to create a new 6DOF motion external force.
    

    :param motion_id: Index of the motion definition.
    :param x, y, z: Coordinates of the 6DOF external force.
    :param t_start: Start time of the external force.
    :param delta_t: Operational time of the external force.
    :param fx, fy, fz: Force vector components.
    
    Example usage:
    >>> create_new_6dof_external_force(, 1, 0.0, -0.2, 1.2, 0, 0.25, -3000, 0, 0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    if not isinstance(t_start, (int, float)) or t_start < 0:
        raise ValueError("`t_start` should be a non-negative number.")
    
    if not isinstance(delta_t, (int, float)) or delta_t <= 0:
        raise ValueError("`delta_t` should be a positive number.")
    
    lines = [
        "#************************************************************************",
        "#*********** Create a new 6DOF motion external force ********************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_6DOF_EXTERNAL_FORCE {motion_id} {x} {y} {z} {t_start} {delta_t} {fx} {fy} {fz}"
    ]
    script.append_lines(lines)
    return

def create_new_6dof_custom_force(motion_id, force_type, filename):
    """
    Appends lines to script state to create a new 6DOF motion custom external force profile.
    

    :param motion_id: Index of the motion definition.
    :param force_type: Type of the custom motion. One of: 'FORCE_VS_TIME' or 'FORCE_VS_DISTANCE'.
    :param filename: Path to the text file containing the custom force profile.
    
    Example usage:
    create_new_6dof_custom_force(, 1, 'FORCE_VS_TIME', 'C:\\Users\\Desktop\\Models\\custom_force_profile.txt')
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    valid_types = ['FORCE_VS_TIME', 'FORCE_VS_DISTANCE']
    if force_type not in valid_types:
        raise ValueError(f"`force_type` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#******** Create a new 6DOF motion custom external force profile ********",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_6DOF_CUSTOM_FORCE {motion_id} {force_type}",
        filename
    ]

    script.append_lines(lines)
    return

def create_new_6dof_spring_force(motion_id, x, y, z, nx, ny, nz, free_length, 
                                 solid_length, initial_length, spring_rate):
    """
    Appends lines to script state to create a new 6DOF motion external spring force.
    

    :param motion_id: Index of the motion definition.
    :param x, y, z: Coordinates of the 6DOF external force in the body frame coordinate system.
    :param nx, ny, nz: Normal vector coordinates of the spring axis.
    :param free_length: Length of the uncompressed spring.
    :param solid_length: Fully-compressed spring length.
    :param initial_length: Initial compressed length of the spring.
    :param spring_rate: Force per unit length of the spring (in N/m).
    
    Example usage:
    create_new_6dof_spring_force(, 1, 0.0, -0.2, 1.2, 0, 0, -1, 0.1, 0.05, 0.06, 100000.0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    for val in [free_length, solid_length, initial_length, spring_rate]:
        if not isinstance(val, (int, float)) or val <= 0:
            raise ValueError("All spring parameters should be positive numbers.")
    
    lines = [
        "#************************************************************************",
        "#*********** Create a new 6DOF motion external spring force *************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_6DOF_SPRING_FORCE {motion_id} {x} {y} {z} {nx} {ny} {nz} {free_length} {solid_length} {initial_length} {spring_rate}"
    ]

    script.append_lines(lines)
    return

def delete_6dof_external_force(motion_id, force_id):
    """
    Appends lines to script state to delete an existing 6DOF Motion external force.
    

    :param motion_id: Index of the motion definition.
    :param force_id: Index of the external force to be deleted.
    
    Example usage:
    delete_6dof_external_force(, 1, 4)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(force_id, int) or force_id <= 0:
        raise ValueError("`force_id` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#*********** Delete an existing 6DOF Motion external force **************",
        "#************************************************************************",
        "#",
        f"DELETE_6DOF_EXTERNAL_FORCE {motion_id} {force_id}"
    ]

    script.append_lines(lines)
    return

def export_6dof_trajectory(motion_id, filename):
    """
    Appends lines to script state to export 6DOF Motion trajectory tables to external file.
    

    :param motion_id: Index of the motion definition.
    :param filename: Path to the text file where the trajectory tables should be written.
    
    Example usage:
    export_6dof_trajectory(, 1, 'C:\\Users\\Desktop\\Models\\6DOF_Trajectory.txt')
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    check_file_existence(filename)
    
    lines = [
        "#************************************************************************",
        "#*********** Export 6DOF Motion trajectory tables to external file ******",
        "#************************************************************************",
        "#",
        f"EXPORT_6DOF_TRAJECTORY {motion_id}",
        filename
    ]

    script.append_lines(lines)
    return

def set_motion_fsi_executable(motion_id, executable_path, show_console='DISABLE', 
                              export_load_distributions='ENABLE'):
    """
    Appends lines to script state to set the FSI motion executable.
    
    Example usage:
    set_motion_fsi_executable(, 1)
    

    :param motion_id: Index of the motion definition.
    :param show_console: Enable or disable the console window output.
    :param export_load_distributions: Enable or disable the export of the aerodynamic load distributions.
    :param executable_path: Path to the FSI Beam executable.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer greater than 0.")
    
    valid_options = ['ENABLE', 'DISABLE']
    if show_console not in valid_options:
        raise ValueError(f"`show_console` should be one of {valid_options}")
    
    if export_load_distributions not in valid_options:
        raise ValueError(f"`export_load_distributions` should be one of {valid_options}")
    
    check_file_existence(executable_path)

    lines = [
        "#************************************************************************",
        "#*********** Set the FSI motion executable ******************************",
        "#************************************************************************",
        "#",
        "SET_MOTION_FSI_EXECUTABLE",
        f"{motion_id} {show_console} {export_load_distributions}",
        executable_path
    ]

    script.append_lines(lines)
    return

def set_motion_fsi_structural_nodes(motion_id, nodes_file_path):
    """
    Appends lines to script state to set the FSI motion structural nodes.
    
    Example usage:
    set_motion_fsi_structural_nodes(, 1)
    

    :param motion_id: Index of the motion definition.
    :param nodes_file_path: Path to the FSI Displacement points file.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer greater than 0.")
    
    check_file_existence(nodes_file_path)

    lines = [
        "#************************************************************************",
        "#*********** Set the FSI motion structural nodes ************************",
        "#************************************************************************",
        "#",
        "SET_MOTION_FSI_STRUCTURAL_NODES",
        str(motion_id),
        nodes_file_path
    ]

    script.append_lines(lines)
    return

def delete_motion(motion_id):
    """
    Appends lines to script state to delete an existing motion definition.


    :param motion_id: Index of the motion definition.
    
    Example usage:
    delete_motion(, 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#*********** Delete an existing motion definition ***********************",
        "#************************************************************************",
        "#",
        f"DELETE_MOTION {motion_id}"
    ]

    script.append_lines(lines)
    return