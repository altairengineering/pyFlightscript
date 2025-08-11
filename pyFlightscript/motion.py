from .types import VALID_AXIS_LIST, VALID_MOTION_SOLVER_TYPE_LIST, VALID_MOTION_TYPE_LIST
from . import script

def set_motion_controls(
    reference_frame: int = 1, 
    cg_x: float = 0.0, 
    cg_y: float = 0.0, 
    cg_z: float = 0.0
) -> None:
    """
    Set the motion controls for the simulation.

    This function defines the center of gravity (CG) and the reference frame
    for the motion of the aircraft.

    Parameters
    ----------
    reference_frame : int, optional
        The reference frame number for the motion, by default 1.
    cg_x : float, optional
        The x-coordinate of the center of gravity, by default 0.0.
    cg_y : float, optional
        The y-coordinate of the center of gravity, by default 0.0.
    cg_z : float, optional
        The z-coordinate of the center of gravity, by default 0.0.

    Examples
    --------
    >>> # Set the motion controls with a specific CG
    >>> set_motion_controls(reference_frame=1, cg_x=1.5, cg_y=0.0, cg_z=0.2)
    """
    if not isinstance(reference_frame, int):
        raise ValueError("`reference_frame` should be an integer value.")
    if not all(isinstance(x, (int, float)) for x in [cg_x, cg_y, cg_z]):
        raise ValueError("`cg_x`, `cg_y`, and `cg_z` should be numeric values.")

    lines = [
        "#",
        "SET_MOTION_CONTROLS",
        f"REFERENCE_FRAME {reference_frame}",
        f"CG {cg_x} {cg_y} {cg_z}",
    ]
    script.append_lines(lines)
    return

def set_motion_solver(
    solver_type: str = 'STEADY', 
    time_step: float = 0.01, 
    total_time: float = 1.0,
    iterations: int = 10, 
    tolerance: float = 1e-6
) -> None:
    """
    Set the motion solver parameters.

    This function configures the solver for motion analysis, including the
    type of solver, time step, total simulation time, iterations, and tolerance.

    Parameters
    ----------
    solver_type : {'STEADY', 'UNSTEADY'}, optional
        The type of motion solver, by default 'STEADY'.
    time_step : float, optional
        The time step for unsteady simulations, by default 0.01.
    total_time : float, optional
        The total simulation time for unsteady simulations, by default 1.0.
    iterations : int, optional
        The number of iterations for the motion solver, by default 10.
    tolerance : float, optional
        The convergence tolerance for the motion solver, by default 1e-6.

    Examples
    --------
    >>> # Set up an unsteady motion solver
    >>> set_motion_solver(solver_type='UNSTEADY', time_step=0.005, total_time=2.0)
    """
    if solver_type not in VALID_MOTION_SOLVER_TYPE_LIST:
        raise ValueError(f"`solver_type` should be one of {VALID_MOTION_SOLVER_TYPE_LIST}")
    if not all(isinstance(x, (int, float)) for x in [time_step, total_time, tolerance]):
        raise ValueError("`time_step`, `total_time`, and `tolerance` should be numeric values.")
    if not isinstance(iterations, int):
        raise ValueError("`iterations` should be an integer value.")

    lines = [
        "#",
        "SET_MOTION_SOLVER",
        f"TYPE {solver_type}",
        f"TIME_STEP {time_step}",
        f"TOTAL_TIME {total_time}",
        f"ITERATIONS {iterations}",
        f"TOLERANCE {tolerance}",
    ]
    script.append_lines(lines)
    return

