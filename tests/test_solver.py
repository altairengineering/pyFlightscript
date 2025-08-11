import pyFlightscript as pyfs


def test_initialize_solver_incompressible_specific_surfaces(script_state):
    """Test initialization of incompressible solver with specific surfaces and quad flags."""
    pyfs.initialize_solver(
        solver_model='INCOMPRESSIBLE',
        surfaces=[(1, 'ENABLE'), (2, 'DISABLE')],
        wake_termination_x=3.5,
        symmetry='MIRROR',
        wall_collision_avoidance='DISABLE',
        stabilization='ENABLE',
        stabilization_strength=1.0,
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        "SOLVER_MODEL INCOMPRESSIBLE",
        "SURFACES 2",
        "1,ENABLE",
        "2,DISABLE",
        "WAKE_TERMINATION_X 3.5",
        "SYMMETRY MIRROR",
        "WALL_COLLISION_AVOIDANCE DISABLE",
        "STABILIZATION ENABLE 1.0",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_initialize_solver_subsonic_all_surfaces(script_state):
    """Test initialization of subsonic solver with all surfaces."""
    pyfs.initialize_solver(
        solver_model='SUBSONIC_PRANDTL_GLAUERT',
        surfaces=-1,
        wake_termination_x='DEFAULT',
        symmetry='MIRROR',
        wall_collision_avoidance='ENABLE',
        stabilization='DISABLE',
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        "SOLVER_MODEL SUBSONIC_PRANDTL_GLAUERT",
        "SURFACES -1",
        "WAKE_TERMINATION_X DEFAULT",
        "SYMMETRY MIRROR",
        "WALL_COLLISION_AVOIDANCE ENABLE",
        "STABILIZATION DISABLE",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_initialize_solver_transonic_periodic_symmetry(script_state):
    """Test initialization of transonic solver with periodic symmetry."""
    pyfs.initialize_solver(
        solver_model='TRANSONIC_FIELD_PANEL',
        surfaces=-1,
        wake_termination_x=3.5,
        symmetry='PERIODIC',
        symmetry_periodicity=4,
        wall_collision_avoidance='DISABLE',
        stabilization='ENABLE',
        stabilization_strength=0.5,
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        "SOLVER_MODEL TRANSONIC_FIELD_PANEL",
        "SURFACES -1",
        "WAKE_TERMINATION_X 3.5",
        "SYMMETRY PERIODIC 4",
        "WALL_COLLISION_AVOIDANCE DISABLE",
        "STABILIZATION ENABLE 0.5",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_initialize_solver_tangent_cone_no_symmetry(script_state):
    """Test initialization of tangent cone solver with no symmetry."""
    pyfs.initialize_solver(
        solver_model='TANGENT_CONE',
        surfaces=[(1, 'ENABLE'), (2, 'ENABLE')],
        symmetry='NONE',
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        "SOLVER_MODEL TANGENT_CONE",
        "SURFACES 2",
        "1,ENABLE",
        "2,ENABLE",
        "SYMMETRY NONE",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_initialize_solver_modified_newtonian(script_state):
    """Test initialization of modified Newtonian solver."""
    pyfs.initialize_solver(
        solver_model='MODIFIED_NEWTONIAN',
        surfaces=-1,
        symmetry='MIRROR',
    )
    expected_tail = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
        "INITIALIZE_SOLVER",
        "SOLVER_MODEL MODIFIED_NEWTONIAN",
        "SURFACES -1",
        "SYMMETRY MIRROR",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_solver_proximal_boundaries(script_state):
    pyfs.solver_proximal_boundaries(1, 4, 5)
    expected_tail = [
        "#************************************************************************",
        "#********* Enable solver proximity checking for specified boundaries ****",
        "#************************************************************************",
        "#",
        "SOLVER_PROXIMAL_BOUNDARIES 3",
        "1",
        "4",
        "5",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_solver_remove_initialization(script_state):
    pyfs.solver_remove_initialization()
    expected_tail = [
        "#************************************************************************",
        "#********* Remove the solver initialization *****************************",
        "#************************************************************************",
        "#",
        "REMOVE_INITIALIZATION",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail
