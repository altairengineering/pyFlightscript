from typing import Literal

# Type Aliases for static type checking
RunOptions = Literal['ENABLE', 'DISABLE']
ValidUnits = Literal["INCH", "MILLIMETER", "OTHER", "FEET", "MILE", "METER", "KILOMETER", "MILS", "MICRON", "CENTIMETER", "MICROINCH"]
ValidForceUnits = Literal['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE']
ValidPlanes = Literal['XY', 'XZ', 'YZ', 'ZX']
BaseRegionType = Literal['EMPIRICAL', 'CONSTANT']
ValidDimensions = Literal['2D', '3D']
ValidAxis = Literal['X', 'Y', 'Z']
ValidGrowthScheme = Literal[1, 2, 3, 4]
ValidSymmetry = Literal['XY', 'XZ', 'YZ', 'NONE']
ValidCadMesh = Literal['CAD', 'MESH']
ValidQuadrant = Literal[1, 2, 3, 4]
ValidRotationAxis = Literal['X', 'Y', 'Z', '1', '2', '3']
ValidExportFormat = Literal['CP-FREESTREAM', 'CP-REFERENCE', 'PRESSURE']
ValidPressureUnits = Literal['PASCALS', 'MEGAPASCALS', 'BAR', 'ATMOSPHERES', 'PSI']
ValidFreestreamType = Literal['CONSTANT', 'CUSTOM', 'ROTATION']
ValidImportMeshFileTypes = Literal["STL", "TRI", "P3D", "CSV", "INP", "STRUCTURED_QUAD", "UNSTRUCTURED_QUAD", "LAWGS", "VTK", "AC", "FAC", "OBJ"]
ValidExportMeshFileTypes = Literal["STL", "TRI", "OBJ"]
ValidThresholds = Literal['AREA', 'QUALITY', 'X', 'Y', 'Z', 'VELOCITY', 'VX', 'VY', 'VZ', 'CP', 'MACH', 'SOLVER_QUALITY']
ValidRanges = Literal['ABOVE_MIN', 'BELOW_MAX', 'ABOVE_MIN_BELOW_MAX']
ValidSubsets = Literal['ALL_FACES', 'VISIBLE_FACES', 'SELECTED_FACES']
ValidTranslationTypes = Literal["ABSOLUTE", "TRANSLATION"]


# Lists for runtime validation
VALID_RUN_OPTIONS = ['ENABLE', 'DISABLE']
VALID_UNITS_LIST = ["INCH", "MILLIMETER", "OTHER", "FEET", "MILE", "METER", "KILOMETER", "MILS", "MICRON", "CENTIMETER", "MICROINCH"]
VALID_FORCE_UNITS_LIST = ['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE']
from typing import Literal

