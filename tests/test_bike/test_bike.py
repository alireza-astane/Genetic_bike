#import pytest
from src.bike.bike import Bike

def test_get_get_masses():
    test_bike = Bike(
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0)
    expectes_masses = [0,0,0,0]
    assert(test_bike.get_masses() == expectes_masses)
