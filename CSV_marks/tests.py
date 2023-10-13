import pytest
import pandas as pd

from results import get_all_tests_average_marks, get_all_failed_students

def test_get_all_tests_average_marks():
    assert get_all_tests_average_marks() == {'Test1': 43.143, 'Test2': 60.571, 'Test3': 65.714, 'Test4': 69.643}

def test_get_all_failed_students():
    assert get_all_failed_students() == ['David', 'Greta', 'Hannah', 'Madison', 'Nicholas']