import time

instructions_00 = [
    "You find yourself standing in an open field, filled with grass and yellow wildflowers.",
    "Rumor has it that a troll is somewhere around here, and has been terrifying the nearby village.",
    "In front of you is a house.",
    "To your right is a dark cave.",
    "In your hand you hold your trusty (but not very effective) dagger.\n",
    "Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)",
    "" # prompt
]
instructions_10 = [
    "You approach the door of the house.",
    "You are about to knock when the door opens and out steps a troll.",
    "Eep! This is the troll's house!",
    "The troll attacks you!",
    "You feel a bit under-prepared for this, what with only having a tiny dagger.",
    "Would you like to (1) fight or (2) run away?" # prompt
]
instructions_1010 = [
    "You do your best...",
    "but your dagger is no match for the troll.",
    "You have been defeated!"
]
instructions_01 = [
    "You peer cautiously into the cave.",
    "It turns out to be only a very small cave.",
    "Your eye catches a glint of metal behind a rock.",
    "You have found the magical Sword of Ogoroth!",
    "You discard your silly old dagger and take the sword with you.",
    "You walk back out to the field.\n",
    "Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)" # prompt
]
instructions_0110 = [
    "You approach the door of the house.",
    "You are about to knock when the door opens and out steps a gorgon.",
    "Eep! This is the gorgon's house!",
    "The gorgon attacks you!",
    "Would you like to (1) fight or (2) run away?" # prompt
]
instructions_011010 = [
    "As the gorgon moves to attack, you unsheath your new sword.",
    "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
    "But the gorgon takes one look at your shiny new toy and runs away!",
    "You have rid the town of the gorgon. You are victorious!",
]
instructions_011001 = [
    "You run back into the field. Luckily, you don't seem to have been followed."
]
instructions_0101 = [
    "You approach the door of the house.",
    "You are about to knock when the door opens and out steps a pirate.",
    "Eep! This is the pirate's house!",
    "The pirate attacks you!",
    "Would you like to (1) fight or (2) run away?", # prompt
]
instructions_010110 = [
    "As the pirate moves to attack, you unsheath your new sword.",
    "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
    "But the pirate takes one look at your shiny new toy and runs away!",
    "You have rid the town of the pirate. You are victorious!"
]

# todo: act based on response
def play_again():
    return input("Would you like to play again? (y/n)")
    

def run(instructions, isPrompt):
    animation = 2
    for message in instructions[:-1]:
        print_pause(message, animation)
    if(isPrompt):
        result = input(instructions[-1]) ## last message is the prompt
        # validate input provided by game player
        while(int(result) != 1 or int(result) != 0):
            result = input(instructions[-1])
        return result 
    return -1 ## we create a handler for this scenario

def house(isWeapon):
    run()
    if(isWeapon):
        return -1 # this indicates a terminal scenario
    return "next"

def fight():
    pass

def cave():
    pass

def field():
    pass


def print_pause(message, duration):
    print(message)
    time.sleep(duration)

game_map = {
    "start": {
        "instructions": instructions_00,
        "next": "",
        "1": {
            "instructions": instructions_10,
            "1": {
                "instructions": instructions_1010,
                "1": {},
                "2": {},
                "stop": True,
                "level": 2
            },
            "2": {},
            "stop": False,
            "level": 1
        },
        "2": {
            "instructions": instructions_01,
            "1": {
                "instructions": instructions_0110,
                "1": {
                    "instructions": instructions_011010,
                    "1": {},
                    "2": {},
                    "stop": True,
                    "level": "3"
                },
                "2": {
                    "instructions": instructions_011001,
                    "1": {},
                    "2": {},
                    "stop": True,
                    "level": "3"
                },
                "stop": False,
                "level": "2"
            },
            "2": {
                "instructions": instructions_0101,
                "1": {},
                "2": {},
                "stop": True,
                "level": "2",
                "next": "" # next move, automatically set
            },
            "stop": False,
            "level": 1
        }
    }
}


# --------------------------------------------START--------------------------------------------------
# game flow

win = ['01*****', '1001**']

# intro
print(run(instructions_00))

time.sleep(5) # pause between game runs

# level1
print(run(instructions_10))