from menu.views import dish
from django.db import models
from datetime import datetime
from menu.models import Menu

# Create your models here.
class Orders(models.Model):

    PROGRESS_CHOICES = [
        ('O','Ordered'),
        ('P','Prepearing'),
        ('C','Completed')
    ]
    dish_id = models.IntegerField()
    quantity = models.IntegerField(default=1, blank=True)
    progress = models.CharField(max_length=1, choices=PROGRESS_CHOICES,default='o', blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def name(self):
        return Menu.objects.filter(id=self.dish_id)[0]

    def __str__(self):
        name = Menu.objects.filter(id=self.dish_id)[0]
        return f"{self.id}. {name.name} {self.progress}"