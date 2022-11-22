# Test_unique_str_helper_functions.py
# Python File containing unit tests for making strings unique in a list
"""
Test_unique_str_helper_functions.py
"""
from unique_str_helper_functions import make_string_unique
from unittest.mock import Mock
from unittest.mock import patch
from pytest import MonkeyPatch

# Test 1: normal case
def test_make_string_unique_str_happy():
    # Assemble
    string = "Dave"
    list_of_strings = ["Dave", "Dave", "Dave", "Dave", "Tim", "John", "Dave", 3]
    # Act
    execute = make_string_unique(string, list_of_strings)
    expected = "Dave_001"
    # Assert
    print(f"{execute} vs. {expected}")
    assert execute == expected

def test_make_string_unique_str_non_string_input():
    # Assemble
    string = 3
    list_of_strings = ["Dave", "Dave", "Dave", "Dave", "Tim", "John", "Dave", 3]
    # Act
    execute = make_string_unique(string, list_of_strings)
    expected = "3_001"
    # Assert
    print(f"{execute} vs. {expected}")
    assert execute == expected

def test_make_string_unique_bool_input():
    # Assemble
    string = True
    list_of_strings = ["True", "True_001", True, "Dave", "Tim", "John", "Dave", 3]
    # Act
    execute = make_string_unique(string, list_of_strings)
    expected = "True_002"
    # Assert
    print(f"{execute} vs. {expected}")
    assert execute == expected

def test_make_string_unique_blank_input():
    # Assemble
    string = ""
    list_of_strings = [
        "",
        "_001", "_002", "_003", "_004", "_005", "_006", "_007", "_008", "_009", "_010",
        "_011", "_012", "_013", "_014", "_015", "_016", "_017", "_018", "_019", "_020",
        "_021", "_022", "_023", "_024", "_025", "_026", "_027", "_028", "_029", "_030",
        "_031", "_032", "_033", "_034", "_035", "_036", "_037", "_038", "_039", "_040",
        "_041", "_042", "_043", "_044", "_045", "_046", "_047", "_048", "_049", "_050",
        "_051", "_052", "_053", "_054", "_055", "_056", "_057", "_058", "_059", "_060",
        "_061", "_062", "_063", "_064", "_065", "_066", "_067", "_068", "_069", "_070",
        "_071", "_072", "_073", "_074", "_075", "_076", "_077", "_078", "_079", "_080",
        "_081", "_082", "_083", "_084", "_085", "_086", "_087", "_088", "_089", "_090",
        "_091", "_092", "_093", "_094", "_095", "_096", "_097", "_098", "_099", "_100",
        "_101", "_102", "_103", "_104", "_105", "_106", "_107", "_108", "_109", "_110",
    ]
    # Act
    execute = make_string_unique(string, list_of_strings)
    expected = "_111"
    # Assert
    print(f"{execute} vs. {expected}")
    assert execute == expected

def test_make_string_unique_not_in_list():
    # Assemble
    string = ""
    list_of_strings = [
        "_001", "_002", "_003", "_004", "_005", "_006", "_007", "_008", "_009", "_010",
        "_011", "_012", "_013", "_014", "_015", "_016", "_017", "_018", "_019", "_020",
        "_021", "_022", "_023", "_024", "_025", "_026", "_027", "_028", "_029", "_030",
        "_031", "_032", "_033", "_034", "_035", "_036", "_037", "_038", "_039", "_040",
        "_041", "_042", "_043", "_044", "_045", "_046", "_047", "_048", "_049", "_050",
        "_051", "_052", "_053", "_054", "_055", "_056", "_057", "_058", "_059", "_060",
        "_061", "_062", "_063", "_064", "_065", "_066", "_067", "_068", "_069", "_070",
        "_071", "_072", "_073", "_074", "_075", "_076", "_077", "_078", "_079", "_080",
        "_081", "_082", "_083", "_084", "_085", "_086", "_087", "_088", "_089", "_090",
        "_091", "_092", "_093", "_094", "_095", "_096", "_097", "_098", "_099", "_100",
        "_101", "_102", "_103", "_104", "_105", "_106", "_107", "_108", "_109", "_110",
    ]
    # Act
    execute = make_string_unique(string, list_of_strings)
    expected = ""
    # Assert
    print(f"{execute} vs. {expected}")
    assert execute == expected
# py -m pytest --cov
