import pytest
import pyFlightscript as pyfs


def test_set_solver_steady(script_state):
    pyfs.steady()
    expected = [
        "#************************************************************************",
        "#********* Set the steady solver ****************************************",
        "#************************************************************************",
        "#",
        "SET_SOLVER_STEADY",
    ]
    assert script_state.lines[-5:] == expected


def test_set_solver_unsteady(script_state):
    pyfs.unsteady(time_iterations=200, delta_time=0.05)
    expected_tail = [
        "#************************************************************************",
        "#********* Set the unsteady solver **************************************",
        "#************************************************************************",
        "#",
        "SET_SOLVER_UNSTEADY",
        "TIME_ITERATIONS 200",
        "DELTA_TIME 0.05",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_unsteady_solver_new_force_plot_all_boundaries(script_state):
    pyfs.unsteady_solver_new_force_plot(
        frame=1,
        units='NEWTONS',
        parameter='FORCE_X',
        name='Propeller_thrust',
        boundaries=-1,
    )
    expected_tail = [
        "#************************************************************************",
        "#********* Create a new unsteady solver force & moments plot ************",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_NEW_FORCE_PLOT",
        "FRAME 1",
        "UNITS NEWTONS",
        "PARAMETER FORCE_X",
        "NAME Propeller_thrust",
        "BOUNDARIES -1",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_unsteady_solver_new_force_plot_specific_boundaries(script_state):
    pyfs.unsteady_solver_new_force_plot(
        frame=2,
        units='NEWTONS',
        parameter='FORCE_Z',
        name='Tail_Load',
        boundaries=3,
        boundary_indices=[1, 4, 5],
    )
    expected_tail = [
        "#************************************************************************",
        "#********* Create a new unsteady solver force & moments plot ************",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_NEW_FORCE_PLOT",
        "FRAME 2",
        "UNITS NEWTONS",
        "PARAMETER FORCE_Z",
        "NAME Tail_Load",
        "BOUNDARIES 3",
        "1,4,5",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_unsteady_solver_new_fluid_plot(script_state):
    pyfs.unsteady_solver_new_fluid_plot(
        frame=1,
        parameter='VELOCITY',
        name='Centerline_Velocity',
        vertex=(-2.0, 1.4, 0.0),
    )
    expected_tail = [
        "#************************************************************************",
        "#********* Create a new unsteady solver fluid properties plot ***********",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_NEW_FLUID_PLOT",
        "FRAME 1",
        "PARAMETER VELOCITY",
        "NAME Centerline_Velocity",
        "VERTEX -2.0 1.4 0.0",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_unsteady_solver_export_plots(script_state, tmp_path):
    out = tmp_path / "unsteady_plots.txt"
    pyfs.unsteady_solver_export_plots(str(out))
    expected_tail = [
        "#************************************************************************",
        "#****************** Export all unsteady solver plots ********************",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_EXPORT_PLOTS",
        str(out),
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_unsteady_solver_delete_all_plots(script_state):
    pyfs.unsteady_solver_delete_all_plots()
    expected_tail = [
        "#************************************************************************",
        "#****************** Delete all unsteady solver plots ********************",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_DELETE_ALL_PLOTS",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_unsteady_solver_animation_enable(script_state, tmp_path):
    folder = str(tmp_path)
    pyfs.unsteady_solver_animation(
        enable_disable='ENABLE',
        folder=folder,
        filetype='PARAVIEW_VTK',
        frequency=10,
        volume_sections='ENABLE',
    )
    expected_tail = [
        "#************************************************************************",
        "#********* Set the unsteady solver animation controls *******************",
        "#************************************************************************",
        "UNSTEADY_SOLVER_ANIMATION ENABLE",
        f"FOLDER {folder}",
        "FILETYPE PARAVIEW_VTK",
        "FREQUENCY 10",
        "VOLUME_SECTIONS ENABLE",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_boundary_layer_type(script_state):
    pyfs.boundary_layer_type('TURBULENT')
    expected_tail = [
        "#************************************************************************",
        "#****************** Set the surface boundary layer type *****************",
        "#************************************************************************",
        "#",
        "SET_BOUNDARY_LAYER_TYPE TURBULENT",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_surface_roughness(script_state):
    pyfs.surface_roughness(50.0)
    expected_tail = [
        "#************************************************************************",
        "#****************** Set the surface roughness height ********************",
        "#************************************************************************",
        "#",
        "SET_SURFACE_ROUGHNESS 50.0",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_viscous_coupling(script_state):
    pyfs.viscous_coupling('DISABLE')
    expected_tail = [
        "#************************************************************************",
        "#****************** Set the solver viscous coupling ********************",
        "#************************************************************************",
        "#",
        "SET_SOLVER_VISCOUS_COUPLING DISABLE",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail
