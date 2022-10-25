employees = {
    "E1": {
        "name": "Emp1",
        "id": "E1",
        "dept": "Finance",
        "years_of_experience": 20

    },
    "E2": {
        "name": "Emp2",
        "id": "E2",
        "dept": "IT",
        "years_of_experience": 2

    },
    "E3": {
        "name": "Emp3",
        "id": "E3",
        "dept": "HR",
        "years_of_experience": 5

    }
}


def get_employee_details(id):
    employees.get(id, None)
