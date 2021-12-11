from utils.printPause import print_pause
from utils.inputs import valid_input


def run(instructions, isPrompt=False, player='', 
            sayHello=False, options = ['1', '2']):
    animation = 1
    if(sayHello):
        print_pause("Hello " + player + "!", animation)
    if(isPrompt):
        for message in instructions[:-1]:
            print_pause(message, animation)
        # validate input and return player choice
        return valid_input(instructions[-1], options)
    else:
        for message in instructions:
            print_pause(message, animation)
    return -1  # todo: create a handler for this scenario
