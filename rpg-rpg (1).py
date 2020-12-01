
import cmd
import textwrap
import sys
import os
import time
import random

######Constant Variables######
class player:
    def __init__(self):
        self.name = ''
        self.position = 'Dining Room'
        self.won = False
        self.solves = 0
        
player1 = player()

DESCRIPTION = 'description'
INFO = 'info',
PUZZLE = 'puzzle'
SOLVED = False
FORWARD = 'north'
BACKWARD = 'south'
LEFT = 'west'
RIGHT = 'east'


room_solved = {'Dining Room': False, 'Kitchen':False, 'Garden':False, 'Hallway':False, 'Metal Gate': False}


####Map Setup####
#  |-------------|      
#  |    | Dining |
#  |Hall  Room   |
#  |    | (Start)|
#  |-  ----|-  --|-----|E
#  |Kitchen|            X
#  |       |Garden     |I
#  |-------|-----------|T


""" You're in a dark mansion"""


rooms = {
    'Dining Room': {
        DESCRIPTION:"The room is dark, only a flickering candle illuminates the large oak dining table",
        INFO : 'Upon closer inspection you notice scribbles scratched into the table',
        PUZZLE : "I'm tall when I'm young, but short when I'm old, what am I?",
        SOLVED: 'a candle',
        FORWARD : 0,
        BACKWARD: 'Garden',
        LEFT: 'Hallway',
        RIGHT : 0,
        'item' : 'candlestick'
        },
    'Hallway': {
        DESCRIPTION:"The hallway is long, dark, and bare, except three paintings that line the west wall.",
        INFO: "The first painting is a portrait of a woman giving birth, the second is a boy mourning beside his father's deathbed the third is a man on a white stallion against a setting sun, you see a small, rusty plague on the ground",
        PUZZLE : 'The plaque says \'The Morning Sun\', you sense you need to place this plaque under the correct painting. Which painting does the plaque belong to?',
        SOLVED: 'the second painting',
        FORWARD : 0,
        BACKWARD: 'Kitchen',
        LEFT : 0,
        RIGHT: 'Dining Room',
        },
    'Kitchen': {
        DESCRIPTION:"The kitchen smells mouldy and stuffy. Spices line the shelves and herbs hang from the ceiling. A prepared carcass with an apple in its mouth sits on the table.",
        INFO : 'There\'s a message carved into its stomach-',
        PUZZLE: "What smells bad alive, but delicious when dead?",
        SOLVED: 'a pig',
        FORWARD : 'Hallway',
        BACKWARD : 0,
        LEFT : 0,
        RIGHT : 0,
        'item' : 'potion'
        },
    'Garden': {
        DESCRIPTION:"Beneath the jaudice moon you can see the garden is overgrown. Vines choke the house, and thorny shrubs litter the garden, a dirt path winds through the garden to a locked, metal gate. You notice footprints on the dirt path.",
        INFO : 'Someone has written something in the dirt-',
        PUZZLE: "What is the first thing a gardener plants?",
        SOLVED: 'a foot',
        FORWARD : 'Dining Room',
        BACKWARD : 0,
        LEFT : 0,
        RIGHT : 'Metal Gate',
        },
    'Metal Gate': {
        DESCRIPTION: 'A tall, rusty gate with vines tangled through it blocks you from leaving. There is no keyhole, it looks like a metal contraption unlocks the gate',
        INFO: 'The thorny vines make it impossible to climb. \nYou see a message.',
        PUZZLE:'Solve my riddles and I\'ll release you.',
        SOLVED: False,
        FORWARD: 0,
        BACKWARD: 0,
        LEFT: 'Garden',
        RIGHT: 0
        }
    }
player1.position = 'Dining Room'

#####Title Screen#####
def title_screen():
    os.system('clear')
    print('###################')
    print('##  Blind House  ##')
    print('###################')
    print('      -play-       ')
    print('      -help-       ')
    print('      -quit-       ')
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
            sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        option = input("< ")
    if option.lower()==("play"):
        start_game() #placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
            sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command")
        
######Help Menu######
def help_menu():
    print('###################')
    print('##  Blind House  ##')
    print('###################')
    print('Use the command\'s north, west, east, south to move')
    print('Type your commands to perform them')
    print('To inspect a room closely, use the command \'examine\'')
    print('Type \'map\' to reveal the map')
    print('Be mindful of your spelling')
    print('Type "back" to return to main menu')
    actions = input("> ")
    acceptable_actions = ['back','play','quit']
    while actions.lower() not in acceptable_actions:
        print("Please enter a valid command")
        actions = input("> ")
    if actions.lower() == ('back'):
        title_screen()
    elif actions.lower() == ('play'):
        game_start = True
        start_game()
    elif actions.lower() == ('quit'):
        sys.exit()



