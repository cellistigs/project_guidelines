from project_guidelines.utils import arithmetic
from unittest.mock import MagicMock,call

def test_add():
    assert arithmetic.add(1,1) == 2

def test_add_mock():
    """
    We can use mocks to assert certain behavior of the function we are testing: we can reach into the functions, and then record the particular set of events that happened to them. IMPORTANT Note that mock_calls is fairly general, but will not provide calls to the return value of a mock object. 

    """
    mock_int = MagicMock()
    b = arithmetic.add(mock_int,1)
    assert mock_int.mock_calls == [call.__add__(1)]

def test_subtract():
    assert arithmetic.subtract(1,1) == 0

def test_subtract_mock():
    """
    We can use mocks to assert certain behavior of the function we are testing: we can reach into the functions, and then record the particular set of events that happened to them. IMPORTANT Note that mock_calls is fairly general, but will not provide calls to the return value of a mock object. 

    """
    mock_int = MagicMock()
    b = arithmetic.add(mock_int,1)
    assert mock_int.mock_calls == [call.__add__(1)]
