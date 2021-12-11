from utils.inputs import valid_input


def play_again(prompt = "Would you like to play again? (y/n)", options = ['y', 'n']):
    result = valid_input(prompt, options)
    if(result == 'y'):
        return True
    return False
