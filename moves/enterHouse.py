from utils import run

def enter_house(weapon):
    run()
    if(weapon):
        return -1 # this indicates a terminal scenario
    return "next"