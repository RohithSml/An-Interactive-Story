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
    
def engine():
    loaded_map,status = load_map(maps)

if __name__=='__main__':
    script, maps = argv
    engine()
