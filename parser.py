import sys
from sys import argv
import json
import pprint



state={ 'items': [],

        'Starting_Room': '',

        'Current_Room' : '',
                
        'inventory' : [],

        'passive_item' : [],
        
        'secret_room_status' : [],

        'secret_room_avl' :{'Organ Room':{'north' : 'Sceret Room','east':'Creeky Hallway'}},

        'End' :'To be continued'

        }

def load_map(maps):
    with  open(maps,"r") as read_file:
        map_data = json.load(read_file)
        if map_data != '':
            return map_data, True
        else:
            return '', False

def Init_state(loaded_map):
    
    state['Current_Room'] = loaded_map[2]['Initial_Room']
    state['Starting_Room'] = loaded_map[2]['Initial_Room']
    state['items']=loaded_map[3]['items']
    state['passive_item']=loaded_map[4]['passive item']
    state['secret_room_status']=loaded_map[5]['secret_room_status']

def user_ip(input=input):
    ret = input('>>')
    return ret

def if_exit(loaded_map,exits):
    if exits in loaded_map[0]['rooms'][state['Current_Room']][1] :
        return True
    else:
        return False
def movement(loaded_map,action):
    ret=''
    if if_exit(loaded_map,action[1]):
        ret = loaded_map[0]['rooms'][state['Current_Room']][1][action[1]]
        return  ret
    else:
        print('I dont see any exits that way.')
        ret = state['Current_Room']
        return ret

def engine():
    loaded_map,status = load_map(maps)
    Init_state(loaded_map)

if __name__=='__main__':
    script, maps = argv
    engine()
