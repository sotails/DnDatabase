from django.db import models

# Create your models here.

class item(models.Model):
	item_type = models.TextField()
	item_name = models.TextField()
	item_description = models.TextField()

	def __str__(self):
		return self.item_type+" "+self.item_name +" "+ self.item_description
  