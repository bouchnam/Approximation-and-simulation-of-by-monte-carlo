#!/usr/bin/env python3
"""
Module permettant de tracer les nombres de 0 a 10
avec les pixels """

def tracer_horizontale(liste, taille, position1, position2):
    """
    tracer une ligne horizontale
    """
    for _ in range(taille):
        for j in range(taille):
            liste[position1][j+position2] = '0 0 0\n'

def tracer_verticale(liste, taille, position1, position2):
    """
    tracer une ligne horizontale
    """
    for i in range(taille):
        for _ in range(taille):
            liste[position1+i][position2] = '0 0 0\n'

def tracer(liste, taille, nombre, pos):
    """ la fonction permettants de tracer tous les nombres
    dans la position adaptee"""
    seg_court = int(3/50*taille)
    seg_long = int(6/50*taille)
    longeur = int(2*taille/9+pos*5*taille/70)
    longeur2 = int(3*taille/9+5*taille/81+5*taille/70)
    if nombre == '5':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_court, longeur2, longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '1':
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur)
    if nombre == '2':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_court, int(3*taille/9+5*taille/70), longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_court, longeur2, longeur)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '6':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_court, longeur2, longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '3':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_court, longeur2, longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '9':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_court, int(3*taille/9+5*taille/70), longeur+seg_court)
        tracer_verticale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_court, longeur2, longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '0':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '4':
        tracer_verticale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur+seg_court)
    if nombre == '8':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+seg_court, longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur+seg_court)
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70)+2*seg_court, longeur)
    if nombre == '7':
        tracer_horizontale(liste, seg_court, int(3*taille/9+5*taille/70), longeur)
        tracer_verticale(liste, seg_long, int(3*taille/9+5*taille/70), longeur+seg_court)
    if nombre == '.':
        tracer_point(liste, taille)

def tracer_point(liste, taille):
    """ tracer le point represantant la virgule dans la simulation"""
    for i in range(6):
        for j in range(6):
            liste[i+int(258*taille/500)][j+int(178*taille/500)] = '0 0 0\n'
