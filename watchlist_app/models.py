from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,related_name="watchlist")
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Riview(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True, blank=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="riviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + ' | ' +self.watchlist.title
    
