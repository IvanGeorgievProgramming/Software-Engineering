import unittest
from unittest.mock import patch, Mock
import pandas as pd
import results as student_marks

class TestStudentMarks(unittest.TestCase):
    
    def setUp(self):
        self.mock_data = {
            'Name': ['Albert', 'Bob', 'Claire', 'David', 'Eva', 'Franklin', 'Greta', 'Hannah', 'Isabella', 'John', 'Kevin', 'Laura', 'Madison', 'Nicholas'],
            'Test1': [40, 41, 41, 42, 43, 44, 45, 46, 49, 48, 45, 50, 40, 30],
            'Test2': [90, 97, 80, 23, 78, 90, 11, 20, 90, 63, 10, 91, 50, 55],
            'Test3': [100, 96, 60, 36, 88, 80, 34, 30, 100, 97, 78, 90, 11, 20],
            'Test4': [83, 97, 40, 45, 77, 90, 67, 40, 83, 96, 88, 80, 59, 30]
        }
        self.mock_df = pd.DataFrame(self.mock_data)

    @patch('pandas.read_csv')
    def test_get_all_test_names(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_df

        result = student_marks.get_all_test_names()
        self.assertEqual(result, ['Test1', 'Test2', 'Test3', 'Test4'])

    @patch('pandas.read_csv')
    def test_get_all_student_names(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_df

        result = student_marks.get_all_student_names()
        expected_names = ['Albert', 'Bob', 'Claire', 'David', 'Eva', 'Franklin', 'Greta', 'Hannah', 'Isabella', 'John', 'Kevin', 'Laura', 'Madison', 'Nicholas']
        self.assertEqual(result, expected_names)

    @patch('pandas.read_csv')
    def test_calculate_average_mark_for_test(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_df

        result = student_marks.calculate_average_mark_for_test('Test1')
        self.assertEqual(result, 43.143)

        result = student_marks.calculate_average_mark_for_test('InvalidTest')
        self.assertEqual(result, "There is no test with name InvalidTest")

    @patch('pandas.read_csv')
    def test_calculate_average_mark_for_student(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_df

        result = student_marks.calculate_average_mark_for_student('Albert')
        self.assertEqual(result, 78.25)

        result = student_marks.calculate_average_mark_for_student('InvalidName')
        self.assertEqual(result, "Student 'InvalidName' not found in the CSV.")

    @patch('pandas.read_csv')
    def test_get_all_tests_average_marks(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_df

        result = student_marks.get_all_tests_average_marks()
        expected_result = {'Test1': 43.145, 'Test2': 60.571, 'Test3': 65.714, 'Test4': 69.643}
        self.assertEqual(result, expected_result)

    @patch('pandas.read_csv')
    def test_get_all_failed_students(self, mock_read_csv):
        mock_read_csv.return_value = self.mock_df

        result = student_marks.get_all_failed_students()
        # Manually determine students with an average below 50
        self.assertEqual(result, ['David', 'Greta', 'Hannah', 'Kevin', 'Madison', 'Nicholas'])

if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        print(f"An error occurred during the test run: {e}")
