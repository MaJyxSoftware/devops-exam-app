# Test App

Voici une application **Django** pour tester vos compétences sur Docker.

Essayez d'utiliser la fonctionnalité disponible de Docker afin de pouvoir lancer l'application en une seule commande (app, db, ...).

Et cela, de la façon la plus sécurisé possible!

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Des variables d'environement sont à utiliser pour configurer correctement l'application.

| Variable       | Valeur                              | Description                                                            |
| -------------- | ----------------------------------- | ---------------------------------------------------------------------- |
| DOMAIN         | string (defaut: `*`)                | Defini le domain autoriser                                             |
| SECRET_KEY     | string (requis)                     | Clef de sécurité pour signer et sécuriser les données sensibles        |
| DEBUG          | `true` ou `false` (defaut: `false`) | Passer l'application en mode debug                                     |
| DB_NAME        | string (requis)                     | Nom de la base de données Postgres                                     |
| DB_USER        | string (requis)                     | Utilisateur à utiliser pour se connecter à la base de données Postgres |
| DB_PASSWORD    | string (requis)                     | Mot de passe pour se connecter à la base de données Postgres           |
| DB_HOST        | string (requis)                     | Adresse de la base de données Postgres                                 |
| DB_PORT        | string (requis)                     | Port de la base de données Postgres                                    |
| REDIS_HOST     | string (requis)                     | Adresse de la base Redis                                               |
| REDIS_PORT     | string (requis)                     | Port de la base Redis                                                  |
| REDIS_PASSWORD | string (default: `None`)            | Mot de passe de la base Redis                                          |

## Prérequis

### Docker

L'application doit pouvoir accéder à l'API Docker via le fichier `.sock`.

### Initialisation de la DB

```bash
./manage.py migrate
```

## Lancement en local

```bash
./manage.py runserver 127.0.0.1:8000
```
