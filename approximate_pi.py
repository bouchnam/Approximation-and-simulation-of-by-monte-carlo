"""
on va generer une simulation de 10 images
represantant des valeurs approximatives de π"""

import sys
import time
from random import uniform
from subprocess import call
import tracer_nombres
import simulator

def generate_ppm_file(taille, nbr_de_points, numimg, apres_virgule):
    """ renvoie une image selon les parametres donnees """
    liste = [['255 255 255\n' for i in range(taille)] for j in range(taille)]
    for _ in range(nbr_de_points):
        i = int(uniform(0, taille-1))
        j = int(uniform(0, taille-1))
        if ((taille/2-i)**2 + (taille/2-j)**2)**0.5 <= taille/2:
            liste[i][j] = '0 0 255\n'
        else:
            liste[i][j] = '255 0 0\n'
    nombre = str(simulator.simulator_pi(nbr_de_points))[:2 + apres_virgule]
    compteur = 1
    for elt in nombre[:2 + apres_virgule]:
        tracer_nombres.tracer(liste, taille, elt, compteur)
        compteur += 1
    nom_image = f'img{numimg}_3-{nombre[2:]}.ppm'
    fichier = open(nom_image, 'w')
    fichier.write('P3\n')
    fichier.write(f'{taille} {taille}\n')
    fichier.write('255\n')
    for k in range(taille):
        fichier.writelines(liste[k])
    fichier.close()
    return nom_image

def draw():
    """ generation des 10 images,puis generation
    de l'image animée GIF
    """
    nouvelle_liste = []
    for i in range(10):
        nom = generate_ppm_file(N, int((i+1)*P/10), i, M)
        nouvelle_liste.append(nom)
    call(['convert', '-delay', '100']+nouvelle_liste+['my_projett.gif'])


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise IndexError('tu dois saisir 3 arguments')
    N = sys.argv[1]
    """ N est la taille de l'image"""
    P = sys.argv[2]
    """ nbr est le nombre de points a generer"""
    M = sys.argv[3]
    """ M est le nombre de nombres apres la virgule"""
    if N.isdigit() is False or int(N) <= 0:
        raise ValueError("N doit etre un nombre positif")
    if P.isdigit() is False or int(P) <= 0:
        raise ValueError("n doit etre un nombre positif")
    if int(P) < 10:
        raise ZeroDivisionError('un 0 au denominateur!!, on a n/10 dans generate_ppm_file!!!')
    if M.isdigit() is False or int(M) <= 0:
        raise ValueError("m doit etre un nombre positif")
    if int(M) > 9:
        raise ValueError("m doit etre inferieur a 9")
    N = int(N)
    P = int(P)
    M = int(M)
    T1 = time.time()
    draw()
    T2 = time.time()
    print(T2-T1)
