from django.db import models

# Create your models here.

class Winner(models.Model):
	name = models.TextField(default='')
	