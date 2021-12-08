from utils.run import run
import instructions


def fight_monster(weapon):
    if(weapon == 'sword'):
        run(instructions.fight_with_sword)
        return
    run(instructions.fight_no_sword)
