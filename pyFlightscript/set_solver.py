from typing import Union, Optional, Literal, List, Tuple
from .utils import *
from .script import script
from .types import *

def steady() -> None:
    """
    Set the solver to steady mode.

    This function appends a command to the script state to configure the
    solver for a steady-state analysis.

    Examples
    --------
    >>> # Set the solver to steady mode
    >>> steady()
    """
    lines = [
        "#************************************************************************",
        "#********* Set the steady solver ****************************************",
        "#************************************************************************",
        "SET_SOLVER_STEADY"
    ]
    script.append_lines(lines)
    return

def unsteady(time_iterations: int = 100, delta_time: float = 0.1) -> None:
    """
    Set the solver to unsteady mode.

    This function appends a command to the script state to configure the
    solver for a time-dependent, unsteady analysis.

    Parameters
    ----------
    time_iterations : int, optional
        Number of time-stepping iterations, by default 100.
    delta_time : float, optional
        Physical time step for the unsteady solver, by default 0.1.

    Examples
    --------
    >>> # Set up an unsteady simulation with 200 time steps
    >>> unsteady(time_iterations=200, delta_time=0.05)
    """
    if not isinstance(time_iterations, int) or time_iterations <= 0:
        raise TypeError("`time_iterations` must be a positive integer.")
    if not isinstance(delta_time, (int, float)) or delta_time <= 0:
        raise TypeError("`delta_time` must be a positive number.")

    lines = [
        "#************************************************************************",
        "#********* Set the unsteady solver **************************************",
        "#************************************************************************",
        "SET_SOLVER_UNSTEADY",
        f"TIME_ITERATIONS {time_iterations}",
        f"DELTA_TIME {delta_time}"
    ]
    script.append_lines(lines)
    return

