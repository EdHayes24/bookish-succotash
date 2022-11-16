# Test_err_catching_helper_functions.py
# Python File containing unit tests for Err_catching user input functions
"""
Test_err_catching_functions.py
"""
from err_catching_helper_functions import get_min_length_string, get_non_negative_int, get_non_neg_float
from pytest import MonkeyPatch


def test_get_min_length_string_zero_len_strings(monkeypatch: MonkeyPatch):
    # Assemble
    inputs = ["", "", "Hello World"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    prompt = "Some String"
    # Act
    execute = get_min_length_string(prompt)
    # Assert
    assert execute == "Hello World"

def test_get_non_neg_int(monkeypatch: MonkeyPatch):
    # Assemble
    inputs = ["-2.23", "-1", "Hello World", "42.36", "42"]
    #inputs = [42]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    prompt = "Enter an integer"
    # Act
    execute = get_non_negative_int(prompt)
    # Assert
    assert execute == 42

def test_get_non_neg_float(monkeypatch: MonkeyPatch):
    # Assemble
    inputs = ["-2.23", "-1", "Hello World", "42.36"]
    #inputs = [42]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    prompt = "Enter an float"
    # Act
    execute = get_non_neg_float(prompt)
    # Assert
    assert execute == 42.36

# py -m pytest --cov