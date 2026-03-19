import os 


def normalize_option(value, parameter_name="value"):
    """Normalize enum-like string options for case-insensitive validation."""
    if not isinstance(value, str):
        raise ValueError(f"`{parameter_name}` should be a string value.")
    return value.strip().upper()

def check_valid_length_units(units):
    """
    Check if the provided input units are valid. 
    """
    valid_units = ["INCH", "MILLIMETER", "OTHER", "FEET", "MILE", "METER", "KILOMETER", 
                   "MILS", "MICRON", "CENTIMETER", "MICROINCH"]
    units = normalize_option(units, "units")
    if units not in valid_units:
        raise ValueError(f"Invalid units: {units}. Must be one of {', '.join(valid_units)}.")
    return units

def check_valid_force_units(units):
    """
    Check if the provided input units are valid. 
    """
    valid_units = ['COEFFICIENTS', 'NEWTONS', 'KILO-NEWTONS', 
                   'POUND-FORCE', 'KILOGRAM-FORCE']
    units = normalize_option(units, "units")
    if units not in valid_units:
        raise ValueError(f"Invalid units: {units}. Must be one of {', '.join(valid_units)}.")
    return units

def check_file_existence(file):
    # Validate file existence
    if not os.path.exists(file):
        raise FileNotFoundError(f"The specified file '{file}' does not exist on path.")
    return