from parser import *
from sys import argv

def test_loading_map():
    
    map_data,status = load_map("./test_data/test_map.json")
    assert status == True

    
