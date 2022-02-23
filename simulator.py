#!/usr/bin/env python3
"""
Module permettant de donner une valeur approximative
de π en utilisant la methode de Monte Carlo
"""

from random import uniform
from collections import namedtuple

Point = namedtuple("Point", 'x y')

def simulator_pi(nbr_de_points):
    """ simulation de pi"""
    compteur = 0
    for _ in range(0, nbr_de_points):
        Point.x = uniform(-1, 1)
        Point.y = uniform(-1, 1)
        rayon = (Point.x**2+Point.y**2)
        if rayon <= 1:
            compteur += 1
    return 4 * compteur / nbr_de_points
