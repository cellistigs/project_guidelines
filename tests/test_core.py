from project_guidelines.core import core_functions 
import project_guidelines
from unittest.mock import patch

def test_increment():
    assert core_functions.increment(1) == 2

def test_increment_mock():
    """
    We can use patch as a context manager to go in and patch a specific module, object, or function (use patch.object for the latter two). This can be useful to run tests without hitting time consuming or extermal functions. Note that return_value can be anything- useful cases might include a specifically configured mock object. This particular case is something like a behavior test, asserting that the output of this function is arrived at via the add function. IMPORTANT: note that the object must be patched where it is imported: although "add" is defined in project_guidelines.utils.arithmetic, it is imported directly into project_guidelines.core.core_functions.  
    """
    with patch.object(project_guidelines.core.core_functions,"add", return_value = 3):
        assert core_functions.increment(1) == 3

def test_decrement():
    assert core_functions.decrement(1) == 0

def test_decrement_mock():
    """
    We can use patch as a context manager to go in and patch a specific module, object, or function (use patch.object for the latter two). This can be useful to run tests without hitting time consuming or extermal functions. Note that return_value can be anything- useful cases might include a specifically configured mock object. This particular case is something like a behavior test, asserting that the output of this function is arrived at via the add function. IMPORTANT: note that the object must be patched where it is imported: although "subtract" is defined in project_guidelines.utils.arithmetic, it is imported directly into project_guidelines.core.core_functions.  
    """
    with patch.object(project_guidelines.core.core_functions,"subtract", return_value = 3):
        assert core_functions.decrement(1) == 3