VALID_PLANE_LIST = ['XY', 'XZ', 'YZ']
VALID_AXIS_LIST = ['X', 'Y', 'Z']
VALID_BOOL_LIST = ['ON', 'OFF']
VALID_SIDE_LIST = ['L', 'R']
VALID_ROTATION_TYPE_LIST = ['EULER', 'QUATERNION']
VALID_CONTOUR_VARIABLE_LIST = [
    'Cp', 'Cp(Sonic)', 'Mach', 'Pressure', 'Temperature', 'Density',
    'Velocity Magnitude', 'Velocity X', 'Velocity Y', 'Velocity Z',
    'Vorticity Magnitude', 'Vorticity X', 'Vorticity Y', 'Vorticity Z',
    'Q-Criterion', 'Lambda2', 'Wall Shear X', 'Wall Shear Y', 'Wall Shear Z',
    'Wall Shear Mag', 'Y+'
]
VALID_VECTOR_VARIABLE_LIST = [
    'Velocity', 'Vorticity', 'Wall Shear Stress'
]
VALID_LINE_TYPE_LIST = ['SOLID', 'DASHED', 'DOTTED', 'DASHDOT']
VALID_COLOR_LIST = [
    'BLACK', 'WHITE', 'RED', 'GREEN', 'BLUE', 'YELLOW', 'MAGENTA', 'CYAN',
    'GRAY', 'ORANGE', 'PURPLE', 'BROWN', 'PINK'
]
VALID_CAMERA_TYPE_LIST = ['PERSPECTIVE', 'ORTHOGRAPHIC']
VALID_PROBE_TYPE_LIST = ['POINT', 'LINE', 'RECTANGLE', 'CIRCLE', 'SPHERE', 'BOX']
VALID_STREAMLINE_SEED_TYPE_LIST = [
    'LINE', 'RECTANGLE', 'CIRCLE', 'CONE', 'CYLINDER', 'SPHERE', 'BOX'
]
VALID_STREAMLINE_INTEGRATION_DIRECTION_LIST = ['FORWARD', 'BACKWARD', 'BOTH']
VALID_STREAMLINE_INTEGRATION_TYPE_LIST = ['RUNGE-KUTTA 2', 'RUNGE-KUTTA 4']
VALID_STREAMLINE_COLOR_VARIABLE_LIST = [
    'Cp', 'Mach', 'Pressure', 'Temperature', 'Density', 'Velocity Magnitude',
    'Velocity X', 'Velocity Y', 'Velocity Z', 'Vorticity Magnitude',
    'Vorticity X', 'Vorticity Y', 'Vorticity Z', 'Q-Criterion', 'Lambda2'
]
VALID_SURFACE_TYPE_LIST = ['ISOSURFACE', 'CUTTINGPLANE']
VALID_ISOSURFACE_VARIABLE_LIST = [
    'Cp', 'Mach', 'Pressure', 'Temperature', 'Density', 'Velocity Magnitude',
    'Velocity X', 'Velocity Y', 'Velocity Z', 'Vorticity Magnitude',
    'Vorticity X', 'Vorticity Y', 'Vorticity Z', 'Q-Criterion', 'Lambda2'
]
VALID_CUTTING_PLANE_VARIABLE_LIST = [
    'Cp', 'Mach', 'Pressure', 'Temperature', 'Density', 'Velocity Magnitude',
    'Velocity X', 'Velocity Y', 'Velocity Z', 'Vorticity Magnitude',
    'Vorticity X', 'Vorticity Y', 'Vorticity Z', 'Q-Criterion', 'Lambda2'
]
VALID_VOLUME_TYPE_LIST = ['BOX', 'SPHERE', 'CYLINDER', 'CONE']
VALID_WAKE_CUT_TYPE_LIST = ['CONSTANT Z', 'CONSTANT Y', 'CONSTANT X']


VALID_MOTION_SOLVER_TYPE_LIST = ['STEADY', 'UNSTEADY']
VALID_MOTION_TYPE_LIST = ['ACCELERATION', 'VELOCITY', 'DISPLACEMENT']

VALID_BASE_REGION_TYPE_LIST = ['EMPIRICAL', 'CONSTANT']
VALID_DIMENSIONS_LIST = ['2D', '3D']
VALID_AXIS_LIST = ['X', 'Y', 'Z']
VALID_GROWTH_SCHEME_LIST = [1, 2, 3, 4]
VALID_SYMMETRY_LIST = ['XY', 'XZ', 'YZ', 'NONE']
VALID_CAD_MESH_LIST = ['CAD', 'MESH']
VALID_QUADRANT_LIST = [1, 2, 3, 4]
VALID_ROTATION_AXIS_LIST = ['X', 'Y', 'Z', '1', '2', '3']
VALID_EXPORT_FORMAT_LIST = ['CP-FREESTREAM', 'CP-REFERENCE', 'PRESSURE']
VALID_PRESSURE_UNITS_LIST = ['PASCALS', 'MEGAPASCALS', 'BAR', 'ATMOSPHERES', 'PSI']
VALID_FREESTREAM_TYPE_LIST = ['CONSTANT', 'CUSTOM', 'ROTATION']
VALID_IMPORT_MESH_FILE_TYPES = ["STL", "TRI", "P3D", "CSV", "INP", "STRUCTURED_QUAD", "UNSTRUCTURED_QUAD", "LAWGS", "VTK", "AC", "FAC", "OBJ"]
VALID_EXPORT_MESH_FILE_TYPES = ["STL", "TRI", "OBJ"]
VALID_THRESHOLD_LIST = ['AREA', 'QUALITY', 'X', 'Y', 'Z', 'VELOCITY', 'VX', 'VY', 'VZ', 'CP', 'MACH', 'SOLVER_QUALITY']
VALID_RANGE_LIST = ['ABOVE_MIN', 'BELOW_MAX', 'ABOVE_MIN_BELOW_MAX']
VALID_SUBSET_LIST = ['ALL_FACES', 'VISIBLE_FACES', 'SELECTED_FACES']
VALID_TRANSLATION_TYPES = ["ABSOLUTE", "TRANSLATION"]
