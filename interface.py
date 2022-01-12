from pygame import Vector2
import core
class Interface :
    def __init__(self):
        self.score = 0
        self.time = 0
        self.taille = Vector2(100,100)
        self.couleur = (100,100,100, 170)
    def ingame(self, player, ennemis):
        core.Draw.rect(self.couleur, (core.WINDOW_SIZE[0]-self.taille.x, 0, self.taille.x, self.taille.y))
        core.Draw.text((0, 0, 0), 'Score :', (core.WINDOW_SIZE[0] - self.taille.x + 10, 10), 20)
        core.Draw.text((0,0,0), str(player.getMass()), (core.WINDOW_SIZE[0]-self.taille.x+10,30), 20)