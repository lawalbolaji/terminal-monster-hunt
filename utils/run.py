from utils.printPause import print_pause

def run(instructions, isPrompt):
    animation = 2
    for message in instructions[:-1]:
        print_pause(message, animation)
    if(isPrompt):
        result = input(instructions[-1]) ## last message is the prompt
        # validate input provided by game player
        while(int(result) != 1 and int(result) != 0):
            result = input("You must enter 1 or 2")
        return result 
    return -1 ## we create a handler for this scenario