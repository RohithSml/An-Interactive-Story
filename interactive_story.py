from parser import *
import time
from sys import argv
script,mapss = argv

print("\n\nAn Interactive Story: by Rohith Jacob Samuel")
print("\n--------------------------------------------")
print('\n')
time.sleep(1)
print(mapss,': is loading.......\n\n')
time.sleep(2)
print("Welcome to this Interactive Story")
print("\n  Controls:\n")
print("\n   The Directions are 'north', 'south','east' and 'west'\n\n   For movement use the keyword: 'move', For example: move south\n\n   For obtaining items for your inventory use keyword: 'get', For example: get cup\n\n   For using items from inventory in that specific room use keyword: 'use', For example: use cup\n\n")
answer=input("Would you like to start ?. (y/n)")
if answer in ['y','Y']:
    engine(mapss)
else:
    exit()
