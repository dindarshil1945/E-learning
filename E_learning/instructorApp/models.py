from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    options=(
        ("student","student"),
        ("instructor","instructor"),
    )
    role=models.CharField(max_length=100,choices=options,default="student")
