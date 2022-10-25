import pytest
from src.unittests.employee import Employee


def test_defaults():
    c = Employee()
    assert c.name is None
    assert c.id is None
    assert c.dept is None
    assert c.status == "Active"


def test_equality():
    e1 = Employee("Karthick", 1, "IT")
    e2 = Employee("Karthick", 1, "IT")
    assert e1 == e2


def test_inequality():
    e1 = Employee("Karthick", 1, "IT")
    e2 = Employee("Karthick", 1, "IT", "InActive")
    assert e1 != e2


def test_from_dict():
    # GIVEN
    employee_dict = {
        "name": "Karthick",
        "id": 1,
        "dept": "IT",
        "status": "Active"
    }

    # WHEN
    actual_employee = Employee.from_dict(employee_dict)

    # THEN
    expected_employee = Employee("Karthick", 1, "IT")
    assert expected_employee == actual_employee
