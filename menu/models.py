from django.db import models


# Create your models here.
class Menu(models.Model):
    
    CHINEES = 'CH'
    FRENCH = 'FR'
    INDIAN = 'IN'
    AMERICAN = 'AM'
    ITALIAN = 'IT'
    CONTENENTAL = 'CO'
    MEXICAN = 'ME'
    
    COISINE_CHOICES = [
        (CHINEES, 'Chinees'),
        (FRENCH, 'French'),
        (INDIAN, 'Indian'),
        (AMERICAN, 'American'),
        (ITALIAN, 'Italian'),
        (CONTENENTAL, 'Contenental'),
        (MEXICAN, 'Mexican')
    ]

    name = models.CharField(max_length=300)
    cost = models.IntegerField(blank=False)
    description = models.CharField(max_length=300, blank=True)
    cuisine = models.CharField(
        max_length=2,
        choices= COISINE_CHOICES,
        default=ITALIAN
    )
    image = models.ImageField(upload_to="media/%Y/%m", blank=False)

    def __str__(self):
        return f'{self.name} -/{self.cost}'
