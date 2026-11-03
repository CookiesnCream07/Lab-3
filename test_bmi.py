import importlib

# Use importlib to dynamically load the module with a hyphen in the folder name
bmi = importlib.import_module("Lab-2.bmi")

def test_bmi_normal_weight():
    # Height = 1.73m, Weight = 60kg (BMI ~20.05 -> Normal Weight)
    result = bmi.calculate_bmi(height=1.73, weight=60)
    assert (result == 0)

def test_bmi_over_weight():
    # Height = 1.73m, Weight = 85kg (BMI ~28.40 -> Over Weight)
    result = bmi.calculate_bmi(height=1.73, weight=85)
    assert (result == 1)

def test_bmi_under_weight():
    # Height = 1.73m, Weight = 45kg (BMI ~15.04 -> Under Weight)
    result = bmi.calculate_bmi(height=1.73, weight=45)
    assert (result == -1)