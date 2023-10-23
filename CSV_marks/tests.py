import unittest
from results import *

class TestResultsMethods(unittest.TestCase):

    def test_get_all_test_names(self):
        expected = ['Test1', 'Test2', 'Test3', 'Test4']
        self.assertEqual(get_all_test_names().tolist(), expected)

    def test_get_all_student_names(self):
        expected_names = ['Albert', 'Bob', 'Claire', 'David', 'Eva', 'Franklin', 'Greta', 'Hannah', 'Isabella', 'John', 'Kevin', 'Laura', 'Madison', 'Nicholas']
        self.assertEqual(get_all_student_names().tolist(), expected_names)

    def test_calculate_average_mark_for_test(self):
        self.assertAlmostEqual(calculate_average_mark_for_test("Test1"), 43.143, places=3)
        self.assertEqual(calculate_average_mark_for_test("TestNonexistent"), "There is no test with name TestNonexistent")

    def test_calculate_average_mark_for_student(self):
        self.assertAlmostEqual(calculate_average_mark_for_student("Albert"), 78.25, places=3)
        self.assertEqual(calculate_average_mark_for_student("NonExistentStudent"), "Student 'NonExistentStudent' not found in the CSV.")

    def test_get_all_tests_average_marks(self):
        averages = get_all_tests_average_marks()
        self.assertEqual(averages, {'Test1': 43.143, 'Test2': 60.571, 'Test3': 65.714, 'Test4': 69.643})

    def test_get_all_failed_students(self):
        failed = get_all_failed_students()
        expected_failed = ['David', 'Greta', 'Hannah', 'Madison', 'Nicholas']
        self.assertEqual(failed, expected_failed)

if __name__ == "__main__":
    unittest.main()