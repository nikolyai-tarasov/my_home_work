import pytest
from src.decorators import dauble_2
from src.decorators import log


def test_log_decor():
    @log("mylog.txt")
    def dauble_2(x):
        return x / x

    result = dauble_2("")
    assert result == None
