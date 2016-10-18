#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from interactions import *
from gameparser import *
import config
import time
import sys
import datetime
from datetime import datetime
global introcount
inv = []

def introanimation():
    config.won = False
    global introcount
    intro = "abcdefghabcdefghabcdefghabcdefghabcdefghabcdefghabcdefghx"
    for char in intro:
        introcount = introcount - 1
        time.sleep(0.01)
        if introcount == 0:
            print("Loading complete.\n\n")
            time.sleep(1)
            print_by_char("Welcome.",0.02)
            time.sleep(1.5)
            title()
            break
        time.sleep(0.006)
        if char is "a":
            print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "b":
            print(" \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "c":
            print("  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "d":
            print("   \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        time.sleep(0.006)
        if char is "e":
            print("   ////////////////////////////////////////")
        time.sleep(0.006)
        if char is "f":
            print("  ////////////////////////////////////////")
        time.sleep(0.006)
        if char is "g":
            print(" ////////////////////////////////////////")
        time.sleep(0.006)
        if char is "h":
            print("////////////////////////////////////////")
        time.sleep(0.006)
        if char is "x":
            print("Loading...")
            time.sleep(0.01)
            introanimation()

def title():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("--------------------------------------------------------------------------------------------------------")
    time.sleep(0.02)
    print("   |             /                                  |                                  \             |")
    time.sleep(0.02)
    print("   |            /                                   |                                   \            |")
    time.sleep(0.02)
    print("   |           /                                    |                                    \           |")
    time.sleep(0.02)
    print("   |          /                                    /|\                                    \          |")
    time.sleep(0.02)
    print("   |         /                                     |||                                     \         |")
    time.sleep(0.02)
    print("   |        /                                     / | \                                     \        |")
    time.sleep(0.02)
    print("   |       /                                     /  |  \                                     \       |")
    time.sleep(0.02)
    print("   |      /                                      |  |  |                                      \      |")
    time.sleep(0.02)
    print("   |     /                                       |  |  |                                       \     |")
    time.sleep(0.02)
    print("   |    /                                        |  |  |                                        \    |")
    time.sleep(0.02)
    print("   |   /                                        /   |   \                                        \   |")
    time.sleep(0.02)
    print("   |  /                                         |   |   |                                         \  |")
    time.sleep(0.02)
    print("   | /                                         /    |    \                                         \ |")
    time.sleep(0.02)
    print("   |/                     ▄████████            |    |    |            ▄███████▄                     \|")
    time.sleep(0.02)
    print("   |                     ███    ███            |    |    |            ███    ███                     |")
    time.sleep(0.02)
    print("   |                     ███    █▀             |    |    |            ███    ███                     |")
    time.sleep(0.02)
    print("   |                     ███                  /     |     \           ███    ███                     |")
    time.sleep(0.02)
    print("   |                    ▀███████████          |     |     |          ▀█████████▀                     |")
    time.sleep(0.02)
    print("   |                             ███         /      |      \          ███                            |")
    time.sleep(0.02)
    print("   |                       ▄█    ███        /       |       \         ███                            |")
    time.sleep(0.02)
    print("   |                      ▄████████▀        █████████████████        ▄████▀                          |")
    time.sleep(0.02)
    print("   |                                        ▀███████████████▀                                        |")
    time.sleep(0.02)
    print("   |                                         ▀█████████████▀                                         |")
    time.sleep(0.02)
    print("   |                                 ___▄▄    \     |     /    ▄▄___                                 |")
    time.sleep(0.02)
    print("   |                         ______%@   ███▄   \----|----/   ▄███   @%______                         |")
    time.sleep(0.02)
    print("   |                 ______.@#          █████\   \  |  /   /█████          #@.______                 |")
    time.sleep(0.02)
    print("   |           _____%@                  █████ \__ \ | / __/ █████                  @%______          |")
    time.sleep(0.02)
    print("   |    ____.@(                         █████    \  |  /    █████                         (@.____    |")
    time.sleep(0.02)
    print("   |---%@-------------------------------█████------#|#------█████-------------------------------@%---|")
    time.sleep(0.02)
    print("   |    ¯¯¯¯¯¯\@,______                 █████  __// | \\\__  █████                 ______,@/¯¯¯¯¯¯    |")
    time.sleep(0.02)
    print("   |                  %&______          █████ /  /  |  \  \ █████          ______&%                  |")
    time.sleep(0.02)
    print("   |                         *@,______  ████▀  /    |    \  ▀████   _____,@*                         |")
    time.sleep(0.02)
    print("   |                                 #@_██▀   /     |     \   ▀██__@#                                |")
    time.sleep(0.02)
    print("   |                                         ▄█████████████▄                                         |")
    time.sleep(0.02)
    print("   |                                        ▄███████████████▄                                        |")
    time.sleep(0.02)
    print("   |                                        █████████████████                                        |")
    time.sleep(0.02)
    print("   |                      ▄██████▄          \       |       /         ▄█   ▄█▄                       |")
    time.sleep(0.02)
    print("   |                     ███    ███          \      |      /         ███ ▄███▀                       |")
    time.sleep(0.02)
    print("   |                     ███    ███           |     |     |          ███ ██▀                         |")
    time.sleep(0.02)
    print("   |                     ███    ███           \     |     /         ▄█████▀                          |")
    time.sleep(0.02)
    print("   |                     ███    ███           |     |     |        ▀▀█████▄                          |")
    time.sleep(0.02)
    print("   |                     ███    ███            \    |    /            ███ ██▄                        |")
    time.sleep(0.02)
    print("   |                     ███    ███            |    |    |            ███ ▀███                       |")
    time.sleep(0.02)
    print("   |\                     ▀██████▀             |    |    |            ███   ▀█▀                     /|")
    time.sleep(0.02)
    print("   | \                                         |    |    |            ▀                            / |")
    time.sleep(0.02)
    print("   |  \                                        \    |    /                                        /  |")
    time.sleep(0.02)
    print("   |   \                                        |   |   |                                        /   |")
    time.sleep(0.02)
    print("   |    \                                       |   |   |                                       /    |")
    time.sleep(0.02)
    print("   |     \                                      |   |   |                                      /     |")
    time.sleep(0.02)
    print("   |      \                                     \   |   /                                     /      |")
    time.sleep(0.02)
    print("   |       \                                     |  |  |                                     /       |")
    time.sleep(0.02)
    print("   |        \                                    \  |  /                                    /        |")
    time.sleep(0.02)
    print("   |         \                                    | | |                                    /         |")
    time.sleep(0.02)
    print("   |          \                                   \ | /                                   /          |")
    time.sleep(0.02)
    print("   |           \                                   |||                                   /           |")
    time.sleep(0.02)
    print("   |            \                                   |                                   /            |")
    time.sleep(0.02)
    print("   |             \                                  |                                  /             |")
    time.sleep(0.02)
    print("---|-------------------------------------------------------------------------------------------------|---")
    main_menu()

def main_menu():

    print("\n                  Welcome to -name of game-. Please select an option by typing it below.\n\n                                  -NEW GAME- || -CREDITS- || -QUIT- \n")

    selection = normalise_input(input('> '))

    parsed_input = ''
    count = 0 # Count for adding spaces
    for x in selection:
        parsed_input = parsed_input + x
        count = count + 1
        if count <= (len(selection) - 1): # Only Adds a space inbetween words if theres more than 1 word in input
            parsed_input = parsed_input + ' '

    selection = parsed_input

    if selection == "new" or selection == "new game":
        print("Starting new game...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        main()
    elif selection == "credits":
        print("A game by Team 5.\n")
        time.sleep(1)
        main_menu()
    elif selection == "quit":
        print("Quitting so soon? We don't think so.")
        main_menu()
    else:
        print("Cooperate.\n")
        time.sleep(1)
        main_menu()

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    itemlist = ""
    for i in items:
        itemlist = itemlist + i["name"] + ", "
    itemlist = itemlist[:len(itemlist)-2]
    return itemlist


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    itemlist ="There is " + list_of_items(room["items"]) + " here.\n"
    if itemlist != "There is "+" here.\n":
        print(itemlist)

def print_room_interacts(room):
    interactlist ="You can interact with " + list_of_items(room["interacts"]) + " here.\n"
    if interactlist != "You can interact with "+" here.\n":
        print(interactlist)


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    print("You have " + list_of_items(items) +".\n")



def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("\n\n")
    print_by_char("TIME: "+ str(datetime.now().time())[:8],0.01)
    time.sleep(0.5)
    print_by_char("DATE: "+room["date"],0.01)
    time.sleep(0.5)
    print_by_char("LOCATION: "+room["name"].upper(),0.01)
    time.sleep(1)
    # Display room description
    print(room["description"])

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_search(room_items, room_interacts):
    if print_room_items(current_room) != None:
        print(print_room_items(current_room))
        print()
    if print_room_interacts(current_room) != None:
        print(print_room_interacts(current_room))
        print()
    elif current_room["items"] == None and current_room["interacts"] == None:
        print("There is nothing here.")
        print()
    for i in room_items:
        print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    for i in room_interacts:
        print("INTERACT " + i["id"].upper() + " to interact with " + i["name"] + ".")
    print("RETURN to stop searching the room.")

def print_inventory(inventory):
    for i in inventory:
        if i != item_notepad:
            print("DROP " + i["id"].upper() + " to drop " + i["name"] + ".")
    for i in inventory:
        print("EXAMINE " + i["id"].upper() + " to examine " + i["name"] + ".")
    print("RETURN to close your inventory.")


def print_menu(exits, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can type:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    print("INVENTORY to open your inventory.")
    print('SEARCH to search ' + current_room['name'] + '.')
    print("NOTE to add to your notepad.")
    #
    # COMPLETE ME!
    #

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if is_valid_exit(current_room["exits"],direction) == True:
        current_room = move(current_room["exits"],direction)
        time.sleep(1)
    else:
        print ("You cannot go there.")
        time.sleep(1.5)

def execute_note():
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    notes = item_notepad["description"]
    print(notes)
    item_notepad["description"] = notes + input("What would you like to add?\n") + "\n"
    print('\nAdded to notepad.')
    time.sleep(1)

def execute_search():
    print()
    print_search(current_room['items'], current_room['interacts'])
    command = normalise_input(input())
    if command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
            execute_search()
        else:
            print("Take what?")
            time.sleep(0.8)
    elif command[0] == 'interact':
        if len(command) > 1:
            execute_interact(command[1])
            execute_search()
        else:
            print('Interact with what?')
    elif command[0] == 'return':
        print("Returning to room...")
        time.sleep(1)
    else:
        print("That doesn't make sense.")

def execute_inventory():
    print()
    print_inventory(inventory)
    command = normalise_input(input())
    if command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
            execute_inventory()
        else:
            print("Drop what?")
            time.sleep(0.8)
    elif command[0] == 'examine':
        if len(command) > 1:
            execute_examine(command[1])
            execute_inventory()
        else:
            print('Examine what?')
    elif command[0] == 'return':
        print("Returning to room...")
        time.sleep(1)
    else:
        print("That doesn't make sense.")

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    takeable = False
    for i in current_room["items"]:
        if i["id"] == item_id:
            takeable = True
            inventory.append(i)
            current_room["items"].remove(i)
            print("You have taken " + i['name'] + ".")
            time.sleep(1.2)
    if takeable == False:
        print("You cannot take that.")
        time.sleep(1.5)


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    droppable = False
    for i in inventory:
        if i["id"] == item_id:
            droppable = True
            inventory.remove(i)
            current_room["items"].append(i)
            print("You have dropped the " + i['id'] + ".")
            time.sleep(1.2)
    if droppable == False:
        print("You cannot drop that.")
        time.sleep(1.5)

def execute_examine(item_id):
    examinable = False
    for i in inventory:
        if i['id'] == item_id:
            examinable = True
            print()
            print(i['description'])
            # Added varying wait time for reading item description
            if len((i['description'].split())) >= 20:
                time.sleep(8)
            elif len((i['description'].split())) >= 10:
                time.sleep(4)
            else:
                time.sleep(2)
    if examinable == False:
        print('You cannot examine that.')
        time.sleep(1.5)

def execute_interact(interact_id):
	interactable = False
	for i in current_room["interacts"]:
		if i['id'] == interact_id:
			interactable = True
			print("\n")
			i['action']()
			time.sleep(2)
	if interactable == False:
		print('You cannot interact with that.')
		time.sleep(1.5)

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
            time.sleep(0.8)

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            time.sleep(0.8)

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            time.sleep(0.8)

    elif command[0] == 'examine':
    	if len(command) > 1:
    		execute_examine(command[1])
    	else:
            print('Examine what?')
            time.sleep(0.8)

    elif command[0] == 'interact':
    	if len(command) > 1:
    		execute_interact(command[1])
    	else:
    		print('Interact with what?')
            #time.sleep(0.8) -- WHY DOESN'T THIS LINE WORK?!

    elif command[0] == 'search':
    		execute_search()

    elif command[0] == 'inventory':
            execute_inventory()

    elif command[0] == 'note':
    		execute_note()
    else:
        print("This makes no sense.")
        time.sleep(0.8)

def menu(exits, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, inv_items)

    # Read player's input
    user_input = input()

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    if normalised_user_input != None:
        return normalised_user_input
    else:
        return "invalid"

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    global command
    # Main game loop
    while config.won == False:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        command = menu(current_room["exits"], inventory)
        execute_command(command)
    global introcount
    print_by_char("You hear a loud mechanincal whir and the ceiling begins to open.\nThe floor begins to rise, pushing you towards the outside world.\nYou reach ground level and walk onto the dirt in front of you.\n\n\nWhere are you?",0.02)
    time.sleep(3)
    print("\n\n\YOU WON, GG")
    time.sleep(5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def print_by_char(string,wait):
	for char in string:
		sys.stdout.write( '%s' % char )
		sys.stdout.flush()
		time.sleep(wait)
	print()



introcount = 20
print_by_char("Initialising...",0.02)
time.sleep(0.5)
print_by_char("Loading...",0.02)
time.sleep(1.2)
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    introanimation()
