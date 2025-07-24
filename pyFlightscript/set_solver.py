from .utils import *    
from .script import script
from .types import ValidForceUnits, VALID_FORCE_UNITS_LIST, RunOptions

def steady():
    """
    Appends lines to script state to set the steady solver.
    
    Example usage:
        steady()
    """
    
    lines = [
        
        "#************************************************************************",
        "#********* Set the steady solver ****************************************",
        "#************************************************************************",
        "#",
        "SET_SOLVER_STEADY"
    ]

    script.append_lines(lines)
    return

def unsteady(time_iterations: int = 100, delta_time: float = 0.1):
    """
    Appends lines to script state to set the unsteady solver.

    :param time_iterations: Number of time-stepping iterations to be run by the unsteady solver.
    :param delta_time: Physical time step of the unsteady solver.

    Example usage:
        unsteady()
    """

    # Type and value checking
    if type(time_iterations) is not int or time_iterations <= 0:
        raise TypeError("`time_iterations` should be a positive integer value.")

    if type(delta_time) not in (int, float) or delta_time <= 0:
        raise TypeError("`delta_time` should be a positive number.")

    lines = [
        "#************************************************************************",
        "#********* Set the unsteady solver **************************************",
        "#************************************************************************",
        "#",
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
    boundary_indices: list = None
):
    """
    Appends lines to script state to create a new unsteady solver force & moments plot.

    :param frame: Index of the coordinate system to be used.
    :param units: Units for the plot.
    :param parameter: The force or moment parameter.
    :param name: Name of the plot.
    :param boundaries: Total geometry boundaries to be linked.
    :param boundary_indices: List of boundary indices.

    Example usage:
    unsteady_solver_new_force_plot(, name='Propeller_thrust', boundaries=3, boundary_indices=[1, 2, 4])
    """

    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")

    if units not in VALID_FORCE_UNITS_LIST:
        raise ValueError(f"`units` should be one of {VALID_FORCE_UNITS_LIST}")

    valid_parameters = [
        'CL', 'CDI', 'CDO', 'CD',
        'FORCE_X', 'FORCE_Y', 'FORCE_Z',
        'MOMENT_X', 'MOMENT_Y', 'MOMENT_Z'
    ]
    if parameter not in valid_parameters:
        raise ValueError(f"`parameter` should be one of {valid_parameters}")

    lines = [
        "#************************************************************************",
        "#********* Create a new unsteady solver force & moments plot ************",
        "#************************************************************************",
        "#",
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
    vertex: tuple = (-1.0, 1.0, 0.0)
):
    """
    Appends lines to script state to create a new unsteady solver fluid properties plot.
    

    :param frame: Index of the coordinate system to be used.
    :param parameter: The fluid property parameter.
    :param name: Name of the plot.
    :param vertex: Vertex coordinates for the fluid property measurement location.
    
    Example usage:
    unsteady_solver_new_fluid_plot(, name='Propeller_slipstream', vertex=(-2.0, 1.4, 0.0))
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_parameters = ['CP_FREE', 'CP_REF', 'MACH', 'VELOCITY', 'VX', 'VY', 'VZ', 'STATIC_PRESSURE_RATIO']
    if parameter not in valid_parameters:
        raise ValueError(f"`parameter` should be one of {valid_parameters}")
    
    lines = [
        "#************************************************************************",
        "#********* Create a new unsteady solver fluid properties plot ***********",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_NEW_FLUID_PLOT",
        f"FRAME {frame}",
        f"PARAMETER {parameter}",
        f"NAME {name}",
        f"VERTEX {' '.join(map(str, vertex))}"
    ]

    script.append_lines(lines)
    return

def unsteady_solver_export_plots(export_filepath: str):
    """
    Appends lines to script state to export all unsteady solver plots.


    :param export_filepath: Path where plots should be exported.
    
    Example usage:
    unsteady_solver_export_plots(, 'C:\\Users\\Desktop\\Models\\my_exported_data.txt')
    """
    
    # Prepare the lines to be written to file
    lines = [
        "#************************************************************************",
        "#****************** Export all unsteady solver plots ********************",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_EXPORT_PLOTS",
        export_filepath
    ]

    script.append_lines(lines)
    return

def unsteady_solver_delete_all_plots():
    """
    Appends lines to script state to delete all unsteady solver plots.
    

    
    Example usage:
    unsteady_solver_delete_all_plots()
    """
    
    # Prepare the lines to be written to file
    lines = [
        "#************************************************************************",
        "#****************** Delete all unsteady solver plots ********************",
        "#************************************************************************",
        "#",
        "UNSTEADY_SOLVER_DELETE_ALL_PLOTS"
    ]

    script.append_lines(lines)
    return

def unsteady_solver_animation(
    enable_disable: RunOptions,
    folder: str,
    filetype: str,
    frequency: int,
    volume_sections: str
):
    """
    Appends lines to script state to configure the unsteady solver animation.

    :param enable_disable: 'ENABLE' or 'DISABLE' to control the animation.
    :param folder: Folder location for output files.
    :param filetype: Type of output file (e.g., 'SOLVER_BITMAP', 'PLOTS_BITMAP', 'TECPLOT_DATA', 'PARAVIEW_VTK').
    :param frequency: Frequency of outputs in terms of solver time steps.
    :param volume_sections: 'ENABLE' or 'DISABLE' the export of volume section output files.
    """
    
    if not isinstance(folder, str):
        raise ValueError("`folder` must be a string indicating the path.")

    if filetype not in ['SOLVER_BITMAP', 'PLOTS_BITMAP', 'TECPLOT_DATA', 'PARAVIEW_VTK']:
        raise ValueError("`filetype` must be one of: 'SOLVER_BITMAP', 'PLOTS_BITMAP', 'TECPLOT_DATA', 'PARAVIEW_VTK'.")

    if not isinstance(frequency, int) or frequency < 1:
        raise ValueError("`frequency` must be an integer greater than 0.")

    if volume_sections not in ['ENABLE', 'DISABLE']:
        raise ValueError("`volume_sections` must be 'ENABLE' or 'DISABLE'.")

    lines = [
        "#************************************************************************",
        "#********* Set the unsteady solver animation controls *******************",
        "#************************************************************************",
        f"UNSTEADY_SOLVER_ANIMATION {enable_disable}"
    ]
    
    if enable_disable == 'ENABLE':
        lines += [
            f"FOLDER {folder}",
            f"FILETYPE {filetype}",
            f"FREQUENCY {frequency}",
            f"VOLUME_SECTIONS {volume_sections}"
        ]

    script.append_lines(lines)
    return

def boundary_layer_type(type_value: str = 'TRANSITIONAL'):
    """
    Appends lines to script state to set the surface boundary layer type.
    

    :param type_value: Type of the boundary layer (default: 'TRANSITIONAL').
    
    Example usage:
    set_boundary_layer_type()
    """
    
    # Type and value checking
    valid_types = ['LAMINAR', 'TRANSITIONAL', 'TURBULENT']
    if type_value not in valid_types:
        raise ValueError(f"`type_value` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the surface boundary layer type *****************",
        "#************************************************************************",
        "#",
        f"SET_BOUNDARY_LAYER_TYPE {type_value}"
    ]
    
    script.append_lines(lines)
    return

def surface_roughness(roughness_height: float = 23.5):
    """
    Appends lines to script state to set the surface roughness height.
    

    :param roughness_height: Height of the surface roughness in nano-meters (default: 23.5 nm).
    
    Example usage:
    set_surface_roughness()
    """
    
    # Type and value checking
    if not isinstance(roughness_height, (int, float)) or roughness_height <= 0.0:
        raise ValueError("`roughness_height` should be a positive integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the surface roughness height ********************",
        "#************************************************************************",
        "#",
        f"SET_SURFACE_ROUGHNESS {roughness_height}"
    ]
    
    script.append_lines(lines)
    return

def viscous_coupling(mode: RunOptions = 'ENABLE'):
    """
    Appends lines to script state to set the solver viscous coupling.


    :param mode: The mode to set the solver viscous coupling, either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    viscous_coupling()
    """

    lines = [
        "#************************************************************************",
        "#****************** Set the solver viscous coupling ********************",
        "#************************************************************************",
        "#",
        f"SET_SOLVER_VISCOUS_COUPLING {mode}"
    ]

    script.append_lines(lines)
    return

def viscous_excluded_boundaries(num_boundaries: int, boundaries: list):
    """
    Appends lines to script state to set the viscous exclusion boundary list.


    :param num_boundaries: Number of boundaries being excluded.
    :param boundaries: List of indices of boundaries being excluded.
    
    Example usage:
    set_viscous_excluded_boundaries(, 3, [1, 2, 4])
    """
    
    # Type and value checking
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` should be an integer value.")

    if not isinstance(boundaries, list) or not all(isinstance(b, int) for b in boundaries):
        raise ValueError("`boundaries` should be a list of integers.")

    if len(boundaries) != num_boundaries:
        raise ValueError("`num_boundaries` should match the number of boundaries provided.")

    lines = [
        "#************************************************************************",
        "#************** Set the viscous exclusion boundary list ****************",
        "#************************************************************************",
        "#",
        f"SET_VISCOUS_EXCLUDED_BOUNDARIES {num_boundaries}",
        ",".join(map(str, boundaries))
    ]

    script.append_lines(lines)
    return

def delete_viscous_excluded_boundaries():
    """
    Appends lines to script state to delete the viscous exclusion boundary list.
    """

    lines = [
        "#************************************************************************",
        "#************** Delete the viscous exclusion boundary list **************",
        "#************************************************************************",
        "#",
        "DELETE_VISCOUS_EXCLUDED_BOUNDARIES"
    ]

    script.append_lines(lines)
    return

def unsteady_viscous_coupling_iteration(num_iteration: int):
    """
    Appends a line to script state to set the unsteady solver viscous-coupling iteration.

    :param num_iteration: The unsteady solver time-stepping iteration where the viscous-coupling is to be enabled.
    """
        
    # Create command line
    line = [
        "#************************************************************************",
        "#************** Set the unsteady-solver viscous-coupling iteration ******",
        "#************************************************************************",
        "#",
        f"SET_UNSTEADY_VISCOUS_COUPLING_ITERATION {num_iteration}"
    ]
    
    script.append_lines(line)
    return

def set_axial_separation_boundaries(boundary_indices: list):
    """
    Appends lines to script state to set axial separation boundaries based on given indices.

    :param boundary_indices: List of boundary indices to be set as axial separation boundaries.
    """
    
    # Type and value checking
    if  isinstance(boundary_indices, list):
        num_boundaries = len(boundary_indices)
        indices_str = ",".join(map(str, boundary_indices))
    elif isinstance(boundary_indices, int):
        num_boundaries = 1
        indices_str = str(boundary_indices)
    else:
        raise ValueError("`boundary_indices` should be a list or integer.")
    
    lines = [
        "#************************************************************************",
        "#************** Set the axial flow separation boundary list *************",
        "#************************************************************************",
        "#",
        f"SET_AXIAL_SEPARATION_BOUNDARIES {num_boundaries}",
        indices_str
    ]

    script.append_lines(lines)
    return

def delete_axial_separation_boundaries():
    """
    Appends lines to script state to delete all axial flow separation boundaries.
    """
    
    lines = [
        "#************************************************************************",
        "#************** Delete the axial flow separation boundary list **********",
        "#************************************************************************",
        "#",
        "DELETE_AXIAL_SEPARATION_BOUNDARIES"
    ]

    script.append_lines(lines)
    return

def set_crossflow_separation_boundaries(boundary_indices: list):
    """
    Appends lines to script state to set cross-flow separation boundaries.

    :param boundary_indices: List of boundary indices to be added to the cross-flow separation boundaries list.
    """
    
    # Type and value checking
    if not isinstance(boundary_indices, list):
        raise ValueError("`boundary_indices` should be a list of integer values.")
    
    if not all(isinstance(idx, int) for idx in boundary_indices):
        raise ValueError("All elements in `boundary_indices` should be integers.")
    
    boundary_count = len(boundary_indices)
    
    lines = [
        "#************************************************************************",
        "#************** Set the cross-flow separation boundary list *************",
        "#************************************************************************",
        "#",
        f"SET_CROSSFLOW_SEPARATION_BOUNDARIES {boundary_count}",
        ",".join(map(str, boundary_indices))
    ]

    script.append_lines(lines)
    return

def delete_crossflow_separation_boundaries():
    """
    Appends lines to script state to delete all cross-flow separation boundaries.
    """
    lines = [
        "#************************************************************************",
        "#************** Delete the cross-flow separation boundary list **********",
        "#************************************************************************",
        "#",
        "DELETE_CROSSFLOW_SEPARATION_BOUNDARIES"
    ]

    script.append_lines(lines)
    return

def set_crossflow_separation_cp(mean_diameter: float):
    """
    Appends lines to script state to set the cross-flow separation pressure coefficient based on mean diameter.

    :param mean_diameter: Mean diameter of the geometric body on which cross-flow separation is to be used (> 0).
    """
    
    # Type and value checking
    if not isinstance(mean_diameter, (int, float)):
        raise ValueError("`mean_diameter` should be a numeric value (integer or float).")
    
    if mean_diameter <= 0:
        raise ValueError("`mean_diameter` should be greater than zero.")
    
    lines = [
        "#************************************************************************",
        "#********** Set the cross-flow separation pressure coefficient **********",
        "#************************************************************************",
        "#",
        f"SET_CROSSFLOW_SEPARATION_CP {mean_diameter}"
    ]

    script.append_lines(lines)
    return

def solver_settings(angle_of_attack: float = 0., sideslip_angle: float = 0., 
                    freestream_velocity: float = 100., iterations: int = 500, 
                    convergence_limit: float = 1e-5, forced_run: RunOptions = 'DISABLE', 
                    reference_velocity: float = 100., 
                    reference_area: float = 1., reference_length: float = 1., processors: int = 2, 
                    wake_size: float = 1000):
    """
    Appends lines to script state to set the solver settings.
    
    Example usage:
        solver_settings()
    """
    # Type and value checking
    if not isinstance(angle_of_attack, (int, float)) or abs(angle_of_attack) >= 90:
        raise ValueError("`angle_of_attack` should be a number with |angle| < 90.")
    
    if not isinstance(sideslip_angle, (int, float)) or abs(sideslip_angle) >= 90:
        raise ValueError("`sideslip_angle` should be a number with |angle| < 90.")
    
    if not isinstance(freestream_velocity, (int, float)):
        raise ValueError("`freestream_velocity` should be a number.")
    
    if not isinstance(iterations, int):
        raise ValueError("`iterations` should be an integer value.")
    
    if not isinstance(reference_velocity, (int, float)):
        raise ValueError("`reference_velocity` should be a number.")
    
    if not isinstance(reference_area, (int, float)):
        raise ValueError("`reference_area` should be a number.")
    
    if not isinstance(reference_length, (int, float)):
        raise ValueError("`reference_length` should be a number.")
    
    if not isinstance(processors, int):
        raise ValueError("`processors` should be an integer value.")
    
    if not isinstance(wake_size, (int, float)):
        raise ValueError("`wake_size` should be a number.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver settings **************************************",
        "#************************************************************************",
        "#",
        "SOLVER_SETTINGS",
        f"ANGLE_OF_ATTACK {angle_of_attack}",
        f"SIDESLIP_ANGLE {sideslip_angle}",
        f"FREESTREAM_VELOCITY {freestream_velocity}",
        f"ITERATIONS {iterations}",
        f"CONVERGENCE_LIMIT {convergence_limit}",
        f"FORCED_RUN {forced_run}",
        f"REFERENCE_VELOCITY {reference_velocity}",
        f"REFERENCE_AREA {reference_area}",
        f"REFERENCE_LENGTH {reference_length}",
        f"PROCESSORS {processors}",
        f"WAKE_SIZE {wake_size}"
    ]

    script.append_lines(lines)
    return

def set_aoa(angle: float):
    """
    Appends lines to script state to set the solver AOA.
    
    :param angle: Angle of attack in degrees. |angle| must be < 90.
    
    Example usage:
    set_aoa(-5.0)
    """

    if abs(angle) >= 90:
        raise ValueError("`angle` must be less than 90 in magnitude.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver AOA *******************************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_AOA {angle}"
    ]
    
    script.append_lines(lines)
    return

def sideslip(angle: float):
    """
    Appends lines to script state to set the solver Side-slip angle.
    

    :param angle: Side-slip angle in degrees. |angle| must be < 90.
    
    Example usage:
    set_sideslip(, 5.0)
    """
    
    if abs(angle) >= 90:
        raise ValueError("`angle` must be less than 90 in magnitude.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver Side-slip angle *******************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_SIDESLIP {angle}"
    ]
    
    script.append_lines(lines)
    return

def velocity(velocity: float = 30.0):
    """
    Appends lines to script state to set the solver free-stream velocity.
    

    :param velocity: The free-stream velocity value.
    
    Example usage:
    set_velocity(30.)
    """
    
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver free-stream velocity **************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_VELOCITY {velocity}"
    ]

    script.append_lines(lines)
    return

def mach_number(mach: float = 3.0):
    """
    Appends lines to script state to set the solver Mach number.
    

    :param velocity: The Mach number value.
    
    Example usage:
    mach_number(3.)
    """
    

    lines = [
        "#************************************************************************",
        "#************** Set the solver Mach number ******************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_MACH_NUMBER {mach}"
    ]

    script.append_lines(lines)
    return

def iterations(num_iterations: int = 500):
    """
    Appends lines to script state to set the solver iterations.
    

    :param num_iterations: The number of solver iterations.
    
    Example usage:
    set_iterations()
    """
    

    lines = [
        "#************************************************************************",
        "#****************** Set the solver iterations ***************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_ITERATIONS {num_iterations}"
    ]

    script.append_lines(lines)
    return

def convergence(threshold: float = 1E-5):
    """
    Appends lines to script state to set the solver convergence threshold.
    

    :param threshold: Convergence threshold value.
    
    Example usage:
    set_convergence()
    """
    

    lines = [
        "#************************************************************************",
        "#****************** Set the solver convergence threshold ****************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_CONVERGENCE {threshold}"
    ]

    script.append_lines(lines)
    return

def forced_iterations(mode: RunOptions = 'ENABLE'):
    """
    Appends lines to script state to enable or disable solver forced iterations mode.
    

    :param mode: Either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    set_forced_iterations()
    """
    

    lines = [
        "#************************************************************************",
        "#****************** Enable solver forced iterations mode ****************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_FORCED_ITERATIONS {mode}"
    ]

    script.append_lines(lines)
    return

def ref_velocity(value: float = 100.):
    """
    Appends lines to script state to set the solver reference velocity.
    

    :param value: Reference velocity.
    
    Example usage:
    set_ref_velocity()
    """
    

    lines = [
        "#************************************************************************",
        "#********* Set the solver reference velocity ****************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_REF_VELOCITY {value}"
    ]

    script.append_lines(lines)
    return

def ref_mach_number(mach: float = 3.0):
    """
    Appends lines to script state to set the solver reference Mach number.
    

    :param velocity: The Mach number value.
    
    Example usage:
    ref_mach_number(3.)
    """
    
    lines = [
        "#************************************************************************",
        "#*************** Set the solver reference Mach number *******************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_REF_MACH_NUMBER {mach}"
    ]

    script.append_lines(lines)
    return

def ref_area(value: float = 1.):
    """
    Appends lines to script state to set the solver reference area.
    

    :param value: Reference area.
    
    Example usage:
    set_ref_area()
    """
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver reference area ********************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_REF_AREA {value}"
    ]

    script.append_lines(lines)
    return

def ref_length(length: float = 1.):
    """
    Appends lines to script state to set the solver reference length.
    

    :param length: Reference length.
    
    Example usage:
    set_ref_length(, length=2.5)
    """

    lines = [
        "#************************************************************************",
        "#********* Set the solver reference length ******************************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_REF_LENGTH {length}"
    ]

    script.append_lines(lines)
    return

def solver_minimum_cp(CP: float = -100):
    """
    Appends lines to script state to set the solver minimum coefficient of pressure.

    :param CP: Minimum coefficient of pressure used by the solver. Default is -100.

    Example usage:
    solver_minimum_cp(-100)
    """
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver minimum coefficient of pressure ***************",
        "#************************************************************************",
        "#",
        f"SOLVER_MINIMUM_CP {CP}"
    ]

    script.append_lines(lines)
    return

def set_max_parallel_threads(num_cores: int = 16):
    """
    Appends lines to script state to set the number of solver parallel cores.
    
    Example usage:
    set_max_parallel_threads()
    
    :param num_cores: Number of parallel cores.
    """
    
    lines = [
        "#************************************************************************",
        "#*********** Set maximum solver parallel cores ***************************",
        "#************************************************************************",
        "#",
        f"SET_MAX_PARALLEL_THREADS {num_cores}"
    ]

    script.append_lines(lines)
    return

def mesh_induced_wake_velocity(enable: bool = True):
    """
    Appends lines to script state to set the solver mesh induced wake velocity.
    
    Example usage:
    set_mesh_induced_wake_velocity()
    

    :param enable: Boolean to either enable or disable the feature.
    """
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver mesh induced wake velocity ********************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_MESH_INDUCED_WAKE_VELOCITY {status}"
    ]

    script.append_lines(lines)
    return

def adverse_gradient_boundary_layer(mode: RunOptions = 'ENABLE'):
    """
    Appends lines to script state to set the adverse pressure gradient boundary layer mode.


    :param mode: Mode to set the adverse pressure gradient boundary layer. ('ENABLE' or 'DISABLE')
    
    Example usage:
    set_adverse_gradient_boundary_layer(, 'DISABLE')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Set the adverse pressure gradient boundary layer mode ********",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_ADVERSE_GRADIENT_BOUNDARY_LAYER {mode}"
    ]

    script.append_lines(lines)
    return

