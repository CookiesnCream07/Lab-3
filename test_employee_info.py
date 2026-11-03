import employee_info


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert result == 60166.67


def test_get_employees_by_dept():
    # Searching for "Sales" returns John and Peter (2 records)
    result = employee_info.get_employees_by_dept("Sales")
    assert len(result) == 2


def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(22, 31)
    assert len(result) == 3