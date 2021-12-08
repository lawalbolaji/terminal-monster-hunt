from utils.run import run
import instructions

def enter_cave(weapon):
    if(weapon == 'sword'):
        print('Nothing to see here again, you have already packed everything')
    else:
        run(instructions.cave)
    return "sword"