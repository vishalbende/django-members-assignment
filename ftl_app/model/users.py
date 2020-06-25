from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid

# main user model
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=256, blank=True, null=True)
    username = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    tz = models.CharField(max_length=256)
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'users'

    def real_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()



