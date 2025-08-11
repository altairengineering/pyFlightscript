import os
import pytest

import pyFlightscript as pyfs
from pyFlightscript.types import VALID_RUN_OPTIONS, VALID_UNITS_LIST

def test_open_fsm_appends_expected_lines(script_state):
    # This test should pass because the run options are valid
    fsm_path = "tests/helper_files/model.fsm"

    pyfs.open_fsm(
        fsm_filepath=str(fsm_path),
        reset_parallel_cores='DISABLE',
        load_solver_initialization='ENABLE',
    )

    expected_tail = [
        "#************************************************************************",
        "#****************** Open an existing simulation file ********************",
        "#************************************************************************",
        "#",
        "OPEN",
        str(fsm_path),
        "LOAD_SOLVER_INITIALIZATION ENABLE",
    ]
    assert script_state.lines[-len(expected_tail):] == expected_tail


def test_open_fsm_invalid_run_option_raises(script_state):
    # These tests test invalid options being passed
    fsm_path = "tests/helper_files/model.fsm"

    with pytest.raises(ValueError):
        pyfs.open_fsm(
            fsm_filepath=str(fsm_path),
            reset_parallel_cores='NOPE',
        )

    with pytest.raises(ValueError):
        pyfs.open_fsm(
            fsm_filepath=str(fsm_path),
            load_solver_initialization='NOPE',
        )
    return


def test_open_fsm_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        pyfs.open_fsm(
            fsm_filepath="C:/does/not/exist.fsm",
        )


def test_new_simulation(script_state):
    pyfs.new_simulation()
    expected = [
        "#************************************************************************",
        "#****************** Create a new simulation *****************************",
        "#************************************************************************",
        "#",
        "NEW_SIMULATION",
    ]
    assert script_state.lines[-5:] == expected


def test_save_as_fsm(script_state, tmp_path):
    out_path = tmp_path / "out.fsm"
    pyfs.save_as_fsm(str(out_path))
    expected = [
        "#************************************************************************",
        "#****************** Save an existing simulation file ********************",
        "#************************************************************************",
        "#",
        "SAVEAS",
        str(out_path),
    ]
    assert script_state.lines[-6:] == expected


def test_set_significant_digits_valid(script_state):
    pyfs.set_significant_digits(7)
    assert script_state.lines[-1] == "SET_SIGNIFICANT_DIGITS 7"


def test_set_significant_digits_invalid_raises():
    with pytest.raises(ValueError):
        pyfs.set_significant_digits(0)
    with pytest.raises(ValueError):
        pyfs.set_significant_digits(-3)
    with pytest.raises(ValueError):
        pyfs.set_significant_digits(3.5)  # type: ignore[arg-type]


def test_set_vertex_merge_tolerance_valid(script_state):
    pyfs.set_vertex_merge_tolerance(1e-6)
    assert script_state.lines[-1] == "SET_VERTEX_MERGE_TOLERANCE 1e-06"


def test_set_vertex_merge_tolerance_invalid_raises():
    with pytest.raises(ValueError):
        pyfs.set_vertex_merge_tolerance("bad")  # type: ignore[arg-type]


def test_set_simulation_length_units_valid(script_state):
    pyfs.set_simulation_length_units('METER')
    assert script_state.lines[-1] == "SET_SIMULATION_LENGTH_UNITS METER"


def test_set_simulation_length_units_invalid_raises():
    with pytest.raises(ValueError):
        pyfs.set_simulation_length_units('YARDS')  # not in VALID_UNITS_LIST


def test_set_trailing_edge_sweep_angle_valid(script_state):
    pyfs.set_trailing_edge_sweep_angle(60)
    assert script_state.lines[-1] == "SET_TRAILING_EDGE_SWEEP_ANGLE 60"


def test_set_trailing_edge_sweep_angle_invalid_raises():
    with pytest.raises(ValueError):
        pyfs.set_trailing_edge_sweep_angle(-1)
    with pytest.raises(ValueError):
        pyfs.set_trailing_edge_sweep_angle(100)
    with pytest.raises(ValueError):
        pyfs.set_trailing_edge_sweep_angle("x")  # type: ignore[arg-type]


def test_set_trailing_edge_bluntness_angle_valid(script_state):
    pyfs.set_trailing_edge_bluntness_angle(90)
    assert script_state.lines[-1] == "SET_TRAILING_EDGE_BLUNTNESS_ANGLE 90"


def test_set_trailing_edge_bluntness_angle_invalid_raises():
    with pytest.raises(ValueError):
        pyfs.set_trailing_edge_bluntness_angle(40)
    with pytest.raises(ValueError):
        pyfs.set_trailing_edge_bluntness_angle(180)
    with pytest.raises(ValueError):
        pyfs.set_trailing_edge_bluntness_angle([])  # type: ignore[arg-type]


def test_set_base_region_bending_angle_valid(script_state):
    pyfs.set_base_region_bending_angle(30)
    assert script_state.lines[-1] == "SET_BASE_REGION_BENDING_ANGLE 30"


def test_set_base_region_bending_angle_invalid_raises():
    with pytest.raises(ValueError):
        pyfs.set_base_region_bending_angle(-1)
    with pytest.raises(ValueError):
        pyfs.set_base_region_bending_angle(100)
    with pytest.raises(ValueError):
        pyfs.set_base_region_bending_angle({})  # type: ignore[arg-type]


