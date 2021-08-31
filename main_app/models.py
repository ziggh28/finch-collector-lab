from django.db import models

# Create your models here.
class finch(models.Model):
  name = models.CharField(max_length=10)
  color = models.CharField(max_length=10)
  avis = models.IntegerField()
  
  def __str__(self):
    return self.name