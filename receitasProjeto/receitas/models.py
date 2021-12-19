from django.db import models
from datetime import datetime
from pessoas.models import Person


# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    preparation_method = models.TextField()
    preparation_time = models.IntegerField()
    yields_volume = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    insert_date = models.DateTimeField(default=datetime.now, blank=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