def farfield_layers(value: int = 3):
    """
    Appends lines to script state to set the solver far-field agglomeration layers.


    :param value: Number of farfield layers. (Default is 3)
    
    Example usage:
    set_farfield_layers(, 4)
    """
    
    if not (1 <= value <= 5):
        raise ValueError("`value` should be between 1 and 5, inclusive.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver far-field agglomeration layers ****************",
        "#************************************************************************",
        "#",
        f"SOLVER_SET_FARFIELD_LAYERS {value}"
    ]

    script.append_lines(lines)
    return

def solver_unsteady_pressure_and_kutta(status: RunOptions = 'ENABLE'):
    """
    Appends lines to script state to enable or disable solver unsteady Bernoulli and Kutta terms.
    

    :param status: Can be 'ENABLE' or 'DISABLE'.
    
    Example usage:
    solver_unsteady_pressure_and_kutta(, status='ENABLE')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver unsteady Bernoulli and Kutta terms *************",
        "#************************************************************************",
        "#",
        f"SOLVER_UNSTEADY_PRESSURE_AND_KUTTA {status}"
    ]
    
    script.append_lines(lines)
    return

def solver_vortex_ring_normalization(status: RunOptions = 'ENABLE'):
    """
    Appends lines to script state to enable or disable solver vortex ring normalization.
    

    :param status: Can be 'ENABLE' or 'DISABLE'.
    
    Example usage:
    solver_vortex_ring_normalization(, status='ENABLE')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver vortex ring normalization **********************",
        "#************************************************************************",
        "#",
        f"SOLVER_VORTEX_RING_NORMALIZATION {status}"
    ]
    
    script.append_lines(lines)
    return

