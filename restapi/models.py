from django.db import models
from documentsite.models import Document, User


# Create your models here.


class UserDocument(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Document = models.ForeignKey(Document, on_delete=models.CASCADE)
    page = models.IntegerField(default=0)
