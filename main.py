import core
from creep import Creep
from fenetre import Fenetre


def setup():
    f = Fenetre()
    f.defTaille(800,800)
    f.defFps(60)
    f.defCouleur((255,255,255))
    f.set(core)

def run():
    None

core.main(setup, run)