# Data visualisation with Django and Vue js ✌️ 🐍
Task for course data visualization

![Vue Logo](/task/src/assets/logo-vue.png "Vue Logo")
![Django Logo](/task/src/assets/logo-django.png "Django Logo")



The application is based on templates such as VueJs and Django (RestFramework). From Vue Cli `create` and Django `createproject` are kept as close as possible to their
original state, except where a different configuration is needed for better integration of the two frameworks.

It's setup to have a clear separation: use Vue, Yarn, and Webpack to handle all frontend logic and asset bundling,
and use Django and RestFramework to manage a Data Models, Web API, and serve static files.

While it's possible to add endpoints to serve django-rendered html responses, the intention is to use Django primarily for the backend, and have view rendering and routing and handled by Vue + Vue Router as a Single Page Application (SPA).

Out of the box, Django will serve the application entry point (`index.html` + bundled assets) at `/` ,
data at `/api/`, and static files at `/static/`. Django admin panel is also available at `/admin/` and can be extended as needed.

### Includes

* Django
* Django Restframework
* Django Whitenoise, CDN Ready
* Vue Cli 3
* Vue Router
* Vuex
* Gunicorn
* Configuration for Heroku Deployment


### Template Structure


| Location             |  Content                                   |
|----------------------|--------------------------------------------|
| `/task/backend`           | Django Project & Backend Config            |
| `/task/backend/api`       | Django App (`/api`)                        |
| `/task/src`               | Vue App .                                  |
| `/task/src/main.js`       | JS Application Entry Point                 |
| `/task/public/index.html` | Html Application Entry Point (`/`)         |
| `/task/public/static`     | Static Assets                              |
| `/task/dist/`             | Bundled Assets Output (generated at `yarn build` |
|`Untitled.ipynb`			| Task 4 with visualisation NetCdf			|
## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv

Also you need Netcdf4 framework, boostrap

## Setup Template

```
$ git clone current repo
$ cd task
```

Setup
```
$ yarn install
$ pipenv install --dev & pipenv shell
$ python manage.py migrate
```

## Running Development Servers

```
$ python manage.py runserver
```

From another tab in the same directory:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Django Api
and static files will be served from `localhost:8000`.

The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.
Proxy config in `vue.config.js` is used to route the requests
back to django's Api on port 8000.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python manage.py runserver
```
