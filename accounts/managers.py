from django.contrib.auth.models import BaseUserManager
from django.db.models import QuerySet
from django.db.models import Manager
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class SoftDeleteQuerySet(QuerySet):
    def delete(self):
        self.update(is_deleted=True, deleted_at=now(), is_active=False)


class SoftDeleteManager(Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset(self.model, using=self._db).filter(is_deleted=False)