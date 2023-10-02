from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class PlatForm(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length= 100)
    website = models.URLField(max_length=100)

    def __str__(self) :
        return  self.name

class WatchList(models.Model):# watchlist =>many things keep like as movie,song etc
    title =models.CharField(max_length=50)
    storyline = models.CharField(max_length=100) #description
    platform = models.ForeignKey(PlatForm,  on_delete=models.CASCADE,related_name= "watch_list")
    avg_rating = models.FloatField(default= 0)
    number_rating = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
    

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    desc = models.CharField(max_length=1000)
    watchlist = models.ForeignKey(WatchList,  on_delete=models.CASCADE,related_name="reviews")
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    create_date=models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        string = str(self.rating)+ " " + str(self.watchlist.title)
        return string