quitgame = 'quit'

def print_location():
    #Makes a pretty picture when printed and prints the cube floor information for the player.
    print('\n' + ('#' * (4 +len(player1.position))))
    print('# ' + player1.position.upper() + ' #')
    print('#' * (4 +len(player1.position)))
    print('\n' + (rooms[player1.position][DESCRIPTION]))
        
####Game Interactivity#####
def prompt():
        print('What would you like to do?')
        action = input("> ")
        acceptable_action = ['move', 'map', 'examine', 'quit']
        while action.lower() not in acceptable_action:
            print('Unknown Command, try using \'move\' or \'examine\' or \'map\'.\n')
            action = input('> ')
        if action.lower() == quitgame:
            sys.exit()
        elif action.lower() in ['move', 'go']:
            move(action.lower())
        elif action.lower() in ['examine', 'info', 'inspect']:
            examine()
        elif action.lower() in ['map']:
            print_map()



def move(myAction):
    askString = "Where would you like to " +myAction+ " to?\n> "
    destination = input(askString)
    if destination == 'north':
        if rooms[player1.position][FORWARD] == 0:
            print('You can\'t go that way!')
            move(myAction)
        else:
            move_dest = rooms[player1.position][FORWARD]
            move_player(move_dest)

    elif destination == 'south':
        if rooms[player1.position][BACKWARD] == 0:
            print('You can\'t go that way!')
            return
        else:
            move_dest = rooms[player1.position][BACKWARD]
            move_player(move_dest)

    elif destination == 'east':
        if rooms[player1.position][RIGHT] == 0:
            print('You can\'t go that way!')
            return
        else:
            move_dest = rooms[player1.position][RIGHT]
            move_player(move_dest)

    elif destination == 'west':
        if rooms[player1.position][LEFT] == 0:
            print('You can\'t go that way!')
            return
        else:
            move_dest = rooms[player1.position][LEFT]
            move_player(move_dest)

    else:
        print('Invalid Command. Try using north, south, east, or west to move')
        move(myAction)

def move_player(move_dest):
        print('You have moved to the ' + move_dest + '.')
        player1.position = move_dest
        print_location()

def examine():
    if room_solved[player1.position] == False:
        print(rooms[player1.position][INFO])
        print(rooms[player1.position][PUZZLE])
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)
    else:
        print("There is nothing new here")

def checkpuzzle(puzzle_answer):
    if player1.position == 'Metal Gate':
        if player1.solves >= 4:
            endspeech = ("You hear a mechanical click and a screech of rust. The gate slowly opens.\n")
            for character in endspeech:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            print("You take a shaky breath. You've escaped the dark mansion.")
            print("Now time to settle your nerves with a beer at the pub.")
            print("You hear the intercom crackle, \"See you again soon " + player1.name + '\".')
            sys.exit()
        else:
            print("Nothing has changed")
    else:
        if puzzle_answer == (rooms[player1.position][SOLVED]):
            room_solved[player1.position] = True
            player1.solves += 1
            print("You have solved this puzzle")
            print("\nPuzzles solved: " + str(player1.solves))
        else:
            print("Wrong answer")
            examine()

def print_map():
    print('  |-------------|         ')      
    print('  |      Dining |         ')
    print('  |Hall|  Room  |         ')
    print('  |    | (Start)|         ')
    print('  |    ---|     |-----|G  ')
    print('  |Kitchen|            A  ')
    print('  |       |   Garden  |T  ')
    print('  |-------|-----------|E  ')
    print('To return to the game type \'back\'')
    action = input('> ')
    if action.lower() == 'back':
        prompt()
    else:
        print('Type \'back\' to return to the game.')
        print_map()

def main_game_loop():
    total_puzzles = 4
    while player1.won is False:
        prompt()
    
        
def start_game():
    os.system('clear')
    question1 = 'What is your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    player1.name = player_name
    
    time.sleep(1)
    
    os.system('clear')
    
    startSequence = 'You wake up in a strange room. Its completely dark except a flickering candle on a large dining table. \nYou try the light switch- it doesn\'t work. \nA dark voice echoes from an intercom, \"Good Evening ' + player1.name + ' and welcome to my humble abode. \nYou can leave any time you want, simply solve my riddles and the gate outside will open\". \nA sinister cackle and a click brings silence. A yellow moon shines from outside. \nYou have somewhere you\'re supposed to be. \nYou need to get out of this house if you\'re ever going to make it to Happy Hour.\n'
    for character in startSequence:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    main_game_loop()


title_screen()



        


        
#
