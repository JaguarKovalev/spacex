from django.db import models
from django.contrib.auth.models import User

class Launch(models.Model):
    mission_name = models.CharField(max_length=255)  # Название миссии
    date = models.DateTimeField()  # Дата запуска
    success = models.BooleanField(null=True)  # Успешность запуска
    rocket = models.CharField(max_length=255)  # Название ракеты

    def __str__(self):
        return self.mission_name


class UserSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь
    search_date = models.DateTimeField(auto_now_add=True)  # Дата поиска
    year = models.IntegerField()  # Год, по которому выполнен поиск

    def __str__(self):
        return f"{self.user.username} - {self.year}"
