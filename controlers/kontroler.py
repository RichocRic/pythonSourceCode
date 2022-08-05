"""Controleur du programme d'échecs."""
import logging
import os
import sys
from subprocess import call
from models.models import Joueur, Tournoi, Tour, Match
from views.vues import Ihm
sys.path.append("/Users/hhmbp/Documents/OC/P4/p4C/models")
sys.path.append("/Users/hhmbp/Documents/OC/P4/p4C/views")
jrap = Joueur()
trs = Tour()
trns = Tournoi()
mtchs = Match()
logging.basicConfig(filename='logs/journal.log', encoding='utf-8', level=logging.DEBUG)


class Maincontroller:
    """Creation de la classe controler."""

    def __init__(self):
        """Constructeur."""
        # self.ctrl = None

    @staticmethod
    def demarrer():
        """Lancement du menu/menu launcher."""
        ctrl = Controleurmenu('n')
        ctrl.gestionchoix()


class Controleurjoueurs:
    """Controleur du menu joueur."""
    def __init__(self, nom):
        """Constructeur."""
        self.nom = nom

    @staticmethod
    def creation_joueurs():
        """Création dynamique de 8 joueurs comme demandé."""
        joueur = []
        nbrjoueur = int(input('Sasir, le Nombre de joueur(s) à inserrer '))
        for i in range(nbrjoueur):
            print('=========================')
            print('Instance Joueur N°:', [i])
            print('=========================\n')
            joueur.append(Joueur())
            joueur[i] = Joueur()
            joueur[i].creation_joueur()
            joueur[i].inserer_bdd('joueurs')


class Controleurrappport:
    """Controleur de Gestion des rapports."""
    def __init__(self, nom):
        """constructeur."""
        self.nom = nom


class Controlermenugestion:
    """Manage displaying and lifecycle."""

    @staticmethod
    def afficher_msg(msg):
        """Personnaliser les msg."""
        print(msg)

    @staticmethod
    def effacer_ecran():
        """Détection des O.S."""
        _ = call('clear' if os.name == 'posix' else 'cls')
        Controlermenugestion.effacer_ecran()

    @staticmethod
    def sortir():
        """Sortie du menu."""
        sys.exit()


class Controlertournoi:
    """Classe tournois controleur."""
    ctrl3 = Controleurjoueurs('T3')

    def __init__(self, nom):
        """Constructeur."""
        self.nom = nom


class Controleurmenu:
    """Initialisation du controleur du menu général."""

    def __init__(self, nom):
        """Constructeur."""
        self.nom = nom
    # @staticmethod
    def gestionchoix(self):
        """Exécution des méthodes en fonction du choix du menu."""

        validationchoix = Ihm.saisie_user()  # views.View.saisie_user()

        if validationchoix == 1:
            print()
            print('========vous avez choisi le tournois========\n')
            trns.creation_tournoi()
            trns.inserer_bdd('tournois')
            self.gestionchoix()

        elif validationchoix == 2:
            print()
            print('\n========vous avez choisi ajouter huit joueurs========\n')
            jrap.creation_joueurs()
            self.gestionchoix()
        elif validationchoix == 3:
            print()
            print('========vous avez choisi la génération de paire de joueur========\n')
            trns.debuter()
            self.gestionchoix()
        elif validationchoix == 4:
            print()
            print('========vous avez choisi de rentrer les résultats========\n')

        elif validationchoix == 5:
            print()
            print('========vous avez choisi le Rapport des joueurs========\n')
            jrap.rapportjoueurs()
            self.gestionchoix()
        elif validationchoix == 6:
            print()
            print('========vous avez choisi le rapport des joueurs par score========\n')
            print(jrap.triejoueur('s'))
            self.gestionchoix()
        elif validationchoix == 7:
            print("\n========vous avez choisi Rapport des tournois========\n")
            trns.rapporttournois()
            self.gestionchoix()
        elif validationchoix == 8:
            print()
            print("========vous avez choisi Rapport des matchs d'un tournois========\n")
            mtchs.rapportmatchs()
            self.gestionchoix()
        elif validationchoix == 9:
            print()
            print("Vous avez choisi le Rapport des tours d'un tournois")
            trs.rapporttours()
            self.gestionchoix()
        elif validationchoix == 10:
            print()
            print('Vous avez choisi de Charger un tournois')
            trns.loadertournois()
            self.gestionchoix()
        elif validationchoix == 11:
            print()
            print('Vous avez choisi de Quitter le programme')
            ctrlg = Controlermenugestion()
            ctrlg.sortir()

        else:
            print('choix invalides')


if __name__ == "__main__":
    menu = Maincontroller()
    menu.demarrer()
