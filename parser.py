import sys
from sys import argv
import json
import pprint
import textwrap



# Use lower case keys for everything. Some are underscore separated. Some have spaces. etc.
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
    """Loads the .json file and returns the map_data and a status"""
    with  open(maps,"r") as read_file:
        map_data = json.load(read_file)
        if map_data != '': # You should probably raise an exception here. Not return ''
            return map_data, True
        else:
            return '', False

def init_state(loaded_map):
    """It initializes the state from the loaded map"""
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
    """Returns User Input"""
    ret = input('>>')
    return ret

def if_exit(loaded_map,exits):
    """Checks if there is an exit in the appropriate direction and Return a boolean value""" 
    if exits in loaded_map[0]['rooms'][state['Current_Room']][1] :
        return True
    else:
        return False

def movement(loaded_map,action):
    """Move the player to its apropriate room, also give access to secret room and ending room"""
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
    """Gets the item from the state to its inventory"""    
    if action[1] == state['items'][0][CurrentRoom]:
        state['inventory'].append(action[1])
        state['items'][0][CurrentRoom]=''
    else:
        print('I wont let you get that {} !'.format(action[1]))

def use_item(loaded_map,action,CurrentRoom):
    """Uses the appropriate item in the designated room, checks secret room status, and controls its access token for the secret room and also give its Post Action Description"""
    ret=''
    if action[1] in state['inventory'] and action[1] in loaded_map[1]['action'] and CurrentRoom in loaded_map[1]['action'][action[1]][0] :
        ret=loaded_map[1]['action'][action[1]][1]
        state['inventory'].remove(action[1])
        loaded_map[0]['rooms'][CurrentRoom][0]=loaded_map[11]['Post Action Description'][CurrentRoom]
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
    """Shows the Status of the player, including current position,inventory, obtainables etc"""
    print("\nYou are in {}\n".format(state['Current_Room']))
    print(textwrap.fill(loaded_map[0]['rooms'][state['Current_Room']][0]))
    print('Obtainables:  ', state['items'][0][state['Current_Room']])
    print('Your Inventory:  ', state['inventory'])

def not_have_passive_item(loaded_map):
    """Checks if player does not have the passive item in inventory and return appropriate boolean value"""
    if state['passive_item'][1]==state['Current_Room'] and state['passive_item'][0] not in state['inventory']:
        state['Current_Room']= state['Starting_Room']
        print(state['passive_item'][2])
        return True
    else:
        return False

def instruction(loaded_map):
    """Prints the Instructions"""
    ret=loaded_map[12]['help']
    print(ret)
    
def engine(maps):
    loaded_map,status = load_map(maps)
    init_state(loaded_map)
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
        if state['Current_Room']=='Coal Chute':
            showStatus(loaded_map)
            state['Current_Room']= state['Starting_Room']
        if action[0]=='quit':
            print('\n I dint expect that you were such a chicken..Too bad, GAME OVER.')
            break
        if action[0]=='help':
            instruction(loaded_map)
        if  not_have_passive_item(loaded_map):
            continue
        if state['Current_Room']==state['End']:
            print(loaded_map[0]['rooms'][state['Current_Room']])
            print('\n You have reached the End of this Chapter. Thanks for Playing')
            break

if __name__=='__main__':
    script, maps = argv
    engine(maps)
    
