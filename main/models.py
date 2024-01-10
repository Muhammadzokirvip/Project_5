from django.db import models

class Food (models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

class Reservation (models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.full_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title 

class Sign(models.Model):
    email = models.EmailField()  