def unsteady_solver_new_force_plot(
    frame: int = 1,
    units: ValidForceUnits = 'NEWTONS',
    parameter: str = 'FORCE_X',
    name: str = 'Plot_Name',
    boundaries: int = -1,
    boundary_indices: Optional[List[int]] = None
) -> None:
    """
    Create a new unsteady solver force and moments plot.

    This function appends a command to the script state to generate a plot of
    force or moment data over time for specified boundaries.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system, by default 1.
    units : ValidForceUnits, optional
        Units for the plot, by default 'NEWTONS'. Must be one of
        `VALID_FORCE_UNITS_LIST`.
    parameter : str, optional
        The force or moment parameter to plot, by default 'FORCE_X'. Must be
        one of `VALID_UNSTEADY_FORCE_PLOT_PARAMETER_LIST`.
    name : str, optional
        Name of the plot, by default 'Plot_Name'.
    boundaries : int, optional
        Number of geometry boundaries to link, or -1 for all, by default -1.
    boundary_indices : Optional[List[int]], optional
        A list of boundary indices if not plotting all, by default None.

    Examples
    --------
    >>> # Plot thrust on specific boundaries
    >>> unsteady_solver_new_force_plot(
    ...     name='Propeller_thrust',
    ...     boundaries=3,
    ...     boundary_indices=[1, 2, 4]
    ... )
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` must be an integer.")
    units = normalize_option(units, "units")
    if units not in VALID_FORCE_UNITS_LIST:
        raise ValueError(f"`units` must be one of {VALID_FORCE_UNITS_LIST}")
    parameter = normalize_option(parameter, "parameter")
    if parameter not in VALID_UNSTEADY_FORCE_PLOT_PARAMETER_LIST:
        raise ValueError(f"`parameter` must be one of {VALID_UNSTEADY_FORCE_PLOT_PARAMETER_LIST}")

    lines = [
        "#************************************************************************",
        "#********* Create a new unsteady solver force & moments plot ************",
        "#************************************************************************",
        "UNSTEADY_SOLVER_NEW_FORCE_PLOT",
        f"FRAME {frame}",
        f"UNITS {units}",
        f"PARAMETER {parameter}",
        f"NAME {name}",
        f"BOUNDARIES {boundaries}"
    ]

    if boundaries != -1 and boundary_indices:
        lines.append(','.join(map(str, boundary_indices)))

    script.append_lines(lines)
    return

def unsteady_solver_new_fluid_plot(
    frame: int = 1,
    parameter: str = 'VELOCITY',
    name: str = 'Plot_Name',
    vertex: Tuple[float, float, float] = (-1.0, 1.0, 0.0)
) -> None:
    """
    Create a new unsteady solver fluid properties plot.

    This function appends a command to the script state to generate a plot of
    a fluid property over time at a specific point.

    Parameters
    ----------
    frame : int, optional
        Index of the coordinate system, by default 1.
    parameter : str, optional
        The fluid property to plot, by default 'VELOCITY'. Must be one of
        `VALID_UNSTEADY_FLUID_PLOT_PARAMETER_LIST`.
    name : str, optional
        Name of the plot, by default 'Plot_Name'.
    vertex : Tuple[float, float, float], optional
        Coordinates (x, y, z) for the measurement location,
        by default (-1.0, 1.0, 0.0).

    Examples
    --------
    >>> # Plot velocity at a specific point in the slipstream
    >>> unsteady_solver_new_fluid_plot(
    ...     name='Propeller_slipstream',
    ...     vertex=(-2.0, 1.4, 0.0)
    ... )
    """
    if not isinstance(frame, int):
        raise ValueError("`frame` must be an integer.")
    parameter = normalize_option(parameter, "parameter")
    if parameter not in VALID_UNSTEADY_FLUID_PLOT_PARAMETER_LIST:
        raise ValueError(f"`parameter` must be one of {VALID_UNSTEADY_FLUID_PLOT_PARAMETER_LIST}")

    lines = [
        "#************************************************************************",
        "#********* Create a new unsteady solver fluid properties plot ***********",
        "#************************************************************************",
        "UNSTEADY_SOLVER_NEW_FLUID_PLOT",
        f"FRAME {frame}",
        f"PARAMETER {parameter}",
        f"NAME {name}",
        f"VERTEX {' '.join(map(str, vertex))}"
    ]
    script.append_lines(lines)
    return

def unsteady_solver_export_plots(export_filepath: str) -> None:
    """
    Export all unsteady solver plots.

    This function appends a command to the script state to export all data
    from unsteady solver plots to a specified file.

    Parameters
    ----------
    export_filepath : str
        The absolute path where the plot data should be exported.

    Examples
    --------
    >>> # Export unsteady plot data
    >>> unsteady_solver_export_plots('C:/data/unsteady_plots.txt')
    """
    if not isinstance(export_filepath, str):
        raise ValueError("`export_filepath` must be a string.")

    lines = [
        "#************************************************************************",
        "#****************** Export all unsteady solver plots ********************",
        "#************************************************************************",
        "UNSTEADY_SOLVER_EXPORT_PLOTS",
        export_filepath
    ]
    script.append_lines(lines)
    return

def unsteady_solver_delete_all_plots() -> None:
    """
    Delete all unsteady solver plots.

    This function appends a command to the script state to remove all
    currently defined unsteady solver plots.

    Examples
    --------
    >>> # Delete all unsteady plots
    >>> unsteady_solver_delete_all_plots()
    """
    lines = [
        "#************************************************************************",
        "#****************** Delete all unsteady solver plots ********************",
        "#************************************************************************",
        "UNSTEADY_SOLVER_DELETE_ALL_PLOTS"
    ]
    script.append_lines(lines)
    return

def unsteady_solver_animation(
    enable_disable: RunOptions,
    folder: str,
    filetype: str,
    frequency: int,
    volume_sections: RunOptions
) -> None:
    """
    Configure the unsteady solver animation.

    This function appends a command to the script state to set up animation
    output for an unsteady simulation.

    Parameters
    ----------
    enable_disable : RunOptions
        Enable or disable the animation. Must be one of `VALID_RUN_OPTIONS`.
    folder : str
        The folder location for the output animation files.
    filetype : str
        The type of output file. Must be one of
        `VALID_ANIMATION_FILETYPE_LIST`.
    frequency : int
        The frequency of output in terms of solver time steps.
    volume_sections : RunOptions
        Enable or disable the export of volume section output files. Must be
        one of `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Enable animation output to a specific folder
    >>> unsteady_solver_animation(
    ...     'ENABLE', 'C:/animation', 'PARAVIEW_VTK', 10, 'ENABLE'
    ... )
    """
    enable_disable = normalize_option(enable_disable, "enable_disable")
    if enable_disable not in VALID_RUN_OPTIONS:
        raise ValueError(f"`enable_disable` must be one of {VALID_RUN_OPTIONS}")
    if not isinstance(folder, str):
        raise ValueError("`folder` must be a string indicating the path.")
    filetype = normalize_option(filetype, "filetype")
    if filetype not in VALID_ANIMATION_FILETYPE_LIST:
        raise ValueError(f"`filetype` must be one of {VALID_ANIMATION_FILETYPE_LIST}")
    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("`frequency` must be an integer greater than 0.")
    volume_sections = normalize_option(volume_sections, "volume_sections")
    if volume_sections not in VALID_RUN_OPTIONS:
        raise ValueError(f"`volume_sections` must be one of {VALID_RUN_OPTIONS}")

    lines = [
        "#************************************************************************",
        "#********* Set the unsteady solver animation controls *******************",
        "#************************************************************************",
        f"UNSTEADY_SOLVER_ANIMATION {enable_disable}"
    ]
    if enable_disable == 'ENABLE':
        lines.extend([
            f"FOLDER {folder}",
            f"FILETYPE {filetype}",
            f"FREQUENCY {frequency}",
            f"VOLUME_SECTIONS {volume_sections}"
        ])
    script.append_lines(lines)
    return

def boundary_layer_type(type_value: str = 'TRANSITIONAL') -> None:
    """
    Set the surface boundary layer type.

    This function appends a command to the script state to define the type of
    boundary layer model to be used in the simulation.

    Parameters
    ----------
    type_value : str, optional
        The type of boundary layer, by default 'TRANSITIONAL'. Must be one of
        `VALID_BOUNDARY_LAYER_TYPE_LIST`.

    Examples
    --------
    >>> # Set the boundary layer to turbulent
    >>> boundary_layer_type('TURBULENT')
    """
    type_value = normalize_option(type_value, "type_value")
    if type_value not in VALID_BOUNDARY_LAYER_TYPE_LIST:
        raise ValueError(f"`type_value` must be one of {VALID_BOUNDARY_LAYER_TYPE_LIST}")

    lines = [
        "#************************************************************************",
        "#****************** Set the surface boundary layer type *****************",
        "#************************************************************************",
        f"SET_BOUNDARY_LAYER_TYPE {type_value}"
    ]
    script.append_lines(lines)
    return

def surface_roughness(roughness_height: float = 23.5) -> None:
    """
    Set the surface roughness height.

    This function appends a command to the script state to specify the
    surface roughness height in nanometers.

    Parameters
    ----------
    roughness_height : float, optional
        The height of the surface roughness in nanometers, by default 23.5.

    Examples
    --------
    >>> # Set a custom surface roughness
    >>> surface_roughness(50.0)
    """
    if not isinstance(roughness_height, (int, float)) or roughness_height <= 0.0:
        raise ValueError("`roughness_height` must be a positive numeric value.")

    lines = [
        "#************************************************************************",
        "#****************** Set the surface roughness height ********************",
        "#************************************************************************",
        f"SET_SURFACE_ROUGHNESS {roughness_height}"
    ]
    script.append_lines(lines)
    return

def viscous_coupling(mode: RunOptions = 'ENABLE') -> None:
    """
    Set the solver viscous coupling.

    This function appends a command to the script state to enable or disable
    the viscous coupling in the solver.

    Parameters
    ----------
    mode : RunOptions, optional
        The mode for viscous coupling, by default 'ENABLE'. Must be one of
        `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Disable viscous coupling
    >>> viscous_coupling('DISABLE')
    """
    mode = normalize_option(mode, "mode")
    if mode not in VALID_RUN_OPTIONS:
        raise ValueError(f"`mode` must be one of {VALID_RUN_OPTIONS}")

    lines = [
        "#************************************************************************",
        "#****************** Set the solver viscous coupling ********************",
        "#************************************************************************",
        f"SET_SOLVER_VISCOUS_COUPLING {mode}"
    ]
    script.append_lines(lines)
    return

def viscous_excluded_boundaries(num_boundaries: int, boundaries: List[int]) -> None:
    """
    Set the viscous exclusion boundary list.

    This function appends a command to the script state to exclude specified
    boundaries from the viscous calculation.

    Parameters
    ----------
    num_boundaries : int
        The number of boundaries being excluded.
    boundaries : List[int]
        A list of indices of the boundaries to be excluded.

    Examples
    --------
    >>> # Exclude boundaries 1, 2, and 4 from viscous calculations
    >>> viscous_excluded_boundaries(3, [1, 2, 4])
    """
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` must be an integer.")
    if not isinstance(boundaries, list) or not all(isinstance(b, int) for b in boundaries):
        raise ValueError("`boundaries` must be a list of integers.")
    if len(boundaries) != num_boundaries:
        raise ValueError("`num_boundaries` must match the length of the `boundaries` list.")

    lines = [
        "#************************************************************************",
        "#************** Set the viscous exclusion boundary list ****************",
        "#************************************************************************",
        f"SET_VISCOUS_EXCLUDED_BOUNDARIES {num_boundaries}",
        ",".join(map(str, boundaries))
    ]
    script.append_lines(lines)
    return

def delete_viscous_excluded_boundaries() -> None:
    """
    Delete the viscous exclusion boundary list.

    This function appends a command to the script state to clear the list of
    boundaries that are excluded from viscous calculations.

    Examples
    --------
    >>> # Clear the viscous exclusion list
    >>> delete_viscous_excluded_boundaries()
    """
    lines = [
        "#************************************************************************",
        "#************** Delete the viscous exclusion boundary list **************",
        "#************************************************************************",
        "DELETE_VISCOUS_EXCLUDED_BOUNDARIES"
    ]
    script.append_lines(lines)
    return

def set_axial_separation_boundaries(boundary_indices: Union[int, List[int]]) -> None:
    """
    Set axial separation boundaries.

    This function appends a command to the script state to define which
    boundaries are subject to axial flow separation.

    Parameters
    ----------
    boundary_indices : Union[int, List[int]]
        A single boundary index or a list of boundary indices.

    Examples
    --------
    >>> # Set a single axial separation boundary
    >>> set_axial_separation_boundaries(3)

    >>> # Set multiple axial separation boundaries
    >>> set_axial_separation_boundaries([1, 2, 5])
    """
    if isinstance(boundary_indices, list):
        num_boundaries = len(boundary_indices)
        indices_str = ",".join(map(str, boundary_indices))
    elif isinstance(boundary_indices, int):
        num_boundaries = 1
        indices_str = str(boundary_indices)
    else:
        raise ValueError("`boundary_indices` must be an integer or a list of integers.")

    lines = [
        "#************************************************************************",
        "#************** Set the axial flow separation boundary list *************",
        "#************************************************************************",
        f"SET_AXIAL_SEPARATION_BOUNDARIES {num_boundaries}",
        indices_str
    ]
    script.append_lines(lines)
    return

def delete_axial_separation_boundaries() -> None:
    """
    Delete all axial flow separation boundaries.

    This function appends a command to the script state to clear the list of
    axial flow separation boundaries.

    Examples
    --------
    >>> # Clear all axial separation boundaries
    >>> delete_axial_separation_boundaries()
    """
    lines = [
        "#************************************************************************",
        "#************** Delete the axial flow separation boundary list **********",
        "#************************************************************************",
        "DELETE_AXIAL_SEPARATION_BOUNDARIES"
    ]
    script.append_lines(lines)
    return

def set_crossflow_separation_boundaries(boundary_indices: List[int]) -> None:
    """
    Set cross-flow separation boundaries.

    This function appends a command to the script state to define which
    boundaries are subject to cross-flow separation.

    Parameters
    ----------
    boundary_indices : List[int]
        A list of boundary indices to be added to the cross-flow separation
        boundaries list.

    Examples
    --------
    >>> # Set boundaries 3, 4, and 5 for cross-flow separation
    >>> set_crossflow_separation_boundaries([3, 4, 5])
    """
    if not isinstance(boundary_indices, list) or not all(isinstance(idx, int) for idx in boundary_indices):
        raise ValueError("`boundary_indices` must be a list of integers.")

    boundary_count = len(boundary_indices)
    lines = [
        "#************************************************************************",
        "#************** Set the cross-flow separation boundary list *************",
        "#************************************************************************",
        f"SET_CROSSFLOW_SEPARATION_BOUNDARIES {boundary_count}",
        ",".join(map(str, boundary_indices))
    ]
    script.append_lines(lines)
    return

def delete_crossflow_separation_boundaries() -> None:
    """
    Delete all cross-flow separation boundaries.

    This function appends a command to the script state to clear the list of
    cross-flow separation boundaries.

    Examples
    --------
    >>> # Clear all cross-flow separation boundaries
    >>> delete_crossflow_separation_boundaries()
    """
    lines = [
        "#************************************************************************",
        "#************** Delete the cross-flow separation boundary list **********",
        "#************************************************************************",
        "DELETE_CROSSFLOW_SEPARATION_BOUNDARIES"
    ]
    script.append_lines(lines)
    return

def aoa(angle: float) -> None:
    """
    Set the solver angle of attack (AOA).

    This function appends a command to the script state to set the angle of
    attack for the simulation.

    Parameters
    ----------
    angle : float
        The angle of attack in degrees. The absolute value must be less than 90.

    Examples
    --------
    >>> # Set the angle of attack to 5 degrees
    >>> aoa(5.0)

    >>> # Set a negative angle of attack
    >>> aoa(-2.5)
    """
    if not isinstance(angle, (int, float)) or abs(angle) >= 90:
        raise ValueError("`angle` must be a number with an absolute value less than 90.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver AOA *******************************************",
        "#************************************************************************",
        f"SOLVER_SET_AOA {angle}"
    ]
    script.append_lines(lines)
    return

def sideslip(angle: float) -> None:
    """
    Set the solver sideslip angle.

    This function appends a command to the script state to set the sideslip
    angle for the simulation.

    Parameters
    ----------
    angle : float
        The sideslip angle in degrees. The absolute value must be less than 90.

    Examples
    --------
    >>> # Set the sideslip angle to 3 degrees
    >>> sideslip(3.0)

    >>> # Set a negative sideslip angle
    >>> sideslip(-1.5)
    """
    if not isinstance(angle, (int, float)) or abs(angle) >= 90:
        raise ValueError("`angle` must be a number with an absolute value less than 90.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver Side-slip angle *******************************",
        "#************************************************************************",
        f"SOLVER_SET_SIDESLIP {angle}"
    ]
    script.append_lines(lines)
    return

def solver_velocity(velocity: float = 30.0) -> None:
    """
    Set the solver free-stream velocity.

    This function appends a command to the script state to define the
    free-stream velocity for the simulation.

    Parameters
    ----------
    velocity : float, optional
        The free-stream velocity value, by default 30.0.

    Examples
    --------
    >>> # Set the freestream velocity to 50.0
    >>> solver_velocity(50.0)
    """
    if not isinstance(velocity, (int, float)):
        raise ValueError("`velocity` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver free-stream velocity **************************",
        "#************************************************************************",
        f"SOLVER_SET_VELOCITY {velocity}"
    ]
    script.append_lines(lines)
    return

def solver_mach_number(mach: float = 3.0) -> None:
    """
    Set the solver Mach number.

    This function appends a command to the script state to define the
    Mach number for the simulation.

    Parameters
    ----------
    mach : float, optional
        The Mach number, by default 3.0.

    Examples
    --------
    >>> # Set the Mach number to 0.8
    >>> solver_mach_number(0.8)
    """
    if not isinstance(mach, (int, float)):
        raise ValueError("`mach` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#************** Set the solver Mach number ******************************",
        "#************************************************************************",
        f"SOLVER_SET_MACH_NUMBER {mach}"
    ]
    script.append_lines(lines)
    return

def solver_iterations(num_iterations: int = 500) -> None:
    """
    Set the solver iterations.

    This function appends a command to the script state to define the
    number of iterations for the solver to perform.

    Parameters
    ----------
    num_iterations : int, optional
        The number of solver iterations, by default 500.

    Examples
    --------
    >>> # Set the solver to run for 1000 iterations
    >>> solver_iterations(1000)
    """
    if not isinstance(num_iterations, int):
        raise ValueError("`num_iterations` must be an integer.")

    lines = [
        "#************************************************************************",
        "#****************** Set the solver iterations ***************************",
        "#************************************************************************",
        f"SOLVER_SET_ITERATIONS {num_iterations}"
    ]
    script.append_lines(lines)
    return

def convergence_threshold(threshold: float = 1e-5) -> None:
    """
    Set the solver convergence threshold.

    This function appends a command to the script state to define the
    convergence criterion for the solver.

    Parameters
    ----------
    threshold : float, optional
        The convergence threshold value, by default 1e-5.

    Examples
    --------
    >>> # Set a tighter convergence threshold
    >>> convergence_threshold(1e-6)
    """
    if not isinstance(threshold, (int, float)):
        raise ValueError("`threshold` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#****************** Set the solver convergence threshold ****************",
        "#************************************************************************",
        f"SOLVER_SET_CONVERGENCE {threshold}"
    ]
    script.append_lines(lines)
    return

def forced_iterations(mode: RunOptions = 'ENABLE') -> None:
    """
    Enable or disable solver forced iterations mode.

    This function appends a command to the script state to force the solver
    to run for the full number of specified iterations, regardless of
    convergence.

    Parameters
    ----------
    mode : RunOptions, optional
        The mode for forced iterations, by default 'ENABLE'. Must be one of
        `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Disable forced iterations
    >>> forced_iterations('DISABLE')
    """
    mode = normalize_option(mode, "mode")
    if mode not in VALID_RUN_OPTIONS:
        raise ValueError(f"`mode` must be one of {VALID_RUN_OPTIONS}")

    lines = [
        "#************************************************************************",
        "#****************** Enable solver forced iterations mode ****************",
        "#************************************************************************",
        f"SOLVER_SET_FORCED_ITERATIONS {mode}"
    ]
    script.append_lines(lines)
    return

def ref_velocity(value: float = 100.0) -> None:
    """
    Set the solver reference velocity.

    This function appends a command to the script state to define the
    reference velocity used for calculating aerodynamic coefficients.

    Parameters
    ----------
    value : float, optional
        The reference velocity, by default 100.0.

    Examples
    --------
    >>> # Set the reference velocity to 150.0
    >>> ref_velocity(150.0)
    """
    if not isinstance(value, (int, float)):
        raise ValueError("`value` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver reference velocity ****************************",
        "#************************************************************************",
        f"SOLVER_SET_REF_VELOCITY {value}"
    ]
    script.append_lines(lines)
    return

def ref_mach_number(mach: float = 3.0) -> None:
    """
    Set the solver reference Mach number.

    This function appends a command to the script state to define the
    reference Mach number for the simulation.

    Parameters
    ----------
    mach : float, optional
        The reference Mach number, by default 3.0.

    Examples
    --------
    >>> # Set the reference Mach number to 0.9
    >>> ref_mach_number(0.9)
    """
    if not isinstance(mach, (int, float)):
        raise ValueError("`mach` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#*************** Set the solver reference Mach number *******************",
        "#************************************************************************",
        f"SOLVER_SET_REF_MACH_NUMBER {mach}"
    ]
    script.append_lines(lines)
    return

def ref_area(value: float = 1.0) -> None:
    """
    Set the solver reference area.

    This function appends a command to the script state to define the
    reference area used for calculating aerodynamic coefficients.

    Parameters
    ----------
    value : float, optional
        The reference area, by default 1.0.

    Examples
    --------
    >>> # Set the reference area to 2.5
    >>> ref_area(2.5)
    """
    if not isinstance(value, (int, float)):
        raise ValueError("`value` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver reference area ********************************",
        "#************************************************************************",
        f"SOLVER_SET_REF_AREA {value}"
    ]
    script.append_lines(lines)
    return

def ref_length(length: float = 1.0) -> None:
    """
    Set the solver reference length.

    This function appends a command to the script state to define the
    reference length used for calculating aerodynamic coefficients.

    Parameters
    ----------
    length : float, optional
        The reference length, by default 1.0.

    Examples
    --------
    >>> # Set the reference length to 3.0
    >>> ref_length(3.0)
    """
    if not isinstance(length, (int, float)):
        raise ValueError("`length` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver reference length ******************************",
        "#************************************************************************",
        f"SOLVER_SET_REF_LENGTH {length}"
    ]
    script.append_lines(lines)
    return

def solver_minimum_cp(cp_min: float = -100.0) -> None:
    """
    Set the solver minimum coefficient of pressure.

    This function appends a command to the script state to define the minimum
    allowed coefficient of pressure in the solver.

    Parameters
    ----------
    cp_min : float, optional
        The minimum coefficient of pressure, by default -100.0.

    Examples
    --------
    >>> # Set a custom minimum Cp
    >>> solver_minimum_cp(-50.0)
    """
    if not isinstance(cp_min, (int, float)):
        raise ValueError("`cp_min` must be a numeric value.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver minimum coefficient of pressure ***************",
        "#************************************************************************",
        f"SOLVER_MINIMUM_CP {cp_min}"
    ]
    script.append_lines(lines)
    return

def set_max_parallel_threads(num_cores: int = 16) -> None:
    """
    Set the number of solver parallel cores.

    This function appends a command to the script state to specify the number
    of parallel threads to be used by the solver.

    Parameters
    ----------
    num_cores : int, optional
        The number of parallel cores, by default 16.

    Examples
    --------
    >>> # Set the solver to use 8 cores
    >>> set_max_parallel_threads(8)
    """
    if not isinstance(num_cores, int):
        raise ValueError("`num_cores` must be an integer.")

    lines = [
        "#************************************************************************",
        "#*********** Set maximum solver parallel cores ***************************",
        "#************************************************************************",
        f"SET_MAX_PARALLEL_THREADS {num_cores}"
    ]
    script.append_lines(lines)
    return

def mesh_induced_wake_velocity(enable: bool = True) -> None:
    """
    Set the solver mesh induced wake velocity.

    This function appends a command to the script state to enable or disable
    the mesh-induced wake velocity feature.

    Parameters
    ----------
    enable : bool, optional
        Enable or disable the feature, by default True.

    Examples
    --------
    >>> # Disable mesh-induced wake velocity
    >>> mesh_induced_wake_velocity(False)
    """
    status = "ENABLE" if enable else "DISABLE"
    lines = [
        "#************************************************************************",
        "#********* Set the solver mesh induced wake velocity ********************",
        "#************************************************************************",
        f"SOLVER_SET_MESH_INDUCED_WAKE_VELOCITY {status}"
    ]
    script.append_lines(lines)
    return

def farfield_layers(value: int = 3) -> None:
    """
    Set the solver far-field agglomeration layers.

    This function appends a command to the script state to define the number
    of far-field agglomeration layers for the solver.

    Parameters
    ----------
    value : int, optional
        The number of far-field layers (between 1 and 5), by default 3.

    Examples
    --------
    >>> # Set the number of far-field layers to 4
    >>> farfield_layers(4)
    """
    if not (1 <= value <= 5):
        raise ValueError("`value` must be an integer between 1 and 5.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver far-field agglomeration layers ****************",
        "#************************************************************************",
        f"SOLVER_SET_FARFIELD_LAYERS {value}"
    ]
    script.append_lines(lines)
    return

def solver_unsteady_pressure_and_kutta(status: RunOptions = 'ENABLE') -> None:
    """
    Enable or disable solver unsteady Bernoulli and Kutta terms.

    This function appends a command to the script state to control the
    unsteady Bernoulli and Kutta terms in the solver.

    Parameters
    ----------
    status : RunOptions, optional
        The status of the unsteady pressure and Kutta terms, by default
        'ENABLE'. Must be one of `VALID_RUN_OPTIONS`.

    Examples
    --------
    >>> # Disable unsteady Bernoulli and Kutta terms
    >>> solver_unsteady_pressure_and_kutta('DISABLE')
    """
    status = normalize_option(status, "status")
    if status not in VALID_RUN_OPTIONS:
        raise ValueError(f"`status` must be one of {VALID_RUN_OPTIONS}")

    lines = [
        "#************************************************************************",
        "#********* Enable solver unsteady Bernoulli and Kutta terms *************",
        "#************************************************************************",
        f"SOLVER_UNSTEADY_PRESSURE_AND_KUTTA {status}"
    ]
    script.append_lines(lines)
    return

def convergence_iterations(value: int = 500) -> None:
    """
    Set the solver convergence iterations.

    This function appends a command to the script state to define the number
    of iterations the solver must run after crossing the convergence threshold.

    Parameters
    ----------
    value : int, optional
        The number of convergence iterations, by default 500.

    Examples
    --------
    >>> # Set the convergence iterations to 100
    >>> convergence_iterations(100)
    """
    if not isinstance(value, int):
        raise ValueError("`value` must be an integer.")

    lines = [
        "#************************************************************************************",
        "#************** Set the solver convergence iterations *********************************",
        "#************************************************************************************",
        f"SET_SOLVER_CONVERGENCE_ITERATIONS {value}"
    ]
    script.append_lines(lines)
    return

def wake_termination_time_steps(value: int) -> None:
    """
    Set the wake termination time-steps value.

    This function appends a command to the script state to define the number
    of time steps after which a wake vortex filament edge is removed.

    Parameters
    ----------
    value : int
        The number of time steps for wake termination.

    Examples
    --------
    >>> # Set wake termination to 50 time steps
    >>> wake_termination_time_steps(50)
    """
    if not isinstance(value, int):
        raise ValueError("`value` must be an integer.")

    lines = [
        "#************************************************************************************",
        "#************** Set the wake termination time-steps value ***************************",
        "#************************************************************************************",
        f"SET_WAKE_TERMINATION_TIME_STEPS {value}"
    ]
    script.append_lines(lines)
    return


def set_valarezo_separation_boundaries(boundary_indices: Union[int, list]) -> None:
    """
    Appends lines to script state to set Valarezo separation boundaries.

    :param boundary_indices: List of boundary indices, or -1 to apply to all boundaries.
    """

    if isinstance(boundary_indices, int) and boundary_indices == -1:
        lines = [
            "#**************************************************************************************",
            "#***************** Set the Valarezo separation boundary list ***************************",
            "#**************************************************************************************",
            "SET_VALAREZO_SEPARATION_BOUNDARIES -1"
        ]
    elif isinstance(boundary_indices, list):
        if not all(isinstance(idx, int) for idx in boundary_indices):
            raise ValueError("All elements in `boundary_indices` should be integers.")

        lines = [
            "#**************************************************************************************",
            "#***************** Set the Valarezo separation boundary list ***************************",
            "#**************************************************************************************",
            f"SET_VALAREZO_SEPARATION_BOUNDARIES {len(boundary_indices)}",
            ",".join(map(str, boundary_indices))
        ]
    else:
        raise ValueError("`boundary_indices` should be a list of integers, or -1.")

    script.append_lines(lines)
    return


def delete_valarezo_separation_boundaries() -> None:
    """
    Appends lines to script state to delete all Valarezo separation boundaries.
    """

    lines = [
        "#**************************************************************************************",
        "#************** Delete the Valarezo separation boundary list ***************************",
        "#**************************************************************************************",
        "DELETE_VALAREZO_SEPARATION_BOUNDARIES"
    ]

    script.append_lines(lines)
    return


def set_crossflow_separation_diameter(value: Union[int, float]) -> None:
    """
    Appends lines to script state to set the maximum diameter for cross-flow separation model.

    :param value: Maximum diameter of the geometric body on which cross-flow separation is set (> 0).
    """

    if not isinstance(value, (int, float)):
        raise ValueError("`value` should be a numeric value (integer or float).")

    if value <= 0:
        raise ValueError("`value` should be greater than zero.")

    lines = [
        "#**************************************************************************************",
        "#************** Set maximum diameter for crossflow separation model *******************",
        "#**************************************************************************************",
        f"SET_CROSSFLOW_SEPARATION_DIAMETER {value}"
    ]

    script.append_lines(lines)
    return


def set_crossflow_separation_axisymmetric(status: str = 'ENABLE') -> None:
    """
    Appends lines to script state to enable cross-flow separation axisymmetric vortex shedding.

    :param status: Can be 'ENABLE' or 'DISABLE'.
    """

    status = normalize_option(status, "status")
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")

    lines = [
        "#**************************************************************************************",
        "#************** Enable cross-flow separation axisymmetric vortex shedding *************",
        "#**************************************************************************************",
        f"SET_CROSSFLOW_SEPARATION_AXISYMMETRIC {status}"
    ]

    script.append_lines(lines)
    return


def kutta_joukowski_lift_forces(status: str = 'ENABLE') -> None:
    """
    Appends lines to script state to set Kutta-Joukowski inviscid lift forces.

    :param status: Can be 'ENABLE' or 'DISABLE'.
    """

    status = normalize_option(status, "status")
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")

    lines = [
        "#************************************************************************",
        "#************* Set the Kutta-Joukowski inviscid lift forces *************",
        "#************************************************************************",
        f"KUTTA_JOUKOWSKI_LIFT_FORCES {status}"
    ]

    script.append_lines(lines)
    return


def laminar_separation(status: str = 'ENABLE') -> None:
    """
    Appends lines to script state to set laminar boundary layer separation.

    :param status: Can be 'ENABLE' or 'DISABLE'.
    """

    status = normalize_option(status, "status")
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")

    lines = [
        "#************************************************************************",
        "#*************** Set Laminar boundary layer separation ******************",
        "#************************************************************************",
        f"LAMINAR_SEPARATION {status}"
    ]

    script.append_lines(lines)
    return


def print_rotor_induced_velocities(status: str = 'ENABLE') -> None:
    """
    Appends lines to script state to print rotor-induced velocities per time step.

    :param status: Can be 'ENABLE' or 'DISABLE'.
    """

    status = normalize_option(status, "status")
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")

    lines = [
        "#************************************************************************",
        "#*********** Print rotor-induced velocities per time step ***************",
        "#************************************************************************",
        f"PRINT_ROTOR_INDUCED_VELOCITIES {status}"
    ]

    script.append_lines(lines)
    return


def additional_wake_relaxation_iteration(status: str = 'ENABLE') -> None:
    """
    Appends lines to script state to perform an additional wake relaxation iteration.

    :param status: Can be 'ENABLE' or 'DISABLE'.
    """

    status = normalize_option(status, "status")
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")

    lines = [
        "#************************************************************************",
        "#*********** Perform additional wake relaxation iteration ***************",
        "#************************************************************************",
        f"ADDITIONAL_WAKE_RELAXATION_ITERATION {status}"
    ]

    script.append_lines(lines)
    return

