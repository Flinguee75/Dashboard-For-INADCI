from werkzeug.security import check_password_hash

# Hash stocké dans la base de données
stored_hash = "scrypt:32768:8:1$KM1040rJGrzipB0c$2525bb4c1eaea69ee3db5e726b08c66f4fe643da17ad66ee5ea56db040b22846fe627a1c6a8ccbc99543b96e3bdee702d23a1510fdae005bf24ade6ba01c3735"

# Mot de passe fourni par l'utilisateur
password = "secure_password123"

# Vérifier le mot de passe
if check_password_hash(stored_hash, password):
    print("Mot de passe correct")
else:
    print("Mot de passe incorrect")
