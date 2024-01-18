from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {
    "blank": True,
    "null": True,
}


class User(AbstractUser):
    """Модель для пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
