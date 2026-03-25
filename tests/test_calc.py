# tests/test_calculator.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import evaluate_expression

import pytest
from calculator import evaluate_expression

def test_basic_arithmetic():
    assert evaluate_expression("2+3") == 5
    assert evaluate_expression("10-4") == 6
    assert evaluate_expression("3*5") == 15
    assert evaluate_expression("8/2") == 4

def test_math_functions():
    import math
    assert round(evaluate_expression("sin(90)"),5) == 1.0
    assert round(evaluate_expression("cos(0)"),5) == 1.0
    assert round(evaluate_expression("tan(45)"),5) == 1.0
    assert evaluate_expression("sqrt(25)") == 5
    assert round(evaluate_expression("log(e)"),5) == 1.0

def test_invalid_expression():
    result = evaluate_expression("1/0")
    assert "error" in result
    result = evaluate_expression("abc")
    assert "error" in result