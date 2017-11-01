from django.db import models

# Create your models here.

class item(models.Model):
	item_type = models.TextField()
	item_name = models.TextField()
	item_description = models.TextField()
  