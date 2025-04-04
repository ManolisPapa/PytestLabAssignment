import pytest
from bat_functions import calculate_bat_power, signal_strength

@pytest.mark.bat_power
def test_calculate_bat_power():
    # Atletico Madrid 0-1 Barcelona, Goal by Ferran Torres 27'
    assert calculate_bat_power(10) == 420
    assert calculate_bat_power(20) == 840
    assert calculate_bat_power(15) == 630

@pytest.mark.parametrize("distance, expected", [
    (10, 0),
    (5, 50),
    (12, 0),
    (3.2, 68)
])
@pytest.mark.signal_strength
def test_signal_strength(distance, expected):
    # Barcelona 4-1 Girona, Goals by Krejci 43', Lewandowski 61',77', and Ferran Torres 86'
    assert signal_strength(distance) == expected