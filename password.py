import hashlib

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

        if not any(35 <= ord(char) <= 38 or 64 == ord(char) or 42 or 94 for char in mdp):
            print("Erreur : le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
            j = False

        if j == True:
            print("Code valide")

        # Hachage du mot de passe avec SHA-256
        # Convertir le mot de passe en bytes
            mdp_bytes = mdp.encode('utf-8')

        # Créer un objet SHA-256
            hash_object = hashlib.sha256(mdp_bytes)

        # Obtenir le hash sous forme de chaîne hexadécimale
            mdp_hache = hash_object.hexdigest()

        # Affichage du mot de passe haché
            print("Votre mot de passe haché est : ", mdp_hache)
            break

# 33 = !   ,  64 = @ , # = 35 , $ = 36 , % = 37 , ^ = 94 , & = 38  * = 42 