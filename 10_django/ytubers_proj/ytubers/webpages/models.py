from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    button_text = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='slider/%Y/%m')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title