import os
from .utils import *    
from .script import script
from .types import *
from .types import *
from typing import Union, Optional, Literal, List

def delete_transition_trip(transition_trip_index: int) -> None:
    """
    Delete an existing transition trip edge set.

    This function appends a command to the script state to delete an existing
    boundary layer transition trip by its index.

    Parameters
    ----------
    transition_trip_index : int
        The index of the boundary layer transition trip edges to be deleted.
        Must be a positive integer.

    Raises
    ------
    ValueError
        If `transition_trip_index` is not an integer greater than 0.

    Examples
    --------
    >>> # Delete the transition trip with index 2
    >>> delete_transition_trip(transition_trip_index=2)
    """

    # Type and value checking
    if not isinstance(transition_trip_index, int) or transition_trip_index <= 0:
        raise ValueError("`transition_trip_index` should be an integer greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#************ Delete an existing transition trip edge set ***************",
        "#************************************************************************",
        "#",
        f"DELETE_TRANSITION_TRIP {transition_trip_index}"
    ]

    script.append_lines(lines)
    return
