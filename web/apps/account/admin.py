from django.contrib import admin
from django.contrib.auth.models import BaseUserManager

class PassportManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = PassporManager
        )

