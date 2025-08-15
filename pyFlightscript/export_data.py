from .utils import *    
from .script import script
from .types import *
from typing import Optional, List

def export_solver_analysis_spreadsheet(output_file: str) -> None:
    """
    Export aerodynamic results to a spreadsheet file.

    This function appends a command to the script state to export the
    aerodynamic results to a specified output file.

    Parameters
    ----------
    output_file : str
        The absolute path to the output file where the aerodynamic results
        will be stored.

    Raises
    ------
    ValueError
        If `output_file` is not a string representing a valid file path.

    Examples
    --------
    >>> # Export aerodynamic results to a text file
    >>> export_solver_analysis_spreadsheet(
    ...     output_file='C:/path/to/results.txt'
    ... )
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

def export_solver_analysis_tecplot(output_file: str) -> None:
    """
    Export Tecplot data based on solver results.

    This function appends a command to the script state to export Tecplot
    data for all initialized boundaries to a specified file.

    Parameters
    ----------
    output_file : str
        The absolute path to the output file where the Tecplot data will be
        stored.

    Raises
    ------
    ValueError
        If `output_file` is not a string representing a valid file path.

    Examples
    --------
    >>> # Export Tecplot data to a .dat file
    >>> export_solver_analysis_tecplot(
    ...     output_file='C:/path/to/tecplot_data.dat'
    ... )
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

def export_solver_analysis_vtk(
    output_filepath: str,
    surfaces: int,
    boundaries: Optional[List[int]] = None
) -> None:
    """
    Export a Visualization Toolkit (VTK) file based on solver results.

    This function appends a command to the script state to export a VTK file
    for specified boundaries based on the solver results.

    Parameters
    ----------
    output_filepath : str
        The absolute path to the output VTK file.
    surfaces : int
        The number of boundaries to export. Use -1 to export all boundaries.
    boundaries : Optional[List[int]], optional
        A list of boundary indices to be exported. Required if `surfaces`
        is not -1. Defaults to None.

    Raises
    ------
    ValueError
        If `surfaces` is not -1 and `boundaries` is not provided, or if the
        length of `boundaries` does not match `surfaces`.

    Examples
    --------
    >>> # Export the first two solver boundaries to a VTK file
    >>> export_solver_analysis_vtk(
    ...     output_filepath='C:/path/to/data.vtk',
    ...     surfaces=2,
    ...     boundaries=[1, 2]
    ... )

    >>> # Export all solver boundaries to a VTK file
    >>> export_solver_analysis_vtk(
    ...     output_filepath='C:/path/to/all_data.vtk',
    ...     surfaces=-1
    ... )
    """
    if surfaces != -1 and boundaries is None:
        raise ValueError("`boundaries` must be provided if `surfaces` is not -1.")
    
    if boundaries and len(boundaries) != surfaces:
        raise ValueError("Length of `boundaries` list must match `surfaces` value.")

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

def set_vtk_export_variables(
    num_variables: int,
    export_wake: RunOptions,
    variables: Optional[List[str]] = None
) -> None:
    """
    Set the variables to be exported in the VTK file.

    This function appends a command to the script state to configure the
    variables that will be included in the VTK export.

    Parameters
    ----------
    num_variables : int
        The number of variables to be exported. Use -1 to export all
        available variables.
    export_wake : RunOptions
        Option to export wake filaments to the VTK file ('ENABLE' or
        'DISABLE').
    variables : Optional[List[str]], optional
        A list of specific variable names to be exported. Required if
        `num_variables` is not -1. Defaults to None.

    Raises
    ------
    ValueError
        If `export_wake` is not a valid option, if `num_variables` is not
        an integer, or if `variables` is not provided when required.

    Examples
    --------
    >>> # Set a custom list of export variables for the VTK file
    >>> set_vtk_export_variables(
    ...     num_variables=5,
    ...     export_wake='DISABLE',
    ...     variables=['X', 'Y', 'Z', 'CP', 'PSTATIC']
    ... )

    >>> # Set all variables for export in the VTK file
    >>> set_vtk_export_variables(num_variables=-1, export_wake='ENABLE')
    """
    
    # Type and value checking
    if export_wake not in VALID_RUN_OPTIONS:
        raise ValueError(f"export_wake should be one of {VALID_RUN_OPTIONS}")
    
    if not isinstance(num_variables, int):
        raise ValueError("`num_variables` should be an integer value.")
        
    if num_variables != -1 and variables is None:
        raise ValueError("`variables` must be provided if `num_variables` is not -1.")
    
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
    format_value: ValidExportFormat = 'DIFFERENCE-PRESSURE',
    units: ValidPressureUnits = 'PASCALS',
    frame: int = 1,
    surfaces: int = -1,
    boundary_indices: Optional[List[int]] = None
) -> None:
    """
    Export FEM CSV (*.txt) file based on solver results.

    This function appends a command to the script state to export FEM CSV
    data based on solver results for all initialized boundaries with the
    specified format and unit specifications.

    Parameters
    ----------
    file_path : str
        The file name with path to file for output.
    format_value : ValidExportFormat, optional
        The format of the export data. Valid options are 'CP-FREESTREAM',
        'CP-REFERENCE', 'PRESSURE', 'DIFFERENCE-PRESSURE'. 
        Defaults to 'DIFFERENCE-PRESSURE'.
    units : ValidPressureUnits, optional
        The units for the exported pressure data. Valid options are 'PASCALS',
        'MEGAPASCALS', 'BAR', 'ATMOSPHERES', 'PSI'. Defaults to 'PASCALS'.
    frame : int, optional
        Index of coordinate system for output. Defaults to 1.
    surfaces : int, optional
        Number of boundaries that need to be exported, or -1 if all boundaries
        need to be exported. Defaults to -1.
    boundary_indices : Optional[List[int]], optional
        A list of boundary indices to export. Required if `surfaces` is not
        -1. Following text lines must include indices of all boundaries for
        which data must be exported. Defaults to None.

    Raises
    ------
    ValueError
        If `format_value` or `units` are invalid, or if `surfaces` is not
        -1 and `boundary_indices` is not provided or its length mismatches.
    TypeError
        If all elements in `boundary_indices` are not integers.

    Examples
    --------
    >>> # Export the FEM CSV file for the first three boundaries
    >>> export_solver_analysis_csv(
    ...     file_path='C:/Users/Desktop/Models/scripting_test_output_data.txt',
    ...     format_value='DIFFERENCE-PRESSURE',
    ...     units='PASCALS',
    ...     frame=1,
    ...     surfaces=3,
    ...     boundary_indices=[1, 2, 3]
    ... )
    
    >>> # Export the FEM CSV file for ALL boundaries
    >>> export_solver_analysis_csv(
    ...     file_path='C:/Users/Desktop/Models/scripting_test_output_data.txt',
    ...     format_value='DIFFERENCE-PRESSURE',
    ...     units='PASCALS',
    ...     frame=2,
    ...     surfaces=-1
    ... )
    """

    # Type and value checking
    if not isinstance(file_path, str):
        raise ValueError("`file_path` should be a string value.")
    
    if format_value not in VALID_EXPORT_FORMAT_LIST:
        raise ValueError(f"Invalid format value. Valid formats are: {VALID_EXPORT_FORMAT_LIST}")

    if units not in VALID_PRESSURE_UNITS_LIST:
        raise ValueError(f"Invalid unit type. Valid units are: {VALID_PRESSURE_UNITS_LIST}")
    
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if not isinstance(surfaces, int):
        raise ValueError("`surfaces` should be an integer value.")

    if surfaces != -1:
        if boundary_indices is None:
            raise ValueError("`boundary_indices` must be provided if `surfaces` is not -1.")
        if len(boundary_indices) != surfaces:
            raise ValueError("Length of `boundary_indices` must match `surfaces`.")
        if not all(isinstance(i, int) for i in boundary_indices):
            raise TypeError("All elements in `boundary_indices` must be integers.")

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

    if surfaces != -1 and boundary_indices:
        for boundary in boundary_indices:
            lines.append(str(boundary))

    script.append_lines(lines)
    return

