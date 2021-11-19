import core
from creep import Creep


def setup():
    print("setup START______")
    core.fps = 30
    core.WINDOW_SIZE = [800,800]

    core.memory("listcreep", [])
    core.memory("listcreep", 100)
    for i in range(0, core.memory("listcreep")):
        core.memory("listcreep").append(Creep())

core.main(setup, run)