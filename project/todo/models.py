from django.db import models
from users.models import User

# Create your models here.
class Todo(models.Model):
    class ImportanceChoices(models.TextChoices):
        VERY_IMPORTANT = 'V'
        IMPORTANT = 'I'
        NOT_IMPORTANT = 'N'


    description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    importance = models.CharField(null=True, max_length=1, choices=ImportanceChoices.choices)

    def __str__(self):
        return self.description