def convergence_iterations(value: int = 500):
    """
    Appends lines to script state to set the solver convergence iterations.
    

    :param value: Number of iterations the solver must run after crossing the convergence threshold.
    
    Example usage:
    convergence_iterations()
    """
    
    lines = [
        "#************************************************************************************",
        "#************** Set the solver convergence iterations *********************************",
        "#************************************************************************************",
        "#",
        f"SET_SOLVER_CONVERGENCE_ITERATIONS {value}"
    ]

    script.append_lines(lines)
    return

def wake_streamwise_agglomeration(enable: bool = True):
    """
    Appends lines to script state to enable/disable the wake-->streamwise agglomeration feature.
    

    :param enable: Boolean value to enable or disable the wake-->streamwise agglomeration feature.
    
    Example usage:
    set_wake_streamwise_agglomeration()
    """
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Enable the wake-->streamwise agglomeration feature ************",
        "#************************************************************************",
        "#",
        f"SET_WAKE_STREAMWISE_AGGLOMERATION {status}"
    ]

    script.append_lines(lines)
    return

def wake_termination_time_steps(value: int):
    """
    Sets the number of time steps after which a wake vortex filament edge loses all of its strength and is removed from the simulation.

    :param value: Integer representing the number of time steps for wake termination.
    """
    
    # Command generation
    lines = [
        "#************************************************************************************",
        "#************** Set the wake termination time-steps value ***************************",
        "#************************************************************************************",
        "#",
        f"SET_WAKE_TERMINATION_TIME_STEPS {value}"
    ]

    # Append lines to script
    script.append_lines(lines)
    return

def wake_relaxation(enable: bool):
    """
    Appends lines to script state to set the wake-relaxation feature either to ENABLE or DISABLE.

    :param enable: Boolean value; True to ENABLE, False to DISABLE the wake-relaxation feature.
    """
    
    # Determine the setting based on the boolean value
    setting = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Set the wake-relaxation feature ******************************",
        "#************************************************************************",
        "#",
        f"SET_WAKE_RELAXATION {setting}"
    ]
    
    script.append_lines(lines)
    return