def export_solver_analysis_pload_bdf(
    file_path: str,
    surfaces: int = -1,
    boundary_indices: Optional[List[int]] = None
) -> None:
    """
    Export NASTRAN PLOAD BDF data based on solver results.

    This function appends a command to the script state to export a NASTRAN
    PLOAD BDF file for specified boundaries.

    Parameters
    ----------
    file_path : str
        The absolute path to the output BDF file.
    surfaces : int, optional
        The number of boundaries to export. Use -1 for all boundaries.
        Defaults to -1.
    boundary_indices : Optional[List[int]], optional
        A list of boundary indices to export. Required if `surfaces` is not
        -1. Defaults to None.

    Raises
    ------
    ValueError
        If `surfaces` is not an integer, or if `surfaces` is not -1 and
        `boundary_indices` is not provided or its length mismatches.

    Examples
    --------
    >>> # Export the NASTRAN PLOAD BDF file for the first three boundaries
    >>> export_solver_analysis_pload_bdf(
    ...     file_path='C:/path/to/data.bdf',
    ...     surfaces=3,
    ...     boundary_indices=[1, 2, 3]
    ... )
    """
    
    if not isinstance(surfaces, int):
        raise ValueError("`surfaces` should be an integer.")
    
    if surfaces != -1:
        if boundary_indices is None:
            raise ValueError("`boundary_indices` must be provided if `surfaces` is not -1.")
        if len(boundary_indices) != surfaces:
            raise ValueError("Length of `boundary_indices` must match `surfaces`.")
    
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

def export_solver_analysis_force_distributions(
    output_filepath: str,
    surfaces: int = -1,
    boundary_indices: Optional[List[int]] = None
) -> None:
    """
    Export force distribution vectors based on solver results.

    This function appends a command to the script state to export the force
    distribution vectors for specified boundaries.

    Parameters
    ----------
    output_filepath : str
        The absolute path to the output data file.
    surfaces : int, optional
        The number of boundaries to export. Use -1 for all boundaries.
        Defaults to -1.
    boundary_indices : Optional[List[int]], optional
        A list of boundary indices to export. Required if `surfaces` is not
        -1. Defaults to None.

    Raises
    ------
    ValueError
        If `surfaces` is not an integer, or if `surfaces` is not -1 and
        `boundary_indices` is not provided or its length mismatches.

    Examples
    --------
    >>> # Export force distributions for three specified boundaries
    >>> export_solver_analysis_force_distributions(
    ...     output_filepath='C:/path/to/force_data.txt',
    ...     surfaces=3,
    ...     boundary_indices=[1, 2, 3]
    ... )
    """
    
    # Type and value checking
    if not isinstance(surfaces, int):
        raise ValueError("`surfaces` should be an integer value.")
    
    if surfaces != -1:
        if boundary_indices is None:
            raise ValueError("`boundary_indices` must be provided when `surfaces` is not -1.")
        if len(boundary_indices) != surfaces:
            raise ValueError("Length of `boundary_indices` must match `surfaces`.")
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


