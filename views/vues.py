"""Ihm du programme d'échecs."""
import os
import sys
import logging

logging.basicConfig(filename='logs/journal.log', encoding='utf-8', level=logging.DEBUG)
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class Ihm:
    """Creation de la class view."""
    lstmenu = ["1.)  Créer un nouveau tournoi.\n",
               "2.)  Ajouter un/plusieurs joueurs.\n",
               "3.)  Générer des paires de joueurs pour le premier tour.\n",
               "4.)  Entrer les résultats  des matchs.\n",
               "5.)  Rapport des joueurs (par ordre alphabétique).\n",
               "6.)  Rapport des joueurs (par classement).\n",
               "7.)  Rapport des tournois.\n",
               "8.)  Rapport des matchs d'un tournois.\n",
               "9.) Rapport des tours d'un tournois.\n",
               "10.) Charger un tournois.\n",
               "11.) Sortir du programme\n\n"]

    @staticmethod
    def affichage_principal():
        """Affichage du menu."""
        print("=" * 32)
        print("======MENU PRINCIPAL============")
        print("================================\n")
        print("".join(Ihm.lstmenu))
        print("=" * 32)
        print("=" * 32)

    @staticmethod
    def saisie_user():
        """Secupération du choix de l'utilisateur."""
        choix = ""
        while choix == "":
            # print("".join(Ihm.lstMenu))
            Ihm.affichage_principal()
            choix = int(input('Entrer le N° du menu & valider par ENTRER:'))
        return choix


if __name__ == "__main__":
    Ihm.saisie_user()
