from django.db import models

class UserChoices(models.TextChoices):
    OWNER='owner'
    STAFF='staff'

class DegreeOwner(models.TextChoices):
    first='Birinchi o\'rin boasr'
    second='Ikkinchi o\rin boasr'