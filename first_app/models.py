from django.db import models

# Create your models here.
# DOCUMENTATION: https://docs.djangoproject.com/en/5.0/topics/db/models/

class Musician(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    release_date = models.DateField()

    rating = (
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "OK"),
        (4, "Good"),
        (5, "Excellent"),
    )
    num_stars = models.IntegerField(choices=rating) 

    def __str__(self):
        return self.name + " by " + str(self.artist) + "(" + str(self.release_date) + ")"


