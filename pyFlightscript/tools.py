from .utils import *    
from .script import script
from .types import *

def execute_solver_sweeper(results_filename, surface_results_path='', 
                           angle_of_attack='ENABLE', side_slip_angle='DISABLE', 
                           velocity='DISABLE', angle_of_attack_start=0.0, 
                           angle_of_attack_stop=0., angle_of_attack_delta=1.,
                           side_slip_angle_start=0., side_slip_angle_stop=0., 
                           side_slip_angle_delta=1.0, velocity_start=0., 
                           velocity_stop=0.0, velocity_delta=1.0, 
                           export_surface_data_per_step='ENABLE', 
                           clear_solution_after_each_run='ENABLE',
                           reference_velocity_equals_freestream='ENABLE',
                           append_to_existing_sweep='DISABLE'):
    """
    Appends lines to script state to execute the solver sweeper.
    :param results_filename (str): The full file path name of the sweep results file.
    :param surface_results_path (str): The path to export surface data per step if 'ENABLE'.

    Example usage:
    execute_solver_sweeper(results_filename='C:\...\sweep_results\sweep.txt', 
                           surface_results_path='C:\...\surface_data\', angle_of_attack='ENABLE', 
                           side_slip_angle='DISABLE', velocity='DISABLE', 
                           angle_of_attack_start=0.0, angle_of_attack_stop=10.0,
                           angle_of_attack_delta=1.0, export_surface_data_per_step='ENABLE',
                           surface_results_path='C:\\...\\sweep_results\\', 
                           clear_solution_after_each_run='ENABLE')
    

    """
    
    # Type and value checking
    valid_options = ['ENABLE', 'DISABLE']
    if angle_of_attack not in valid_options or side_slip_angle not in valid_options or \
       velocity not in valid_options or export_surface_data_per_step not in valid_options or \
       clear_solution_after_each_run not in valid_options or \
       reference_velocity_equals_freestream not in valid_options or \
       append_to_existing_sweep not in valid_options:
        raise ValueError("Only 'ENABLE' or 'DISABLE' are valid options for the respective fields.")
    
    # Create lines based on the given values
    lines = [
        "#************************************************************************",
        "#****************** Initialize and execute the solver sweeper ***********",
        "#************************************************************************",
        "#",
        "EXECUTE_SOLVER_SWEEPER",
        f"ANGLE_OF_ATTACK {angle_of_attack}",
        f"SIDE_SLIP_ANGLE {side_slip_angle}",
        f"VELOCITY {velocity}",
        f"ANGLE_OF_ATTACK_START {angle_of_attack_start}",
        f"ANGLE_OF_ATTACK_STOP {angle_of_attack_stop}",
        f"ANGLE_OF_ATTACK_DELTA {angle_of_attack_delta}",
        f"SIDE_SLIP_ANGLE_START {side_slip_angle_start}",
        f"SIDE_SLIP_ANGLE_STOP {side_slip_angle_stop}",
        f"SIDE_SLIP_ANGLE_DELTA {side_slip_angle_delta}",
        f"VELOCITY_START {velocity_start}",
        f"VELOCITY_STOP {velocity_stop}",
        f"VELOCITY_DELTA {velocity_delta}",
        f"EXPORT_SURFACE_DATA_PER_STEP {export_surface_data_per_step}",
        ]

    # Only add surface_results_path if EXPORT_SURFACE_DATA_PER_STEP is ENABLE
    if export_surface_data_per_step == 'ENABLE' and surface_results_path:
        lines.append(f"{surface_results_path}")

    lines.extend([
        f"CLEAR_SOLUTION_AFTER_EACH_RUN {clear_solution_after_each_run}",
        f"REFERENCE_VELOCITY_EQUALS_FREESTREAM {reference_velocity_equals_freestream}",
        f"APPEND_TO_EXISTING_SWEEP {append_to_existing_sweep}",
        f"{results_filename}"
    ])

    script.append_lines(lines)
    return

