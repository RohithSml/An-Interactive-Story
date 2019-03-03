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

def test_user_ip():
    def fake_input(_):
        return 'a'
    assert user_ip(fake_input)=='a'

def test_if_exit():
    map_data,status = load_map("./test_data/test_map.json")
    assert if_exit(map_data,'north') == True

def test_if_exit_false():
    map_data,status = load_map("./test_data/test_map.json")
    assert if_exit(map_data,'south') == False

def test_movement_true():
     map_data,status = load_map("./test_data/test_map.json")
     assert movement(map_data,['move','north']) == 'Creeky Hallway'

def test_movement_false():
     map_data,status = load_map("./test_data/test_map.json")
     assert movement(map_data,['move','south']) == 'Room 0'

def test_get_item():
    map_data,status = load_map("./test_data/test_map.json")
    get_item(map_data,['get','lantern'],'Chapel')
    assert state['inventory']== ['lantern']
    assert state['items'][0]['Chapel'] == ''

def test_get_item_false(capsys):
    map_data,status = load_map("./test_data/test_map.json")
    get_item(map_data,['get','lantern'],'Organ Room')
    out,err=capsys.readouterr()
    assert out == 'I wont let you get that lantern !\n'
