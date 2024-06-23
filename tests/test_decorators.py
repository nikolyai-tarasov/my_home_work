import pytest

from src.decorators import dauble_2, log


def test_log_decor():
    result = dauble_2("")
    assert result is None
    assert dauble_2(2) == 1
