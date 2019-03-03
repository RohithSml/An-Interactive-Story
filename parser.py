import sys
from sys import argv
import json
import pprint



state={ 'items': [],

        'Starting_Room': '',

        'Current_Room' : '',
                
        'inventory' : [],

        'passive_item' : [],
        
        'secret_room_status' : {},

        'secret_room_avl' :[],

        'count':0,

        'End status': [],

        'End direction':[],

        'End' :''

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
    state['secret_room_avl'] = loaded_map[5]['secret_room_avl']
    state['count'] = loaded_map[6]['count']
    state['End status'] = loaded_map[7]['End status']
    state['End direction'] = loaded_map[8]['End direction']
    state['End'] = loaded_map[9]['End']
    state['secret_room_status']=loaded_map[10]['secret_room_status']

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
    elif state['secret_room_status']['access'] == True and state['Current_Room'] == state['secret_room_avl'][0]:
        ret=state['secret_room_avl'][1][action[1]]
        return ret
    elif state['End status'][1] == True and state['Current_Room'] == state['End direction'][0]:
        ret=state['End direction'][1][action[1]]
        return ret
    else:
        print('I dont see any exits that way.')
        ret = state['Current_Room']
        return ret

def get_item(loaded_map,action,CurrentRoom):
    
    if action[1] == state['items'][0][CurrentRoom]:
        state['inventory'].append(action[1])
        state['items'][0][CurrentRoom]=''
    else:
        print('I wont let you get that {} !'.format(action[1]))

def use_item(loaded_map,action,CurrentRoom):
    ret=''
    if action[1] in state['inventory'] and action[1] in loaded_map[1]['action'] and CurrentRoom in loaded_map[1]['action'][action[1]][0] :
        ret=loaded_map[1]['action'][action[1]][1]
        state['inventory'].remove(action[1])
        print(ret)
        if CurrentRoom in state['secret_room_status']:
            state['secret_room_status'][CurrentRoom] = True
            state['count']=state['count']+1
        if state['count'] ==2:
            state['secret_room_status']['access'] = True
        if CurrentRoom == state['End status'][0]:
            state['End status'][1] = True
    else:
        print('I wont let you use it')

def showStatus(loaded_map):
    print("You are in {}".format(state['Current_Room']))
    print(loaded_map[0]['rooms'][state['Current_Room']][0])
    print('Obtainables:  ', state['items'][0][state['Current_Room']])
    print('Your Inventory:  ', state['inventory'])

def engine(maps):
    loaded_map,status = load_map(maps)
    Init_state(loaded_map)
    while True:
        showStatus(loaded_map)
        user= user_ip()  
        action=''
        action=user.lower().split()
        if action[0] == 'move':
           state['Current_Room'] = movement(loaded_map,action)
           
        if action[0] == 'get':
           get_item(loaded_map,action,state['Current_Room'])
           
        if action[0]== 'use':
            use_item(loaded_map,action,state['Current_Room'])
            

        if state['Current_Room']==state['End']:
            print(loaded_map[0]['rooms'][state['Current_Room']])
            print('YOU WON')
            break

if __name__=='__main__':
    script, maps = argv
    engine(maps)
    
