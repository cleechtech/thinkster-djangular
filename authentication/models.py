from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('Users must have a valid email address.')
		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

		# self.model refers to the model attribute of BaseUserManager
		account = self.model(
			email=self.normalize_email(email), username=kwargs.get('username')
		)
		account.set_password(password)
		account.save()
		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)
		account.is_admin = True
		account.save()
		return account

# Create Account model
class Account(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)

	# Optional name fields
	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	tagline = models.CharField(max_length=140, blank=True)

	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# When you want to get a model instance in Django, you use an expression 
	# of the form Model.objects.get(**kwargs). 
	# The objects attribute here is a Manager class whose name typically 
	# follows the <model name>Manager convention
	objects = AccountManager()

	# treat email field as the username for this model
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		# change string representation of Account objects
		return self.email

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name


