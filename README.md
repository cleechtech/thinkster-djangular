# thinkster-django-angular-boilerplate

## Installation

*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) and
[Node.js](http://nodejs.org/).*

* Fork this repository.
* `$ git clone git@github.com:<your username>/thinkster-django-angular-boilerplate.git`
* `$ mkvirtualenv thinkster-djangular`
* `$ cd thinkster-django-angular-boilerplate/`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

[full tutorial](https://thinkster.io/django-angularjs-tutorial/)

Make sure account serializer is working
```
>>> from authentication.models import Account
>>> from authentication.serializers import AccountSerializer
>>> account = Account.objects.latest('created_at')
>>> serialized_account = AccountSerializer(account)
>>> serialized_account.data.get('email')
>>> serialized_account.data.get('username')
```


