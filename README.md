# NoSQL - TP 1- TOMATIS Margot

## Comment démarrer le Replica Set avec Docker.

On commence par créer un réseau pour les containers mongo.
```bash
docker network create mongo_network
```
On utilise ensuite le docker-compose.yml pour lancer les containers mongo1, mongo2 et mongo3.
```bash
docker-compose up -d
```
On vérifie que les containers sont bien lancés.
```bash
docker-compose ps
```
On se connecte au container mongo1 pour initialiser le Replica Set.
```bash
docker exec -it mongo1 mongosh
```
On teste la connexion au Replica Set en créant une collection test et voir si elle est bien répliquée sur les 3 containers.
```bash
db.createCollection("test")
exit
docker exec -it mongo2 bash
show collections
exit
docker exec -it mongo3 bash
show collections
exit
```

## Comment générer et insérer les fausses données.

On commence par se connecter au container mongo1 pour installer les packages nécessaires.
```bash
docker exec -it mongo1 bash   
apt-get update && apt-get install python3-pip
apt-get install python3.9
pip install faker
pip install pymongo
exit
```
On copie le script generate_users.py dans le container mongo1.
```bash
docker cp .\scripts mongo1:usr/src
```
On se connecte au container mongo1 pour générer les fausses données.
```bash
cd usr/src/scripts
python3 ./generate_users.py
``` 

## Les commandes CLI utilisées pour les opérations CRUD et leurs résultats.

On importe les données générées dans la collection users de la base de données db_cli.
```bash
mongoimport --db db_cli --collection users --file users.json --jsonArray
```
On sélectionne la base de données db_cli.
```bash
mongosh
use db_cli
```

### Insert - ajouter un new user

Pour insérer un nouvel utilisateur, on utilise la commande insertOne.
```bash
db.users.insertOne({
        "name": "Larry Goodman",
        "age": 34,
        "email": "timothy73@example.com",
        "createdAt": "2022-03-19T18:53:32.367455"
    })
```

### Read - cherche les users de plus de 30 ans

Pour chercher les utilisateurs de plus de 30 ans, on utilise la commande find.
```bash
db.users.find({age: {$gt: 30}})
```

### Update - ajouter 5 ans à l'age de tous les users

Pour ajouter 5 ans à l'âge de tous les utilisateurs, on utilise la commande updateMany.
```bash
db.users.updateMany({}, {$inc: {age: 5}})
```

### Delete - un user spécifique

Pour supprimer un utilisateur spécifique, on utilise la commande deleteOne.
```bash
db.users.deleteOne({name: "Larry Goodman"})
```

## Une section sur l'exécution de votre script.

On retourne dans le bash de mongo1 pour copier le script crud_automatisation.py.
```bash
docker cp .\scripts\crud_automatisation.py mongo1:usr/src/scripts
```
On se connecte au container mongo1 pour exécuter le script.
```bash
docker exec -it mongo1 bash
python3 /usr/src/scripts/crud_automatisation.py
```

## Les différences observées entre les opérations CRUD en CLI et via le script.
Les commandes CRUD en CLI sont plus simples et plus rapides à exécuter, mais elles sont moins flexibles que les scripts. Les scripts permettent de faire des opérations plus complexes et de les automatiser.

## Toute difficulté rencontrée et comment vous l'avez surmontée.
Beaucoup de difficultes avec le docker-compose, j'ai du revoir la configuration du docker-compose.yml et les commandes pour le lancer (creation d'un autre container pour la gestion du rs, impossible en tapant directement la commande d'installation du rs dans le container mongo1).

J'ai aussi eu des difficultés avec la commande mongoimport, j'ai du ajouter le paramètre --jsonArray pour que les données soient bien importées.