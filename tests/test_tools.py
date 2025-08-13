import pyFlightscript as pyfs


def test_execute_solver_sweeper_basic_appends_expected_lines(script_state):
    pyfs.execute_solver_sweeper(
        results_filename="fs_output/results.csv",
        angle_of_attack='ENABLE',
        side_slip_angle='DISABLE',
        velocity='DISABLE',
        angle_of_attack_start=-3,
        angle_of_attack_stop=6,
        angle_of_attack_delta=1,
        side_slip_angle_start=0.0,
        side_slip_angle_stop=0.0,
        side_slip_angle_delta=1.0,
        velocity_start=0.0,
        velocity_stop=0.0,
        velocity_delta=1.0,
        export_surface_data_per_step='DISABLE',
        clear_solution_after_each_run='DISABLE',
        reference_velocity_equals_freestream='ENABLE',
        append_to_existing_sweep='DISABLE',
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize and execute the solver sweeper ***********",
        "#************************************************************************",
        "EXECUTE_SOLVER_SWEEPER",
        "ANGLE_OF_ATTACK ENABLE",
        "SIDE_SLIP_ANGLE DISABLE",
        "VELOCITY DISABLE",
        "ANGLE_OF_ATTACK_START -3",
        "ANGLE_OF_ATTACK_STOP 6",
        "ANGLE_OF_ATTACK_DELTA 1",
        "SIDE_SLIP_ANGLE_START 0.0",
        "SIDE_SLIP_ANGLE_STOP 0.0",
        "SIDE_SLIP_ANGLE_DELTA 1.0",
        "VELOCITY_START 0.0",
        "VELOCITY_STOP 0.0",
        "VELOCITY_DELTA 1.0",
        "EXPORT_SURFACE_DATA_PER_STEP DISABLE",
        "CLEAR_SOLUTION_AFTER_EACH_RUN DISABLE",
        "REFERENCE_VELOCITY_EQUALS_FREESTREAM ENABLE",
        "APPEND_TO_EXISTING_SWEEP DISABLE",
        "fs_output/results.csv",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_execute_solver_sweeper_with_surface_export(script_state):
    pyfs.execute_solver_sweeper(
        results_filename="fs_output/results.csv",
        angle_of_attack='ENABLE',
        side_slip_angle='DISABLE',
        velocity='DISABLE',
        angle_of_attack_start=0.0,
        angle_of_attack_stop=10.0,
        angle_of_attack_delta=1.0,
        side_slip_angle_start=0.0,
        side_slip_angle_stop=0.0,
        side_slip_angle_delta=1.0,
        velocity_start=0.0,
        velocity_stop=0.0,
        velocity_delta=1.0,
        export_surface_data_per_step='VTK',
        surface_results_path="fs_output/surface",
        clear_solution_after_each_run='ENABLE',
        reference_velocity_equals_freestream='ENABLE',
        append_to_existing_sweep='DISABLE',
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize and execute the solver sweeper ***********",
        "#************************************************************************",
        "EXECUTE_SOLVER_SWEEPER",
        "ANGLE_OF_ATTACK ENABLE",
        "SIDE_SLIP_ANGLE DISABLE",
        "VELOCITY DISABLE",
        "ANGLE_OF_ATTACK_START 0.0",
        "ANGLE_OF_ATTACK_STOP 10.0",
        "ANGLE_OF_ATTACK_DELTA 1.0",
        "SIDE_SLIP_ANGLE_START 0.0",
        "SIDE_SLIP_ANGLE_STOP 0.0",
        "SIDE_SLIP_ANGLE_DELTA 1.0",
        "VELOCITY_START 0.0",
        "VELOCITY_STOP 0.0",
        "VELOCITY_DELTA 1.0",
        "EXPORT_SURFACE_DATA_PER_STEP VTK",
        "fs_output/surface",
        "CLEAR_SOLUTION_AFTER_EACH_RUN ENABLE",
        "REFERENCE_VELOCITY_EQUALS_FREESTREAM ENABLE",
        "APPEND_TO_EXISTING_SWEEP DISABLE",
        "fs_output/results.csv",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_execute_solver_sweeper_mach_sweep(script_state):
    pyfs.execute_solver_sweeper(
        results_filename="fs_output/mach_results.csv",
        angle_of_attack='DISABLE',
        side_slip_angle='DISABLE',
        velocity='ENABLE',
        velocity_mode='MACH',
        angle_of_attack_start=0.0,
        angle_of_attack_stop=0.0,
        angle_of_attack_delta=1.0,
        side_slip_angle_start=0.0,
        side_slip_angle_stop=0.0,
        side_slip_angle_delta=1.0,
        velocity_start=0.0,
        velocity_stop=1.0,
        velocity_delta=0.1,
        export_surface_data_per_step='DISABLE',
        clear_solution_after_each_run='ENABLE',
        reference_velocity_equals_freestream='ENABLE',
        append_to_existing_sweep='DISABLE',
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize and execute the solver sweeper ***********",
        "#************************************************************************",
        "EXECUTE_SOLVER_SWEEPER",
        "ANGLE_OF_ATTACK DISABLE",
        "SIDE_SLIP_ANGLE DISABLE",
        "VELOCITY ENABLE",
        "ANGLE_OF_ATTACK_START 0.0",
        "ANGLE_OF_ATTACK_STOP 0.0",
        "ANGLE_OF_ATTACK_DELTA 1.0",
        "SIDE_SLIP_ANGLE_START 0.0",
        "SIDE_SLIP_ANGLE_STOP 0.0",
        "SIDE_SLIP_ANGLE_DELTA 1.0",
        "MACH_START 0.0",
        "MACH_STOP 1.0",
        "MACH_DELTA 0.1",
        "EXPORT_SURFACE_DATA_PER_STEP DISABLE",
        "CLEAR_SOLUTION_AFTER_EACH_RUN ENABLE",
        "REFERENCE_VELOCITY_EQUALS_FREESTREAM ENABLE",
        "APPEND_TO_EXISTING_SWEEP DISABLE",
        "fs_output/mach_results.csv",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_stability_toolbox_settings_appends_expected_lines(script_state):
    pyfs.stability_toolbox_settings(
        rotation_frame=1,
        units='PER_RADIAN',
        clear_solver_per_run='DISABLE',
        angular_rate_increment=0.25,
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Set the S&C toolbox parameters here *****************",
        "#************************************************************************",
        "#",
        "STABILITY_TOOLBOX_SETTINGS",
        "ROTATION_FRAME 1",
        "UNITS PER_RADIAN",
        "CLEAR_SOLVER_PER_RUN DISABLE",
        "ANGULAR_RATE_INCREMENT 0.25",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_stability_toolbox_new_coefficient_boundaries_all(script_state):
    pyfs.stability_toolbox_new_coefficient(
        frame=1,
        units='NEWTONS',
        numerator='CL',
        denominator='AOA',
        constant=1.0,
        name='LiftCoeff',
        boundaries=-1,
    )
    expected_tail = [
        "#************************************************************************",
        "#********* Create a new S&C Coefficient *********************************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_NEW_COEFFICIENT",
        "NAME LiftCoeff",
        "NUMERATOR CL",
        "DENOMINATOR AOA",
        "FRAME 1",
        "CONSTANT 1.0",
        "BOUNDARIES -1",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_stability_toolbox_new_coefficient_specific_boundaries(script_state):
    pyfs.stability_toolbox_new_coefficient(
        frame=2,
        units='KILOGRAM-FORCE',
        numerator='FORCE_X',
        denominator='ROTX',
        constant=0.75,
        name='ThrustDeriv',
        boundaries=[1, 2, 4],
    )
    expected_tail = [
        "#************************************************************************",
        "#********* Create a new S&C Coefficient *********************************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_NEW_COEFFICIENT",
        "NAME ThrustDeriv",
        "NUMERATOR FORCE_X",
        "DENOMINATOR ROTX",
        "FRAME 2",
        "CONSTANT 0.75",
        "BOUNDARIES 3",
        "1,2,4",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_stability_toolbox_delete_all_appends_expected_lines(script_state):
    pyfs.stability_toolbox_delete_all()
    expected_tail = [
        "#************************************************************************",
        "#****************** Delete all S&C Toolbox coefficients *****************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_DELETE_ALL",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_compute_stability_coefficients_appends_expected_lines(script_state):
    pyfs.compute_stability_coefficients()
    expected_tail = [
        "#************************************************************************",
        "#****************** Compute the stability coefficients ******************",
        "#************************************************************************",
        "COMPUTE_STABILITY_COEFFICIENTS",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_stability_toolbox_export_appends_expected_lines(script_state):
    pyfs.stability_toolbox_export("fs_output/stability.csv")
    expected_tail = [
        "#************************************************************************",
        "#*********** Export the S&C toolbox results to external file ************",
        "#************************************************************************",
        "STABILITY_TOOLBOX_EXPORT",
        "fs_output/stability.csv",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail
