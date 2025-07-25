from .utils import *    
from .script import script
from .types import *

def export_solver_analysis_spreadsheet(output_file):
    """
    Appends lines to script state to export the aerodynamic results to the specified file.
    

    :param output_file: Path to the output file where the aerodynamic results will be stored.
    
    Example usage:
    export_solver_analysis_spreadsheet(, 'C:\\Users\\Desktop\\Models\\scripting_test_output_data.txt')
    """
    
    # Checking for valid file path
    if not isinstance(output_file, str):
        raise ValueError("`output_file` should be a string representing a valid file path.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export the aerodynamic results **********************",
        "#************************************************************************",
        "#",
        "EXPORT_SOLVER_ANALYSIS_SPREADSHEET",
        f"{output_file}"
    ]

    script.append_lines(lines)
    return

def export_solver_analysis_tecplot(output_file):
    """
    Appends lines to script state to export the Tecplot data based on the solver results for all initialized boundaries to the specified file.
    

    :param output_file: Path to the output file where the Tecplot data will be stored.
    
    Example usage:
    export_solver_analysis_tecplot(, 'C:\\Users\\Desktop\\Models\\scripting_test_output_data.dat')
    """
    
    # Checking for valid file path
    if not isinstance(output_file, str):
        raise ValueError("`output_file` should be a string representing a valid file path.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export the Tecplot data file *************************",
        "#************************************************************************",
        "#",
        "EXPORT_SOLVER_ANALYSIS_TECPLOT",
        f"{output_file}"
    ]

    script.append_lines(lines)
    return

def export_solver_analysis_vtk(output_filepath, surfaces, boundaries=None):
    """
    Appends lines to script state to export the Visualization Toolkit (*.vtk) 
    file based on the solver results for the specified boundaries.
    

    :param output_filepath: File name with path to output file.
    :param surfaces: Number of boundaries that need to be exported, or -1 if all boundaries 
    need to be exported.
    :param boundaries: List of boundary indices to be exported, if applicable.
    
    Example usage:
    # Export the first two solver boundaries in VTK file
    export_solver_analysis_vtk(, 'C:\\Users\\Desktop\\Models\\scripting_test_output_data.vtk', 2, [1, 2])
    # Export ALL solver boundaries in VTK file
    export_solver_analysis_vtk(, 'C:\\Users\\Desktop\\Models\\scripting_test_output_data.vtk', -1)
    """

    lines = [
        "#************************************************************************",
        "#****************** Export the Visualization Toolkit (*.vtk) file *********",
        "#************************************************************************",
        "#",
        "EXPORT_SOLVER_ANALYSIS_VTK",
        output_filepath,
        f"SURFACES {surfaces}"
    ]
    
    if boundaries:
        lines.extend(map(str, boundaries))

    script.append_lines(lines)
    return

def set_vtk_export_variables(num_variables, export_wake, variables=None):
    """
    Appends lines to script state to set the variables to be exported in the VTK file.
    

    :param num_variables: Number of variables to be exported. For all variable export set value to -1
    :param export_wake: Option to export wake filaments to VTK file. Either 'ENABLE' or 'DISABLE'.
    :param variables: List of variables to be exported, if applicable.
    
    Example usage:
    # Set a custom list of export variables in VTK file
    set_vtk_export_variables(, 5, 'DISABLE', ['X', 'Y', 'Z', 'CP', 'PSTATIC'])
    # Set all variables for export in VTK file
    set_vtk_export_variables(, -1, 'ENABLE')
    """
    
    # Type and value checking
    valid_wakes = ['ENABLE', 'DISABLE']
    if export_wake not in valid_wakes:
        raise ValueError(f"export_wake should be one of {valid_wakes}")
    
    if not isinstance(num_variables, int):
        raise ValueError("`num_variables` should be an integer value.")
    
    lines = [
        "SET_VTK_EXPORT_VARIABLES",
        f"{num_variables} {export_wake}"
    ]
    
    if variables:
        lines.extend(variables)

    script.append_lines(lines)
    return

def export_solver_analysis_csv(
    file_path: str, 
    format_value: str = 'DIFFERENCE-PRESSURE', 
    units: str = 'PASCALS', 
    surfaces: int = -1, 
    frame: int = 1,
    boundary_indices: list = None
):
    """
    Appends lines to script state to export the FEM CSV based on the solver results.
    :param file_path: File name with path to file.
    :param format_value: Format of the export data. 
    :param units: Units for the exported data.
    :param surfaces: Number of boundaries to be exported or -1 for all.
    :param boundary_indices: List of boundary indices.
    
    Example usage:
    # Export the FEM CSV file for the first three boundaries
    export_solver_analysis_csv('C:\\Users\\Desktop\\Models\\scripting_test_output_data.txt',
                               surfaces=3, frame=1,
                               boundary_indices=[1,2,3])
    """

    valid_formats = ['CP-FREESTREAM', 'CP-REFERENCE', 'PRESSURE']
    valid_units = ['PASCALS', 'MEGAPASCALS', 'BAR', 'ATMOSPHERES', 'PSI']


    if format_value not in valid_formats:
        raise ValueError(f"Invalid format value. Valid formats are: {valid_formats}")

    if units not in valid_units:
        raise ValueError(f"Invalid unit type. Valid units are: {valid_units}")

    if surfaces != -1 and boundary_indices is None:
        raise ValueError("`boundary_indices` must be provided if `surfaces` is not -1.")

    if boundary_indices is not None:
        if not isinstance(boundary_indices, list):
            raise TypeError("`boundary_indices` must be a list of integers.")
        for idx in boundary_indices:
            if not isinstance(idx, int):
                raise TypeError("Each element in `boundary_indices` must be an integer.")

    lines = [
        "#************************************************************************",
        "#****************** Export the FEM CSV based on solver results **********",
        "#************************************************************************",
        "#",
        "EXPORT_SOLVER_ANALYSIS_CSV",
        file_path,
        f"FORMAT {format_value}",
        f"UNITS {units}",
        f"FRAME {frame}",
        f"SURFACES {surfaces}"
    ]

    if surfaces != -1:
        if not boundary_indices:
            raise ValueError("`boundary_indices` must be provided if `surfaces` is not -1.")
        for boundary in boundary_indices:
            lines.append(str(boundary))
    else:
        lines.append("ALL")

    script.append_lines(lines)
    return

def export_solver_analysis_pload_bdf(file_path, surfaces=-1, boundary_indices=None):
    """
    Appends lines to script state to export the NASTRAN PLOAD BDF based on the solver results.
    

    :param file_path: File name with path to file.
    :param surfaces: Number of boundaries to be exported or -1 for all.
    :param boundary_indices: List of boundary indices.
    
    Example usage:
    # Export the NASTRAN PLOAD BDF file for the first three boundaries
    export_solver_analysis_pload_bdf(, 
                                     'C:\\Users\\Desktop\\Models\\scripting_test_output_data.bdf',
                                     surfaces=3,
                                     boundary_indices=[1,2,3])
    """
    
    if not isinstance(surfaces, int):
        raise ValueError("`surfaces` should be an integer.")
    
    if surfaces != -1 and boundary_indices is None:
        raise ValueError("`boundary_indices` must be provided if `surfaces` is not -1.")
    
    lines = [
        "#************************************************************************",
        "#*********** Export the NASTRAN PLOAD BDF based on solver results *******",
        "#************************************************************************",
        "#",
        "EXPORT_SOLVER_ANALYSIS_PLOAD_BDF",
        file_path,
        f"SURFACES {surfaces}"
    ]
    
    if boundary_indices:
        for boundary in boundary_indices:
            lines.append(str(boundary))
    
    script.append_lines(lines)
    return

def export_solver_analysis_force_distributions(output_filepath, surfaces=-1, boundary_indices=None):
    """
    Appends lines to script state to export the force distribution vectors based on the solver results.
    

    :param output_filepath: Path to the output data file.
    :param surfaces: Number of boundaries that need to be exported, or -1 if all boundaries need to be exported.
    :param boundary_indices: List of boundary indices to be exported. If surfaces is not -1, this parameter must be provided.
    
    Example usage:
    export_solver_analysis_force_distributions(, 'C:\\Users\\Desktop\\Models\\scripting_test_output_data.txt', 3, [1, 2, 3])
    """
    
    # Type and value checking
    if not isinstance(surfaces, int):
        raise ValueError("`surfaces` should be an integer value.")
    
    if surfaces != -1 and boundary_indices is None:
        raise ValueError("`boundary_indices` should be provided when `surfaces` is not -1.")
    
    if boundary_indices:
        if not all(isinstance(b, int) for b in boundary_indices):
            raise ValueError("`boundary_indices` should be a list of integers.")
    
    lines = [
        "#************************************************************************",
        "#******* Export force distributions file for the selected boundaries ****",
        "#************************************************************************",
        "#",
        "EXPORT_SOLVER_ANALYSIS_FORCE_DISTRIBUTIONS",
        output_filepath,
        f"SURFACES {surfaces}"
    ]
    if boundary_indices:
        lines.extend(map(str, boundary_indices))

    script.append_lines(lines)
    return


