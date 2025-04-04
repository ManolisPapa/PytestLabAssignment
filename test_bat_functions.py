import pytest
from bat_functions import *
import bat_functions
from unittest.mock import patch

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

@pytest.fixture
def bat_vehicles_dict():
    return { 
        'Batmobile': {'speed': 200, 'armor': 80}, 
        'Batcycle': {'speed': 150, 'armor': 50},
        'Batplane': {'speed': 250, 'armor': 70}, 
        'Batboat': {'speed': 180, 'armor': 60},
        'Batwing': {'speed': 300, 'armor': 60} 
    }

@pytest.mark.vehicles
def test_known_or_unknown_vehicle(bat_vehicles_dict):
    keys = list(bat_vehicles_dict.keys())
    assert get_bat_vehicle(keys[0]) == bat_vehicles_dict['Batmobile']
    assert get_bat_vehicle(keys[1]) == bat_vehicles_dict['Batcycle']
    with pytest.raises(ValueError, match="Unknown vehicle: Batplane"):
        get_bat_vehicle(keys[2])
    with pytest.raises(ValueError, match="Unknown vehicle: Batboat"):  
        get_bat_vehicle(keys[3])
    assert get_bat_vehicle(keys[4]) == bat_vehicles_dict['Batwing']

@pytest.mark.joker_info
def test_fetch_joker_info():
    with patch("bat_functions.fetch_joker_info", return_value={'mischief_level': 50, 'location': 'Gotham City Hall'}):
        info = bat_functions.fetch_joker_info()
    assert info['mischief_level'] == 50
    assert info['location'] == 'Gotham City Hall'