import unittest
import pandas as pd
from results import *

TEST_CSV = """Name,Test1,Test2,Test3,Test4
Albert,40,90,100,83
Bob,41,97,96,97
Claire,41,80,60,40
"""

with open("marks_test.csv", "w") as f:
    f.write(TEST_CSV)

def mocked_read_csv(filename):
    return pd.read_csv("marks_test.csv")

pd.read_csv = mocked_read_csv

class TestResultsMethods(unittest.TestCase):

    def test_get_all_test_names(self):
        expected = ['Test1', 'Test2', 'Test3', 'Test4']
        self.assertEqual(get_all_test_names().tolist(), expected)

    def test_get_all_student_names(self):
        expected = ['Albert', 'Bob', 'Claire']
        self.assertEqual(get_all_student_names().tolist(), expected)

    def test_calculate_average_mark_for_test(self):
        self.assertEqual(calculate_average_mark_for_test("Test1"), 40.667)
        self.assertEqual(calculate_average_mark_for_test("TestNonexistent"), "There is no test with name TestNonexistent")

    def test_calculate_average_mark_for_student(self):
        self.assertEqual(calculate_average_mark_for_student("Albert"), 78.25)
        self.assertEqual(calculate_average_mark_for_student("NonExistentStudent"), "Student 'NonExistentStudent' not found in the CSV.")

    def test_get_all_tests_average_marks(self):
        expected = {'Test1': 40.667, 'Test2': 89.0, 'Test3': 85.333, 'Test4': 73.333}
        self.assertEqual(get_all_tests_average_marks(), expected)

    def test_get_all_failed_students(self):
        self.assertEqual(get_all_failed_students(), ['Claire'])

if __name__ == "__main__":
    unittest.main()