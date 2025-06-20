from django.contrib.auth.models import BaseUserManager

class MorhpyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('A user must have a username')
        if not email:
            raise ValueError('A user must have an email')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superusers must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superusers must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
