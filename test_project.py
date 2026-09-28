from project import (
    calculate_average,
    is_duplicate_subject,
    get_school_type_name,
    parse_number,
)


def test_calculate_average():
    assert calculate_average([]) == 0
    assert calculate_average([{"Name": "Math", "Grade": 78}]) == 78
    assert calculate_average(
        [{"Name": "Math", "Grade": 78}, {"Name": "English", "Grade": 91}]
    ) == 84.5


def test_is_duplicate_subject():
    grades = [{"Name": "Math", "Grade": 78}]
    assert is_duplicate_subject(grades, "Math") is True
    assert is_duplicate_subject(grades, "English") is False
    assert is_duplicate_subject([], "Math") is False


def test_get_school_type_name():
    assert get_school_type_name(1) == "Primary"
    assert get_school_type_name(2) == "Secondary"
    assert get_school_type_name(3) == "Both"
    assert get_school_type_name(9) == "Unknown"


def test_parse_number():
    assert parse_number("78") == 78
    assert parse_number("0") == 0
    assert parse_number("abc") is None
    assert parse_number("") is None
