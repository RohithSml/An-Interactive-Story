from parser import engine
import time
from sys import argv
script,mapss = argv

def main():
    print ("""

    An Interactive Story: by Rohith Jacob Samuel
    --------------------------------------------

    """)

    print(mapss,': is loading.......\n\n')
    print("""Welcome to this Interactive Story

      Controls:

      The Directions are 'north', 'south','east' and 'west'.
      For movement use the keyword: 'move', For example: move south

      For obtaining items for your inventory use keyword: 'get', For example: get cup
      For using items from inventory in that specific room use keyword: 'use', For example: use cup
    """)
    answer=input("Would you like to start ?. (y/n)")
    if answer in ['y','Y']:
        engine(mapss)
    else:
        exit()

if __name__ == "__main__":
    main()
