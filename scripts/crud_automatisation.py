from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client['votre_base_de_donnees']
users_collection = db['users']


# Fonction pour insérer les données générées dans la collection users
def insert_users_data(users_data):
    users_collection.insert_many(users_data)
    print("Données insérées avec succès !")


# Fonction pour lire et afficher tous les utilisateurs de plus de 30 ans
def find_users_over_30():
    users_over_30 = users_collection.find({"age": {"$gt": 30}})
    print("Utilisateurs de plus de 30 ans :")
    for user in users_over_30:
        print(user)


# Fonction pour mettre à jour l'âge de tous les utilisateurs en ajoutant 5 ans
def update_users_age():
    users_collection.update_many({}, {"$inc": {"age": 5}})
    print("Âge de tous les utilisateurs mis à jour avec succès !")


# Fonction pour supprimer un utilisateur spécifique par son nom
def delete_user_by_name(name):
    result = users_collection.delete_one({"name": name})
    if result.deleted_count == 1:
        print(f"L'utilisateur {name} a été supprimé avec succès !")
    else:
        print(f"L'utilisateur {name} n'a pas été trouvé.")


# Données d'exemple à insérer
example_users_data = [
    {"name": "Alice", "age": 28, "email": "alice@example.com", "createdAt": "2022-01-01T00:00:00Z"},
    {"name": "Bob", "age": 35, "email": "bob@example.com", "createdAt": "2022-01-02T00:00:00Z"},
    # Ajoutez d'autres données générées ici
]

# Insérer les données d'exemple
insert_users_data(example_users_data)

# Lire et afficher tous les utilisateurs de plus de 30 ans
find_users_over_30()

# Mettre à jour l'âge de tous les utilisateurs en ajoutant 5 ans
update_users_age()

# Supprimer un utilisateur spécifique par son nom
delete_user_by_name("Alice")

# Fermer la connexion
client.close()
