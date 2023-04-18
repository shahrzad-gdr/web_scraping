from django.db import models

class Movie(models.Model):

    title = models.CharField(max_length=150)
    rank  = models.DecimalField(max_digits=3, decimal_places=1)
    year  = models.IntegerField()
    director = models.CharField(max_length=50)
    link = models.URLField()
    poster = models.URLField()


    def __str__(self):
        return self.title




