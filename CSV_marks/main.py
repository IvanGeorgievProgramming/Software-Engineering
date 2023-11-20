import cProfile
from functions import get_all_tests_average_marks, get_all_failed_students, get_all_student_names, get_all_test_names, calculate_average_mark_for_student, calculate_average_mark_for_test

def main():
    print("Test average marks:")
    print(get_all_tests_average_marks())

    print("\nFailed students:")
    print(get_all_failed_students())

    print("\nAll student names:")
    print(get_all_student_names())

    print("\nAll test names:")
    print(get_all_test_names())

    print("\nAverage mark for student 'Albert':")
    print(calculate_average_mark_for_student("Albert"))

    print("\nAverage mark for test 'Test1':")
    print(calculate_average_mark_for_test("Test1"))

if __name__ == "__main__":
    cProfile.run('main()')