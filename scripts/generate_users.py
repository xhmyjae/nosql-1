from faker import Faker
import json
from datetime import datetime

# Initialisation de Faker
fake = Faker()


# Fonction pour générer un utilisateur aléatoire
def generate_user():
    name = fake.name()
    age = fake.random_int(min=18, max=80)
    email = fake.email()
    created_at = fake.date_time_this_decade().isoformat()
    return {
        "name": name,
        "age": age,
        "email": email,
        "createdAt": created_at
    }


# Génération de 100 utilisateurs aléatoires
users = [generate_user() for _ in range(100)]

# Écriture des données dans un fichier JSON
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("Données générées avec succès !")
