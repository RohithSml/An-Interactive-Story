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

        'passive_item' :  ['lantern', 'Dusty Hallway','As you walked over to through next room, you loose your footing and fall down into a dark abyss'],
        
        'secret_room_status' : {'Laboratory':False, 'Library':False,'access':False},

        'secret_room_avl' :['Organ Room',{'north' : 'Secret Room','east':'Creeky Hallway'}],
               
        'count': 0 ,

        'End status':['Secret Room',False],

        'End direction':['Secret Room',{'north':'Room Zen', 'south':'Organ Room'}],
               
        'End' :'Room Zen'

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

def test_use_item(capsys):
    map_data,status = load_map("./test_data/test_map.json")
    state['inventory']=['battered_ring']
    use_item(map_data,['use', 'battered_ring'],'Laboratory')
    out,err= capsys.readouterr()
    assert out== '\n\nYou take out the Battered Ring etched with strange symbols, as you slowly try to place the ring in the index finger of the stone hand *thud* the ring gets fixed in the stone and you see a faint glow on the engravings of the ring, Suddenly you hear a *THUD* comming from downstaris near the Organ room.\n\n'

def test_use_item_false(capsys):
    map_data,status = load_map("./test_data/test_map.json")
    state['inventory']=['battered_ring']
    use_item(map_data,['use', 'battered_ring'],'Library')
    out,err= capsys.readouterr()
    assert out =='I wont let you use it\n'

def test_for_secret_room_access():
     map_data,status = load_map("./test_data/test_map.json")
     state['inventory']=['skull','battered_ring']
     state['secret_room_status']={'Laboratory':False, 'Library':False,'access':False}
     state['count']=0
     use_item(map_data,['use','skull'], 'Library')
     assert state['secret_room_status']=={'Laboratory':False, 'Library':True,'access':False}
     use_item(map_data,['use','battered_ring'], 'Laboratory')
     assert state['secret_room_status']=={'Laboratory':True, 'Library':True,'access':True}

     state['Current_Room']='Organ Room'
     assert movement(map_data,['move','north']) == 'Secret Room'


def test_for_EndRoom_acess():
    map_data,status = load_map("./test_data/test_map.json")
    state['inventory']=['sacrificial_dagger']
    use_item(map_data,['use','sacrificial_dagger'],'Secret Room')
    assert state['End status'][1]==True
    
    state['Current_Room']='Secret Room'
    assert movement(map_data,['move','north']) == 'Room Zen'

def test_for_not_having_passive_item():
     map_data,status = load_map("./test_data/test_map.json")
     state['Current_Room']= 'Dusty Hallway'
     assert not_have_passive_item(map_data)== True

def test_for_having_passive_item():
    map_data,status = load_map("./test_data/test_map.json")
    state['Current_Room']= 'Dusty Hallway'
    state['inventory']=['lantern']
    assert not_have_passive_item(map_data)== False

def test_for_instruction(capsys):
    map_data,status = load_map("./test_data/test_map.json")
    instruction(map_data)
    out,err= capsys.readouterr()
    assert out =='\n\n For movement use : move \n For picking up items to inventory use : get \n For using item use keyword : use \n\n'
    
     
     
    
    
    
    
