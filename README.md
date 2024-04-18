# NoSQL - TP 1

## TOMATIS Margot

### Comment démarrer le Replica Set avec Docker.

docker network create mongo_network 
docker-compose up -d
docker-compose ps
docker exec -it mongo1 mongosh
db.createCollection("test")
docker exec -it mongo2 bash
show collections

### Comment générer et insérer les fausses données.

docker exec -it mongo1 bash   
apt-get update && apt-get install python3-pip
apt-get install python3.9
pip install faker
pip install pymongo
exit
docker cp .\scripts mongo1:usr/src
cd usr/src/scripts
python3 ./generate_users.py 

### Les commandes CLI utilisées pour les opérations CRUD et leurs résultats.

mongoimport --db db_cli --collection users --file users.json --jsonArray
mongosh
use db_cli
#### insert new user
db.users.insertOne({
        "name": "Larry Goodman",
        "age": 34,
        "email": "timothy73@example.com",
        "createdAt": "2022-03-19T18:53:32.367455"
    })
#### read les users de plus de 30 ans
db.users.find({age: {$gt: 30}})
#### update ajouter 5 ans à l'age de tous les users
db.users.updateMany({}, {$inc: {age: 5}})
#### delete un user specifique
db.users.deleteOne({name: "Larry Goodman"})

### Une section sur l'exécution de votre script, les différences observées entre les opérations CRUD en CLI et via le script.

#### retourner dans le bash de mongo1 dans /usr/src/scripts
copier le nouveau fichier crud_automatisation.py dans le container mongo1
exit
docker cp .\scripts\crud_automatisation.py mongo1:usr/src/scripts
docker exec -it mongo1 bash
python3 /usr/src/scripts/crud_automatisation.py

### Toute difficulté rencontrée et comment vous l'avez surmontée.
Beaucoup de difficultes avec le docker-compose, j'ai du revoir la configuration du fichier yaml et les commandes pour le lancer (creation d'un autre container pour la gestion du rs).
