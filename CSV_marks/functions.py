import pandas as pd

path = "D:\Ivan\Programming\Software Engineering\CSV_marks\marks.csv"

# * Get Names
def get_all_test_names():
    df = pd.read_csv(path)

    return df.columns[1:].values

def get_all_student_names():
    df = pd.read_csv(path)

    return df["Name"].values

# * Calculate Average Mark

def calculate_average_mark_for_test(test_name):
    df = pd.read_csv(path)

    if test_name not in df.columns:
        return f"There is no test with name {test_name}"
    
    average_mark_for_test = df[test_name].mean()
    rounded_average_mark_for_test = round(average_mark_for_test, 3)

    return rounded_average_mark_for_test

def calculate_average_mark_for_student(student_name):
    df = pd.read_csv(path)
    df.set_index('Name', inplace=True)

    if student_name not in df.index:
        return f"Student '{student_name}' not found in the CSV."
    
    student_row = df.loc[student_name]
    average_mark_for_student = student_row.mean()
    rounded_average_mark_for_student = round(average_mark_for_student, 3)

    return rounded_average_mark_for_student

# * Get Results

def get_all_tests_average_marks():
    tests_average_marks = {}

    for test_name in get_all_test_names():
        tests_average_marks[test_name] = calculate_average_mark_for_test(test_name)

    return tests_average_marks

def get_all_failed_students():
    failed_students = []

    for student_name in get_all_student_names():
        average_mark = calculate_average_mark_for_student(student_name)
        assert isinstance(average_mark, float), f"Expected float but got {type(average_mark)} for student {student_name}"
        
        if average_mark < 50:
            failed_students.append(student_name)

    return failed_students