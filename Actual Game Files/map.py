from items import *
from interactions import *

room_Hub = {
    "name": "Hub",

    "description":
    """----------\n You are standing in the hub; the central room in the complex.\n A console stands in the middle of the room.\n Each wall has an electrical doorway leading to other rooms.\n----------""",
    "exits": {"south": "Star Wars", "east": "Indiana Jones", "west": "Shawshank", "north": "Mr Robot"},

    "items": [item_fragment1],
    "interacts": [interact_console],
    "date": "Unknown"
}

room_robot = {
    "name": "Mr Robot's Room",

    "description":
    """----------\n You enter an ancient relic of the past: A video game arcade.\n As you look around, you see computer components spread across most surfaces.\n You also spot a single functioning arcade machine.\n----------""",

    "exits": {"east": "Book of Eli", "south": "Hub", "west": "Sherlock"},

    "items": [item_phone],
    "interacts": [interact_arcade, interact_laptop],
    "date": "2016"
}

room_indiana = {
    "name": "The Temple of Doom",

    "description":
    """----------\n You find yourself standing at the base of a large set of stairs.\n The room around you seems ancient and the walls are covered in carvings which are completely unintelligible to you.\n Atop the stairs you can see a sort of shrine with <key item here> centered on it.\n----------""",

    "exits": {"north": "Book of Eli", "south": "Fight Club", "west": "Hub"},

    "items": [],
    "interacts": [interact_tombstone],
    "date": "1935"
}

room_SW = {
    "name": "Millennium Falcon",

    "description":
    """----------\n Once the light fades you find yourself standing in what appears to be the cockpit of yet another ship.\n Everything appears to be powered down however you hear noises coming from somewhere not far from you, objects seem to being moved and voices raised.\n You cautiously take a quick look around only to be discovered by a being you are unfamiliar with and it appears to be hostile!\n----------""",

    "exits": {"north": "Hub", "east": "Fight Club", "west": "Jurassic World"},

    "items": [],
    "interacts": [interact_bb8],
    "date": "A long time ago"
}

room_jurassic = {
    "name": "Jurassic World",

    "description":
    """----------\n Once you took a step through the exit you have now found yourself standing in a forest.\n You're surrounded by trees and thick bushes and the only sounds you can initially hear are of birds high up in the trees.\n After a short period of brief inspection you begin to get the feeling that you are being watched.\n----------""",

    "exits": {"north": "Shawshank", "east": "Star Wars"},

    "items": [],
    "interacts": [],
    "date": "2020"
}

room_sherlock = {
    "name": "221B Baker Street",

    "description":
    """----------\n You take a step forward exiting the shimmering lights that soon fade away.\n Taking a glance around the room you find yourself standing by a desk located\n in a darkened library.\n For what you can see in the darkness you notice multiple bookshelves located\n around you as well as open books and notepads on the desk by your side.\n----------""",

    "exits": {"east": "Mr Robot", "south": "Shawshank"},

    "items": [item_vicbook, item_violin],
    "interacts": [],
    "date": "2015"
}

room_Eli = {
    "name": "West Coast of the United States",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"south": "Indiana Jones", "west": "Mr Robot"},

    "items": [item_ammo],
    "interacts": [interact_walkietalkie, interact_radio],
    "date": "30 years after a nuclear apocalypse"
}

room_shawshank = {
    "name": "Shawshank State Penitentiary",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Sherlock","south": "Jurassic World"},

    "items": [item_shirt, item_photo],
    "interacts": [],
    "date": "1965"
}
room_fight = {
    "name": "An underground club",

    "description":
    """----------\n After taking the exit you come to find yourself laying face first on the floor with a loud ringing sound in your ears which is followed by a wave of pain.\n It takes a few moments but you finally begin to hear again however it is faded yelling at first which gradually becomes more clear.\n Pulling yourself to your feet you find yourself standing in a darkened room surrounded by yelling spectators as you come face to face with a man who shoves you back somewhat and looks as if he is ready to fight!\n----------""",

    "exits": {"north": "Indiana Jones","west":"Star Wars"},

    "items": [],
    "interacts": [],
    "date": "1999"
}

rooms = {
    "Hub": room_Hub,
    "Mr Robot": room_robot,
    "Indiana Jones": room_indiana,
    "Star Wars": room_SW,
    "Jurassic World": room_jurassic,
    "Sherlock": room_sherlock,
    "Book of Eli": room_Eli,
    "Shawshank": room_shawshank,
    "Fight Club": room_fight


}
