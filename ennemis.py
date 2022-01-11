from pygame.math import Vector2
import pygame
import core
import math


class Ennemi:
    def __init__(self):
        self.rayon = 0
        self.position = Vector2(core.WINDOW_SIZE[0]/2,core.WINDOW_SIZE[1]/2)
        self.masse = 200
        self.couleur = (255,0,0)
        self.vitesse = Vector2(0,0)
        self.vitesseMax = 0
        self.nom = ""
        self.score = 0
        self.target = Vector2(0,0)

    def calculVitesse(self):
        self.vitesseMax = 2.5-self.rayon/100

    def afficher(self, surface):
        pygame.draw.circle(surface, self.couleur, [int(self.position.x), int(self.position.y)], self.rayon)

    def deplacer(self, joueur, creeps):
        self.comportement(joueur, creeps)
        if self.target != Vector2(0,0):
            self.vitesse = Vector2(self.target.x - self.position.x, self.target.y - self.position.y)
            self.vitesse = self.vitesse.normalize()
            self.vitesse = self.vitesse*self.vitesseMax
        if self.position.x+self.vitesse.x+self.rayon >= core.WINDOW_SIZE[0] or self.position.x+self.vitesse.x-self.rayon <= 0:
            self.vitesse.x = 0
        if self.position.y+self.vitesse.y+self.rayon >= core.WINDOW_SIZE[1] or self.position.y+self.vitesse.y-self.rayon <= 0:
            self.vitesse.y = 0
        self.position += self.vitesse
    def calculRayon(self):
        self.rayon = round(math.sqrt((self.masse*2)/3.14))
    def addMass(self, m):
        self.masse += m
    def getRadius(self):
        return self.rayon
    def getPosition(self):
        return self.position
    def distance(self, circle):
        return Vector2(self.position.x-circle.getPosition().x, self.position.y-circle.getPosition().y).magnitude()
    def mangerCreep(self, creeps):
        dist = []
        for c in creeps :
            dist.append(self.distance(c))
            if min(dist)==self.distance(c) :
                self.target = c.getPosition()
    def mangerJoueur(self, joueur):
        self.target = joueur.getPosition()
    def fuirJoueur(self, joueur):
        point = Vector2(self.position.x-joueur.getPosition().x, self.position.y-joueur.getPosition().y)
        self.target = self.position+point
    def comportement(self, joueur, creeps):
        if joueur.getMass()<self.masse :
            self.mangerJoueur(joueur)
        elif joueur.getMass()>self.masse and self.distance(joueur)<200 :
            self.fuirJoueur(joueur)
        else:
            self.mangerCreep(creeps)
    def setPosition(self, p):
        self.position = p