import pytest
from processor.add_numbers import add_two_number


def test_add_two_number():
    """Check two numbers add"""

    assert add_two_number(5,5)==10
    assert add_two_number(6.1,7.1)==13.2

