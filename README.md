# FastApi and Gaphql:
Ce projet a comme objectif d'initier à l'utilisation de graphql
avec fastapi en passant par le lirairie graphene.

## requirements:
Pour lancer le projet, il faut installer docker/docker-compose.
En suite lancer la commande suivante:
```
docker-compose up --build
```

Avant de lancer la ligne de commande précédante, il faut créer un
fichier .env en vous basant de ce qui existent dans le fichier .env.dist.

Il est possible de copier coller directement le contenu dans le .env, mais il
est aussi possible de modifier les accès.

Une fois que les containers sont lancés, il suffit d'aller sur l'url
suivant pour utiliser l'interface graphiql:
: http://localhost:8080/graphql


## Services:
On a trois services dont la premier est l'app, la deuxième est la
definition de la base de données qui est dans notre cas MONGODB.
Le dernier service est nginx qui est supplémentaire.

## Test à ajouter:
Les opérations qui existent actuellement sont les opérations de bases
comme dans un api rest (CRUD).

## TODO:
- ajout de test
- optimisation de l'api en ajoutant des gestions d'erreur.
- Voir d'autres cas d'usages et enrichir le contenu du projet
    en ajoutant des accès avec token (JWT) par exemple.
