from django.db import models

# Create your models here.
class Game(models.Model):

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    publisher = models.CharField(max_length=200)
    platform = models.CharField(max_length=400)

    hint = models.CharField(max_length=200)
    
    rating = models.IntegerField()
    series = models.IntegerField(null=True) #null if not in series otherwise the installment number
    genre1 = models.CharField(max_length=100)
    genre2 = models.CharField(max_length=100)
    setting = models.CharField(max_length=100)
    multiplayer = models.CharField(max_length=200)
    playtime = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.publisher}"
