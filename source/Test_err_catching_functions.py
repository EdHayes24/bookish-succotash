# Test_err_catching_helper_functions.py
# Python File containing unit tests for Err_catching user input functions
"""
Test_err_catching_functions.py
"""
from err_catching_helper_functions import (
    get_min_length_string,
    get_non_negative_int,
    get_non_neg_float,
    options_selector
)
from pytest import MonkeyPatch
import pytest


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
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    prompt = "Enter an integer"
    # Act
    execute = get_non_negative_int(prompt)
    # Assert
    assert execute == 42


def test_get_non_neg_float(monkeypatch: MonkeyPatch):
    # Assemble
    inputs = ["-2.23", "-1", "Hello World", "42.36"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    prompt = "Enter an float"
    # Act
    execute = get_non_neg_float(prompt)
    # Assert
    assert execute == 42.36

def test_options_selector(monkeypatch: MonkeyPatch):
    # Assemble
    options = ["a", "b", "c", "d", "e", "f", "g"]
    inputs = ["-2.23", "-1", "Hello World", "42.36", "42", "3", "7"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    # Act
    execute = options_selector(options, "Input Selection Here: ")
    expected = 3
    # Assert
    assert execute == expected

def test_options_selector_emptylist(monkeypatch: MonkeyPatch):
    # Assemble
    options = []
    inputs = ["3"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    # Act
    execute = options_selector(options, "Input Selection Here: ")
    assert execute == None
    # with pytest.raises(IndexError):
    #     options_selector(options, "Input Selection Here: ")
# py -m pytest --cov
