from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)

	# Define metadata for serializer
	class Meta:
		# specify model
		model = Account

		# specify which attributes of the Account model should be serialized
		# is_superuser should not be available to the client for security reasons
		fields = ('id', 'email', 'username', 'created_at', 'updated_at',
			'first_name', 'last_name', 'tagline', 'password', 'confirm_password',)

		# these fields are self updating
		read_only_fields = ('created_at', 'updated_at',)

		# handle deserialization
		def create(self, validated_data):
			return Account.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.username = validated_data.get('username', instance.username)
			instance.tagline = validated_data.get('tagline', instance.tagline)

			instance.save()

			password = validated_data.get('password', None)
			confirm_password = validated_data.get('confirm_password', None)

			if password and confirm_password and password == confirm_password:
				instance.set_password(password)
				instance.save()

			# update session authentication hash
			update_session_auth_hash(self.context.get('request'), instance)

			return instance