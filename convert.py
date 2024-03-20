#functions for handling conversions between units
units = {
    "Length": {
        "Centimeter": 1.0,
        "Inch": 2.54,
        "Meter": 100,
        "Kilometer": 100000.0,
        "Feet": 30.48,
        "Mile": 160934.4,
    },
    "Mass": {
        "Gram": 1.0,
        "Kilogram": 1000.0,
        "Pound": 453.59237,
        "Ounce": 28.349523125, 
        "Ton": 1000000.0,
    }
} 


def convert_units(units, value, from_unit, to_unit):

    return float(value) * units[from_unit] / units[to_unit]
