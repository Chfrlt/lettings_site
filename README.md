## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Créer l'environnement virtuel

- `cd /path/to/lettings_site`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/lettings_site`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/lettings_site`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/lettings_site`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/lettings_site`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Docker

### Construire une image Docker image pour lancer l'application localement

- Téléchargez et installez [Docker](https://docs.docker.com/get-docker/)
- `cd /path/to/lettings_site`
- Créer l'image via la commande `docker build -t <image-name> .`
- Utilisez la commande `docker run --rm -p 8080:8080 --env-file .env <image-name>`

Vous pouvez ensuite accéder à l'application dans un navigateur via l'adresse http://127.0.0.1:8080/

## Deploiment

Afin d'effectuer le déploiement et de mettre en place l'intégration continue de l'application, il est nécessaire de posséder un compte sur l'ensemble de ces applications:
> - [GitHub](https://github.com/)
> - [CircleCI](https://circleci.com)
> - [Docker](https://www.docker.com)
> - [Heroku](https://www.heroku.com)
> - [Sentry](https://sentry.io/welcome/)

Le déploiement de l'application est automatisé par un pipeline CircleCI.

- Créer une application Heroku par la méthode de votre choix
> Le nom de l'application doit être identique à celui mentionné dans le fichier cofig.yml
- Initialiser un projet sur [CircleCI](https://circleci.com)
- Il est ensuite nécessaire de configurer les variables d'environnements sur CircleCI.

Variables d'environnements requises:

| Tables   |      Are      |
|----------|:-------------:|
| DOCKER_USERNAME | Nom d'utilisateur Docker |
| DOCKER_PASSWORD | Mot de passe Docker |
| DOCKER_REPOSITORY | Nom du repository sur DockerHub |
| HEROKU_API_TOKEN | Token Heroku |
| SECRET_KEY | Clé secrète Django |
| SENTRY_DSN | URL du projet Sentry |


Par la suite, un push sur la branche master du dépot GitHub enclenche l'exécution des tests et du linting du code.

**Si les test et le linting s'exécutent sans erreurs:**

- Création d'une image Docker et dépôt sur DockerHub
- Si l'étape précédente s'exécute sans erreur:
  * Déploiement de l'application sur Heroku


### Sentry

- Installer [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Utilisez la commande `heroku addons:create sentry --app <>`
- Vous pouvez accéder à la page Sentry via `heroku addons:open sentry`
