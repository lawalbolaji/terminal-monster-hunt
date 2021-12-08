from utils.printPause import print_pause

def run(instructions, isPrompt = False, player = '', sayHello= False):
    animation = 1
    if(sayHello):
        print_pause("Hello " + player + "!", animation)
    if(isPrompt):
        for message in instructions[:-1]:
            print_pause(message, animation)
        result = input(instructions[-1]) ## last message is the prompt
        # validate input provided by game player
        while(int(result) != 1 and int(result) != 2):
            result = input("You must enter 1 or 2")
        return result     
    else:
        for message in instructions:
            print_pause(message, animation)
    return -1 ## todo: create a handler for this scenario