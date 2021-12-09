def play_again():
    result = input("Would you like to play again? (y/n)")
    while(result != 'y' and result != 'n'):
        result = input("please enter a valid response")
    if(result == 'y'):
        return True
    return False