import os
import time
from datetime import datetime
from random import choice
from sys import platform

from pypresence import Presence
from tqdm import tqdm

from config import *


def clear_console():
    if platform == "linux" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

while True:
    try:
        # Choisir un élément à afficher
        name = choice(names)

        # Récupérer ses informations
        client_id = ids[name]
        st = states[name]
        bu = buttons[name]
        lt = choice(quotes)

        # Se connecter au serveur RPC Discord
        RPC = Presence(client_id)
        RPC.connect()

        # Choisir entre le logo jour et le logo nuit
        if datetime.now().hour >= 19 or datetime.now().hour <= 7:
            li = large_image_night[name]
        else:
            li = large_image[name]

        # Envoyer les informations au RPC Discord
        RPC.update(state=st,
                   buttons=bu,
                   large_image=li,
                   large_text=lt)

        # Afficher une interface basique
        clear_console()
        print("En cours d'affichage: " + str(name))
        print("Citation: " + str(lt))
        print("")
        print("Prochain changement :")

        # Attendre 60 secondes avec un barre de chargement
        for i in tqdm(range(300)):
            time.sleep(0.2)

        # Fermer la connection actuelle
        RPC.close()

    except KeyboardInterrupt:
        print("Fermeture de la connection RPC...")
        RPC.close()
        exit()