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

        if not any((35 <= ord(char) <= 38) or (ord(char) == 64) or (ord(char) == 42) or (ord(char) == 94) for char in mdp):
            print("Erreur : le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
            # 33 = !   ,  64 = @ , # = 35 , $ = 36 , % = 37 , ^ = 94 , & = 38  * = 42 
            j = False

        if  user == mdp:
            j = False
            print("Le nom d'utilisateur ne peut pas être identique à votre mot de passe !")

        if j == True:
            print("Code valide")

            mdp_bytes = mdp.encode('utf-8')

            hash_object = hashlib.sha256(mdp_bytes)

            mdp_hache = hash_object.hexdigest()

 
            print("Votre mot de passe haché est : ", mdp_hache)
            break