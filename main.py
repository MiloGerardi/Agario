import core
from creep import Creep
from fenetre import Fenetre
from joueur import Joueur
from pygame import Vector2
from ennemis import Ennemi


def setup():
    f = Fenetre()
    f.defTaille(800,800)
    f.defFps(60)
    f.defCouleur((255,255,255))
    f.set(core)

    core.memory("listcreep", [])
    core.memory("nbcreep", 150)
    for c in range(core.memory("nbcreep")):
        core.memory("listcreep").append(Creep())
        core.memory("listcreep")[c].update()
    core.memory("joueur", Joueur())

    core.memory("listennemis", [])
    for c in range(3):
        core.memory("listennemis").append(Ennemi())
    core.memory("listennemis")[0].setPosition(Vector2(50, 50))


def run():
    core.cleanScreen()
    for c in core.memory("listcreep"):
        c.show(core.screen)
    core.memory("joueur").calculRayon()
    core.memory("joueur").calculVitesse()
    core.memory("joueur").deplacer()
    core.memory("joueur").afficher(core.screen)
    creepEating(core.memory("joueur"), core.memory("listcreep"))
    for i in core.memory("listennemis"):
        i.calculRayon()
        i.calculVitesse()
        i.deplacer(core.memory("joueur"), core.memory("listcreep"))
        i.afficher(core.screen)
        creepEating(i, core.memory("listcreep"))


def creepEating(player, creepList):
    for i in creepList :
        if collide(player, i, 0) :
            player.addMass(i.getMass())
            i.update()

def collide(circle_1, circle_2, tolerance):
    dist = Vector2((circle_1.getPosition().x-circle_2.getPosition().x), (circle_1.getPosition().y-circle_2.getPosition().y))
    dist = dist.magnitude()
    if dist <= circle_1.getRadius()+circle_2.getRadius()+tolerance :
        return True
    else:
        return False

core.main(setup, run)

