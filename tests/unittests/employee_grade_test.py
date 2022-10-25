from unittest.mock import patch
from src.unittests.employee_grade import calculate_employee_grade
import unittest


class TestEmployeeGrade(unittest.TestCase):

    @patch('src.unittests.employee_grade.employee_repository')
    def test_employee_grade_for_db_connection_issue(self, mocked_employee_repository):
        mocked_employee_repository.get_employee_details.side_effect = TimeoutError
        with self.assertRaises(TimeoutError):
            calculate_employee_grade("E23")

    @patch('src.unittests.employee_grade.employee_repository')
    def test_employee_grade_for_non_existing_employees(self, mocked_employee_repository):
        mocked_employee_repository.get_employee_details.return_value = None
        with self.assertRaises(ValueError) as cm:
            calculate_employee_grade("E23")

        self.assertEqual(str(cm.exception), "E23 is not available in database")

    @patch('src.unittests.employee_grade.employee_repository')
    def test_employee_grade_for_level_A(self, mocked_employee_repository):
        mocked_employee_repository.get_employee_details.return_value = {
            "name": "Temp1",
            "id": "T1",
            "dept": "Finance",
            "years_of_experience": 20

        }
        level = calculate_employee_grade("T1")

        self.assertEqual(level, "Level A")
