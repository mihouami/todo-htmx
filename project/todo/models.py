from django.db import models
from users.models import User

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
