import pytest
from simulator.simulator import Simulator

def test_simulator_initialized_correct_state():
    simulator = Simulator(5,5)
    assert simulator.get_board_size() == [5,5]

def test_simulator_initialized_correct_size():
    simulator = Simulator(31,57)
    assert simulator.get_board_size() == [31,57]

