from django.db import models

class UserChoices(models.TextChoices):
    OWNER='owner'
    STAFF='staff'