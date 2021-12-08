import instructions
from utils.run import run
from utils.playAgain import play_again
from moves.enterCave import enter_cave
from moves.enterHouse import enter_house
from moves.fight import fight_monster

class MonsterHunt:
    player = ''
    difficulty = 1 # todo: create implementation for difficulty level
    weapon = 'dagger'
    status = 'not started'
    
    def __init__(self, player, difficulty = 1) -> None:
        self.player = player
        self.difficulty = difficulty

    def play(self):
        while(True):
            self.status = "started"
            run(instructions.start, player = self.player, sayHello = True) ## introduce game to player
            # todo: create a new beast
            while(self.status != 'game over'):
                decision = int(run(instructions.decide, True)) ## do they want to enter house or cave
                if(decision == 1):
                    decision = int(enter_house()) ## player is inside the house, do they want to fight
                    if(decision == 1):
                        fight_monster(self.weapon)
                        self.status = 'game over'
                        continue
                    run(instructions.escape) ## run away
                    continue
                self.weapon = enter_cave(self.weapon)
            if(not play_again()):
                break

myGame = MonsterHunt("bolaji")

myGame.play()