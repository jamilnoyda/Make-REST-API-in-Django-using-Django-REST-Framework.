## Python School

# REST-API-in-Django-using-Django-REST-Framework.
REST API in Django using Django REST Framework.


[![Python Version](https://img.shields.io/badge/python-2.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-1.11-brightgreen.svg)](https://djangoproject.com)


This is an example project to illustrate an implementation of REST API in Django using Django REST Framework with multiple user types. In this Django app, teachers can upload marksheet of student and send him  and students can sign up and can see his marksheet

# Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/sibtc/django-multiple-user-types-example.git
```

API Root:
http://127.0.0.1:8000/api/



Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/django-multiple-user-types-example/blob/master/LICENSE).
