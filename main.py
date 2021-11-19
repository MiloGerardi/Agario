import core
import creep
from creep import Creep


def setup():
    print("setup START______")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    print("setup END______")

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
