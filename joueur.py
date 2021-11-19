from pygame.math import Vector2


class Joueur:
    def __init__(self):
        rayon = 0
        position = Vector2(0,0)
        masse = 0
        couleur = (0,0,0)
        vitesse = Vector2(0,0)
        vitesseMax = 0
        vitesseMin = 0
        positionDepart = Vector2(0,0)
        acceleartion = Vector2(0,0)
        accMax = 0
        accMin = 0
        force = Vector2(0,0)
        nom = ""
        score = 0
