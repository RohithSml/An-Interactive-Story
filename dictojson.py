import json


maps= [

{'rooms' : {'Room 0' :['You open your eyes. You feel the chilling cold on your back, you get up and find yourself alone in a dim lit room."What is this place ?. You ask yourself. Having no re-collection on how you got here, you look around. The floor is made of wood, the walls look old, there is nothing in this room, you look north and see a door.it seems unlocked and partialy opened', {'north' : 'Creeky Hallway','item':''}],

               'Creeky Hallway' :['You are now in a hallway, with a chandelier hanging in the middle of the hallway, as you take each step, the wood creeks beneth you. you see big framed-pictures hanging on both sides of the hall, with torn-up pictures in them, you seem somehow disturbed by this. You can see three exits towards the north, west and east.', {'north' : 'Dusty Hallway', 'west' : 'Organ Room', 'east' : 'Chapel', 'south' : 'Room 0', 'item' :''}],

               'Organ Room' :['As you enter this room,you see a pipe organ infront of you, with its rusty pipes running through the ceiling. The organ looks busted. you see a Battered_Ring kept on one of the keys. You also feel a gentle breeze from the north, but there are no visible windows or openings. huh? thats unsettling. ', {'east':'Creeky Hallway','item':'battered_ring'}],

               'Chapel' :['You are in a huge room, what seems to be like a chapel of some sorts, it is not the typical chapel you would see normally, there is a statue of a saint like figure in the far end of the chapel, the statue looks very old and it depicts of a bearded man in robes holding a book high in his right hand, and left hand holding a lantern towards the middle of the room. It seems there is no way to move forward', {'west':'Creeky Hallway', 'item':'lantern'}],

               'Dusty Hallway':['You find yourself in another hallway, which is infested with cobwebs,and the floor is partially gone one wrong step and its Game-Over, you see several animal skulls fixed on either sides of the walls, you feel a cold chill running down your spine, and decide not to linger around this place. You find three exits. Towards the north is a staircase going up and An unlocked door towads the east.', {'north':'Conservatory', 'east':'Coal Chute', 'south':'Creeky Hallway'}],

                'Coal Chute':['As you enter this room, You hear a creeking sound, *BANG*!!!, The coal chute you were standing on opens up and engulfs you, into its dark pits..'],
                
               'Conservatory' :['You have reached the upper floor, this room looks like a conservatory, with glass roof and the walls are of glass as well,there are many shelves around you, each self has about 10 different potted plants/vines, but all seem dried up and rotten. You look out through the glass, and much to your dismay, you see nothing but pitch black, not even moonlight. You notice a skull of a raven, seems odly misplaced on the desk. You look around and see the glass wall on the east is blacked off with a black linen type cloth, and there seems to be an opening..', {'east':'Laboratory', 'south':'Dusty Hallway', 'item':'skull'}],
        
               'Laboratory' :['You are in a laboratory of some sort, there is a old CRT monitor hooked up to wires and connected through the walls and the monitor is flickering. There appears to be a stone hand, with its index finger pointing up, and it seems the stone hand is also hooked up to a bunch of wires beside the monitor. You look around,towards the south and east you see flesh like walls pulse with a steady heartbeat, your own heart beats with the rythm of the house, you feel drawn into the walls.', {'south':'Library', 'east':'Bloody Room','west':'Conservatory','item':''}],

               'Bloody Room':['As the flickering light blub looms over you head, The smell in this room is horrible, it smells like death, like blood, a slaughter house smell. You look forward, your heart stops for a brief second as you comprehend what you are seeing, In the centre, a pedestal with mysterious symbols etched into it,and holds a fresh goat head on it, its eyes gouged out. The blood from the decapitated goat is still oozing out onto the pedestal,the blood had filled the cravesses shaped like a pentagram around the pedestal on the floor. You retch as the sight is nausiating. You notice a sacrifical_dagger with mysterious symbols sticking out of the forehead of the goat. There is nowhere else to go but go back west', {'west':'Laboratory', 'item':'sacrifical_dagger'}],

               'Library':['A small room, which seems like a library. The books are neatly stacked throught out the room. The books have collected a lot of dust as if no one has taken them for centuries. Out of sheer curiosity you take up a few books. The books are written in some other language with mystical symbols. you put them back. you see a pedestal  with a symbol of a snake curled like the number 8 and biting its tail. There is noway to move forward.', {'north':'Laboratory'}],

                'Room Zen': 'You enter this room not knowing what to expect, you see a glimmer of light far ahead, is it your escape from this horror...',

                'Secret Room':['As you look around, towrads the north you see a statue of the Vitruvian Man emmbedded in the walls, something seems different there is a stone heart at its centre with a small slit in it. It seems like something can be placed in it.', {'south':'Organ Room'}]}}, 
    
    { 'action' : {

                 'battered_ring' : ['Laboratory', '\n\nYou take out the Battered Ring etched with strange symbols, as you slowly try to place the ring in the index finger of the stone hand *thud* the ring gets fixed in the stone and you see a faint glow on the engravings of the ring, Suddenly you hear a *THUD* comming from downstaris near the Organ room.\n'],

                 'skull' : ['Library', '\n\nThe symbol on the pedestal looks very familiar, ah yes !, you take out the skull, it has the same symbol as the pedestial only difference is that the there is a pentagram etched on its forehead. you place the skull on the pedestal. you see the pedestal slowing sinking in.. you hear a *THUDD* comming from the Organ Room...\n'],
        
                 'sacrificial_dagger' : ['Secret Room', '\n\nAs you take the twisted shard of iron, covered on blood and you slowly placed it in the heart. the symbols glow brightly and the Vitruvian man splits into two to make way for an exit\n']}
    },
    {'Initial_Room' : 'Room 0'},

    {'items':[{'Room 0':'', 'Creeky Hallway':'','Dusty Hallway':'','Laboratory':'','Library':'','Secret Room':'','End':'','Coal Chute':'', 'Organ Room':'battered_ring', 'Chapel':'lantern', 'Conservatory':'skull', 'Bloody Room':'sacrificial_dagger'}]},

    {'passive item' : ['lantern', 'Dusty Hallway','\n\nAs you walked over to through next room, you loose your footing and fall down into a dark abyss']},

    {'secret_room_avl' :['Organ Room',{'north' : 'Secret Room','east':'Creeky Hallway'}]},

        {'count':0},

        {'End status': ['Secret Room',False]},

        {'End direction':['Secret Room',{'north':'Room Zen', 'south':'Organ Room'}]},

        {'End' :'Room Zen'},

    {'secret_room_status' : {'Laboratory':False, 'Library':False,'access':False}},

    {'Post Action Description':{'Laboratory' :'You are in a laboratory of some sort, there is a old CRT monitor hooked up to wires and connected through the walls. The monitor stopped flickering. The Battered Ring still glows faintly on the stone hand which is hooked up to a bunch of wires beside the monitor. You look around,towards the south and east you see flesh like walls pulse with a steady heartbeat, your own heart beats with the rythm of the house, you feel drawn into the walls.',

     'Library':'A small room, which seems like a library. The books are neatly stacked throught out the room. The books have collected a lot of dust as if no one has taken them for centuries. Out of sheer curiosity you take up a few books. The books are written in some other language with mystical symbols. you put them back. You  can see the  pedestal with the skull on it. There is noway to move forward.',

                                'Secret Room':'As you look around, towrads the north you see a statue of the Vitruvian Man split into two making an exitway.'}},

    {'help':'\n\n For movement use : move \n For picking up items to inventory use : get \n For using item use keyword : use \n'} 

]
                          


dump_maps = json.dumps(maps)
load_maps = json.loads(dump_maps)

with open('maps.json', 'w') as output_file:
    json.dump(load_maps, output_file)

