# -*- coding: utf-8 -*-


def pizza():
    print("Pizzaaaaaaa")


def nuggets():
    print("Course de poussins!")


def quiche():
    print("Qui?")


def croques():
    print("Ma machine est partie...")


def courgettes():
    print("Non, pas de courgettes :'(")


def choix_repas_moche(num_choix=4):
    """
    Choix d'un repas en utilisant les if/else
    """
    if num_choix == 1:
        pizza()
    if num_choix == 2:
        nuggets()
    if num_choix == 3:
        quiche()
    if num_choix == 4:
        courgettes()


def choix_repas(num_choix=4):
    """
    Choix d'un repas en utilisant les dictionnaires
    """
    choix = {1: pizza, 2: nuggets, 3: quiche, 4: courgettes}
    return choix.get(num_choix, 4)()


if __name__ == '__main__':
    choix_repas(1)
    choix_repas(2)
    choix_repas(3)
    choix_repas(4)
    choix_repas()