def stability_toolbox_settings(ROTATION_FRAME=1, UNITS='PER_RADIAN', 
                               CLEAR_SOLVER_PER_RUN='DISABLE', ANGULAR_RATE_INCREMENT=0.1):
    """
    Appends lines to script state to set the S&C toolbox parameters.

    :param ROTATION_FRAME: Index of the coordinate system used for applying rotation rates.
                           Default is 1 for reference coordinate system.
    :param UNITS: PER_RADIAN or PER_DEGREE (only for dynamic stability coefficients).
    :param CLEAR_SOLVER_PER_RUN: ENABLE or DISABLE clearing of the solution prior to each solver run.
    :param ANGULAR_RATE_INCREMENT: Incremental angular rate (rad/sec) to be applied about the three axes 
                                   of the specified rotation coordinate system for dynamic coefficients.

    Example usage:
    stability_toolbox_settings(3, 'PER_RADIAN', 'DISABLE', 0.2)
    """
    
    valid_units = ['PER_RADIAN', 'PER_DEGREE']
    valid_options = ['ENABLE', 'DISABLE']
    
    if not isinstance(ROTATION_FRAME, int):
        raise ValueError("`ROTATION_FRAME` should be an integer value.")

    if UNITS not in valid_units:
        raise ValueError(f"`UNITS` should be one of {valid_units}")

    if CLEAR_SOLVER_PER_RUN not in valid_options:
        raise ValueError(f"`CLEAR_SOLVER_PER_RUN` should be one of {valid_options}")

    if not isinstance(ANGULAR_RATE_INCREMENT, (int, float)):
        raise ValueError("`ANGULAR_RATE_INCREMENT` should be an integer or float value.")
        
    lines = [
        "#************************************************************************",
        "#****************** Set the S&C toolbox parameters here *****************",
        "#************************************************************************",
        "#",
        "STABILITY_TOOLBOX_SETTINGS",
        f"{ROTATION_FRAME}",
        f"{UNITS}",
        f"{CLEAR_SOLVER_PER_RUN}",
        f"{ANGULAR_RATE_INCREMENT}"
    ]

    script.append_lines(lines)
    return

def stability_toolbox_new_coefficient(FRAME, UNITS, NUMERATOR, DENOMINATOR, CONSTANT, NAME, BOUNDARIES):
    """
    Appends lines to script state to define a new Stability & Control (S&C) coefficient.

    :param FRAME: Index of the coordinate system for computing the coefficient's numerator variable.
    :param UNITS: One of: COEFFICIENTS, NEWTONS, KILO-NEWTONS, POUND-FORCE, KILOGRAM-FORCE
    :param NUMERATOR: One of: CL,CDI,CDO,CD,FORCE_X,FORCE_Y,FORCE_Z,MOMENT_X,MOMENT_Y,MOMENT_Z
    :param DENOMINATOR: One of: AOA,BETA,ROTX,ROTY,ROTZ
    :param CONSTANT: Value of the constant to multiply to the basic derivative term.
    :param NAME: Name of the user-defined coefficient.
    :param BOUNDARIES: Geometry boundaries linked to this coefficient's numerator variable.
    
    Example usage:
    stability_toolbox_new_coefficient(NAME='CLq', NUMERATOR='CL', DENOMINATOR='ROTY', FRAME=2, CONSTANT=208.7, BOUNDARIES=-1)
    """

    valid_units = ['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE']
    if UNITS not in valid_units:
        raise ValueError(f"`UNITS` should be one of {valid_units}")

    valid_numerators = ['CL', 'CDI', 'CDO', 'CD', 'FORCE_X', 'FORCE_Y', 'FORCE_Z', 'MOMENT_X', 'MOMENT_Y', 'MOMENT_Z']
    if NUMERATOR not in valid_numerators:
        raise ValueError(f"`NUMERATOR` should be one of {valid_numerators}")

    valid_denominators = ['AOA', 'BETA', 'ROTX', 'ROTY', 'ROTZ']
    if DENOMINATOR not in valid_denominators:
        raise ValueError(f"`DENOMINATOR` should be one of {valid_denominators}")

    if not isinstance(CONSTANT, (int, float)):
        raise ValueError("`CONSTANT` should be an integer or float value.")

    lines = [
        "#************************************************************************",
        "#********* Create a new S&C Coefficient *********************************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_NEW_COEFFICIENT",
        f"NAME {NAME}",
        f"NUMERATOR {NUMERATOR}",
        f"DENOMINATOR {DENOMINATOR}",
        f"FRAME {FRAME}",
        f"CONSTANT {CONSTANT}",
        f"BOUNDARIES {BOUNDARIES}"
    ]

    if BOUNDARIES != -1:
        boundaries_list = ",".join(map(str, BOUNDARIES))
        lines.append(boundaries_list)

    script.append_lines(lines)
    return

def stability_toolbox_delete_all():
    """
    Appends lines to script state to delete all S&C toolbox coefficients.

    Example usage:
    stability_toolbox_delete_all()
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Delete all S&C Toolbox coefficients *****************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_DELETE_ALL"
    ]

    script.append_lines(lines)
    return

def compute_stability_coefficients():
    """
    Appends lines to script state to compute the stability coefficients.
    
    Example usage:
    compute_stability_coefficients()
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Compute the stability coefficients ******************",
        "#************************************************************************",
        "COMPUTE_STABILITY_COEFFICIENTS"
    ]

    script.append_lines(lines)
    return

def stability_toolbox_export(filename):
    """
    Appends lines to script state to export the S&C toolbox results to an external file.

    :param filename: Path of the file where S&C toolbox results should be exported.

    Example usage:
    stability_toolbox_export(r'C:\...\Testing cases\test_stability.txt')
    """
    
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string representing the path.")
    lines = [
        "#************************************************************************",
        "#*********** Export the S&C toolbox results to external file ************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_EXPORT",
        filename
    ]

    script.append_lines(lines)
    return
