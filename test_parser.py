from parser import *
from sys import argv

def test_loading_map():
    
    map_data,status = load_map("./test_data/test_map.json")
    assert status == True

    
def test_initial_state():
    map_data,status = load_map("./test_data/test_map.json")
    Init_state(map_data)
    estimate={ 'items': [{'Room 0':'', 'Creeky Hallway':'','Dusty Hallway':'','Laboratory':'','Library':'','Secret Room':'','End':'','Coal Chute':'', 'Organ Room':'battered_ring', 'Chapel':'lantern', 'Conservatory':'skull', 'Bloody Room':'sacrificial_dagger'}],

        'Starting_Room': 'Room 0',

        'Current_Room' : 'Room 0',
                
        'inventory' : [],

        'passive_item' : ['lantern', 'Dusty Hallway'],
        
        'secret_room_status' : [False, False],

        'secret_room_avl' :{'Organ Room':{'north' : 'Sceret Room','east':'Creeky Hallway'}},

        'End' :'To be continued'

        }

    assert state==estimate
