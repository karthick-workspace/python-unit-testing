from src.unittests import employee_repository


def calculate_employee_grade(id):
    # Assume this is database call
    employee = employee_repository.get_employee_details(id)

    if employee is None:
        raise ValueError(f"{id} is not available in database")

    if employee.get('years_of_experience') >= 20:
        return 'Level A'
    elif 15 <= employee.get('years_of_experience') < 20:
        return 'Level B'
    elif 10 <= employee.get('years_of_experience') < 15:
        return 'Level C'
    else:
        return 'Level D'
