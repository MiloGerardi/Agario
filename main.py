import core
import creep
from creep import Creep
from fenetre import Fenetre


def setup():
    f = Fenetre()
    f.defTaille(800,800)
    f.defFps(60)
    f.defCouleur((255,255,255))
    f.set(core)

    core.memory("listcreep", [])
    core.memory("nbcreep", 100)
    for c in range(0, core.memory("nbcreep")):
        core.memory("listcreep").append(Creep())


def run():
    core.cleanScreen()
    core.printMemory()

    for c in core.memory("nbcreep"):
        creep.show(core.screen)
        creep.update()

core.main(setup, run)
