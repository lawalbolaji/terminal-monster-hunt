from utils.beast import beast

start = [
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

house_no_sword = [
    "You approach the door of the house.",
    "You are about to knock when the door opens and out steps a troll.",
    "Eep! This is the troll's house!",
    "The troll attacks you!",
    "You feel a bit under-prepared for this, what with only having a tiny dagger.",
    "Would you like to (1) fight or (2) run away?" # prompt
]

fight_with_sword = [
    "You do your best...",
    "but your dagger is no match for the troll.",
    "You have been defeated!"
]

cave = [
    "You peer cautiously into the cave.",
    "It turns out to be only a very small cave.",
    "Your eye catches a glint of metal behind a rock.",
    "You have found the magical Sword of Ogoroth!",
    "You discard your silly old dagger and take the sword with you.",
    "You walk back out to the field.\n",
]

field = [
    "Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)" # prompt
]

house_with_sword = [
    "You approach the door of the house.",
    f"You are about to knock when the door opens and out steps a {beast()}.",
    f"Eep! This is the {beast()}'s house!",
    f"The {beast()} attacks you!",
    "Would you like to (1) fight or (2) run away?" # prompt
]

fight_no_sword = [
    f"As the {beast()} moves to attack, you unsheath your new sword.",
    "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
    f"But the {beast()} takes one look at your shiny new toy and runs away!",
    f"You have rid the town of the {beast()}. You are victorious!",
]

escape = [
    "You run back into the field. Luckily, you don't seem to have been followed."
]
