__author__ = 'anderson'
import pytest

from santos.santos import Job
from santos.exceptions import TaskException

@pytest.fixture
def setup():
    d = {'hour': '1', 'kwargs': {"a": "A"}}
    return Job(lambda x: print(x), id="func3", **d)

@pytest.fixture
def setup_two():
    d = {'minutes': '1', 'kwargs': {"a": "B"}}
    return Job(lambda x: print(x), id="func2", **d)

@pytest.fixture
def setup_three():
    d = {'day_of_the_week': "Sa", 'kwargs': {"a": "B"}}
    return Job(lambda x: print(x), id="func3", **d)

@pytest.fixture
def setup_four():
    d = {'time_of_the_d': "02:16:50", 'kwargs': {"a": "D"}}
    return Job(lambda x: print(x), id="func4", **d)

def test_hour(setup):
    print("Teste hour")
    assert setup.calculateInterval() == 3600

def test_minute(setup_two):
    print("Teste minute")
    assert setup_two.calculateInterval() == 60

def test_day_of_week_raise(setup_three):
    print("Teste day_of_the_week")
    with pytest.raises(TaskException):
        setup_three.calculateInterval()

def test_params_not_combined(setup_four):
    with pytest.raises(TaskException):
        setup_four.calculateInterval()