def set_motion_translation(
    axis: str = 'Z', 
    motion_type: str = 'ACCELERATION', 
    amplitude: float = 1.0,
    frequency: float = 1.0, 
    phase: float = 0.0, 
    initial_displacement: float = 0.0,
    initial_velocity: float = 0.0
) -> None:
    """
    Define a translational motion.

    This function specifies a translational motion along a given axis. The motion
    can be defined by acceleration, velocity, or displacement.

    Parameters
    ----------
    axis : {'X', 'Y', 'Z'}, optional
        The axis of translation, by default 'Z'.
    motion_type : {'ACCELERATION', 'VELOCITY', 'DISPLACEMENT'}, optional
        The type of motion definition, by default 'ACCELERATION'.
    amplitude : float, optional
        The amplitude of the motion, by default 1.0.
    frequency : float, optional
        The frequency of the motion in Hz, by default 1.0.
    phase : float, optional
        The phase angle of the motion in degrees, by default 0.0.
    initial_displacement : float, optional
        The initial displacement, by default 0.0.
    initial_velocity : float, optional
        The initial velocity, by default 0.0.

    Examples
    --------
    >>> # Define a sinusoidal velocity motion along the X-axis
    >>> set_motion_translation(axis='X', motion_type='VELOCITY', amplitude=5.0, frequency=2.0)
    """
    if axis not in VALID_AXIS_LIST:
        raise ValueError(f"`axis` should be one of {VALID_AXIS_LIST}")
    if motion_type not in VALID_MOTION_TYPE_LIST:
        raise ValueError(f"`motion_type` should be one of {VALID_MOTION_TYPE_LIST}")
    if not all(isinstance(x, (int, float)) for x in [amplitude, frequency, phase, initial_displacement, initial_velocity]):
        raise ValueError("Motion parameters (`amplitude`, `frequency`, `phase`, `initial_displacement`, `initial_velocity`) should be numeric.")

    lines = [
        "#",
        "SET_MOTION_TRANSLATION",
        f"AXIS {axis}",
        f"TYPE {motion_type}",
        f"AMPLITUDE {amplitude}",
        f"FREQUENCY {frequency}",
        f"PHASE {phase}",
        f"INITIAL_DISPLACEMENT {initial_displacement}",
        f"INITIAL_VELOCITY {initial_velocity}",
    ]
    script.append_lines(lines)
    return

def set_motion_rotation(
    axis: str = 'Y', 
    motion_type: str = 'ACCELERATION', 
    amplitude: float = 1.0,
    frequency: float = 1.0, 
    phase: float = 0.0, 
    initial_displacement: float = 0.0,
    initial_velocity: float = 0.0
) -> None:
    """
    Define a rotational motion.

    This function specifies a rotational motion about a given axis. The motion
    can be defined by acceleration, velocity, or displacement.

    Parameters
    ----------
    axis : {'X', 'Y', 'Z'}, optional
        The axis of rotation, by default 'Y'.
    motion_type : {'ACCELERATION', 'VELOCITY', 'DISPLACEMENT'}, optional
        The type of motion definition, by default 'ACCELERATION'.
    amplitude : float, optional
        The amplitude of the motion, by default 1.0.
    frequency : float, optional
        The frequency of the motion in Hz, by default 1.0.
    phase : float, optional
        The phase angle of the motion in degrees, by default 0.0.
    initial_displacement : float, optional
        The initial angular displacement, by default 0.0.
    initial_velocity : float, optional
        The initial angular velocity, by default 0.0.

    Examples
    --------
    >>> # Define a pitching acceleration motion about the Y-axis
    >>> set_motion_rotation(axis='Y', motion_type='ACCELERATION', amplitude=10.0, frequency=1.5)
    """
    if axis not in VALID_AXIS_LIST:
        raise ValueError(f"`axis` should be one of {VALID_AXIS_LIST}")
    if motion_type not in VALID_MOTION_TYPE_LIST:
        raise ValueError(f"`motion_type` should be one of {VALID_MOTION_TYPE_LIST}")
    if not all(isinstance(x, (int, float)) for x in [amplitude, frequency, phase, initial_displacement, initial_velocity]):
        raise ValueError("Motion parameters (`amplitude`, `frequency`, `phase`, `initial_displacement`, `initial_velocity`) should be numeric.")

    lines = [
        "#",
        "SET_MOTION_ROTATION",
        f"AXIS {axis}",
        f"TYPE {motion_type}",
        f"AMPLITUDE {amplitude}",
        f"FREQUENCY {frequency}",
        f"PHASE {phase}",
        f"INITIAL_DISPLACEMENT {initial_displacement}",
        f"INITIAL_VELOCITY {initial_velocity}",
    ]
    script.append_lines(lines)
    return
