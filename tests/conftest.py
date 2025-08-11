import os
import sys
import pytest

# Ensure repository root is on sys.path so `pyFlightscript` can be imported
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import pyFlightscript as pyfs


@pytest.fixture(autouse=True)
def reset_script_state():
    """Automatically reset global script state before each test."""
    pyfs.hard_reset()
    yield
    pyfs.hard_reset()


@pytest.fixture()
def script_state():
    """Return the underlying script state for assertions."""
    return pyfs.script
