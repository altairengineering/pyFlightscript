from typing import Literal

# Type Aliases for static type checking
RunOptions = Literal['ENABLE', 'DISABLE']
ValidUnits = Literal["INCH", "MILLIMETER", "OTHER", "FEET", "MILE", "METER", "KILOMETER", "MILS", "MICRON", "CENTIMETER", "MICROINCH"]
ValidForceUnits = Literal['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE']
ValidPlanes = Literal['XY', 'XZ', 'YZ']

# Lists for runtime validation
VALID_RUN_OPTIONS = ['ENABLE', 'DISABLE']
VALID_UNITS_LIST = ["INCH", "MILLIMETER", "OTHER", "FEET", "MILE", "METER", "KILOMETER", "MILS", "MICRON", "CENTIMETER", "MICROINCH"]
VALID_FORCE_UNITS_LIST = ['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 'POUND-FORCE', 'KILOGRAM-FORCE']
VALID_PLANE_LIST = ['XY', 'XZ', 'YZ']