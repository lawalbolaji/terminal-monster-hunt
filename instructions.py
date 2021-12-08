from utils.beast import beast
from utils.weapon import weapon

current_beast = beast()
current_weapon = weapon()

start = [
    "You find yourself standing in an open field, filled with grass and yellow wildflowers.",
    "Rumor has it that a troll is somewhere around here, and has been terrifying the nearby village.",
    "In front of you is a house.",
    "To your right is a dark cave.",
    "In your hand you hold your trusty (but not very effective) dagger.\n"
]

decide = [
    "Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)",
    "" # prompt
]

house = [
    "You approach the door of the house.",
    f"You are about to knock when the door opens and out steps a {current_beast}.",
    f"Eep! This is the {current_beast}'s house!",
    f"The {current_beast} attacks you!",
    "Would you like to (1) fight or (2) run away?" # prompt
]

cave = [
    "You peer cautiously into the cave.",
    "It turns out to be only a very small cave.",
    "Your eye catches a glint of metal behind a rock.",
    f"You have found the {current_weapon}",
    f"You discard your silly old dagger and take the {current_weapon} with you.",
    "You walk back out to the field.\n",
]

fight_no_sword = [
    "You do your best...",
    "but your dagger is no match for the troll.",
    "You have been defeated!"
]

fight_with_sword = [
    f"As the {current_beast} moves to attack, you bring our your {current_weapon}",
    f"The {current_weapon} shines brightly in your hand as you brace yourself for the attack.",
    f"But the {current_beast} takes one look at your shiny new toy and runs away!",
    f"You have rid the town of the {current_beast}. You are victorious!",
]

escape = [
    "You run back into the field. Luckily, you don't seem to have been followed."
]