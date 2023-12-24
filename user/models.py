from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SALES = "SALES", "Savdo"
        MATERIALS = "MATERIAL", "Material"
        PRODUCT = "PRODUCT", "Mahsulot"

    base_role = Role.ADMIN

    role = models.CharField(max_length=32, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
