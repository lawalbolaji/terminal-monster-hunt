from utils.printPause import print_pause

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