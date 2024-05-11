from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwarg):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email).lower(),**kwarg)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None, **kwarg):
        user = self.create_user(email, password=password, **kwarg)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user



class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    