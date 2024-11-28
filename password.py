import hashlib
import json
import os

user = (input("entre votre nom d'utilisateur : "))

while True:

        mdp = input("Veuillez saisir un mot de passe en respectant les différentes conditions : ")
        
        j = True

        if len(mdp) < 8:
            print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
            j = False

        if not any(97 <= ord(char) <= 122 for char in mdp):
            print("Erreur : le mot de passe doit contenir au moins une lettre minuscule.")
            j = False 

        if not any(65 <= ord(char) <= 90 for char in mdp):
            print("Erreur : le mot de passe doit contenir au moins une lettre majuscule.")
            j = False

        if not any(48 <= ord(char) <= 57 for char in mdp):
            print("Erreur : le mot de passe doit contenir au moins un chiffre.")
            j = False

        if not any((35 <= ord(char) <= 38) or (ord(char) == 64) or (ord(char) == 42) or (ord(char) == 94) for char in mdp):
            print("Erreur : le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
            # 33 = !   ,  64 = @ , # = 35 , $ = 36 , % = 37 , ^ = 94 , & = 38  * = 42 
            j = False

        if j:
            print("Mot de passe valide.")

        #hachage mot de passe
            mdp_hache = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

        #lecture / init des donnees
            if os.path.exists("password.json") and os.path.getsize("password.json") > 0:
                    with open("password.json", "r") as f:
                     data = json.load(f)
            else:
            #si le fichier est vide ou inexistant
                    data = []

            if any(entry["hashed_password"] == mdp_hache for entry in data):
                 print("Code incorrect : ce mot de passe est déjà présent dans le fichier JSON.")
                 continue
            else:
                    data.append({"user": user, "hashed_password": mdp_hache})

            with open("password.json", "w") as f:
                    json.dump(data, f, indent=2)

            print("Votre mot de passe haché a été enregistré.")
            break
