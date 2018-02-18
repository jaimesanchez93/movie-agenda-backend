from django.db import models

# Create your models here.

CATEGORIES = (
     ('FAN','Fantastic'),
     ('SCF','Sciencie-Fiction',),
     ('THR','Thriller'),
     ('DRA','Drama'),
     ('ACT','Action'),
     ( 'COM','Comedy'),
     ( 'KID','Kids'),
     ( 'MIS', 'Mistery'),
     ('TER','Terror'),
     ('UNC','Uncategoried')
)

class Movie(models.Model):

    name = models.CharField(max_length=150)
    category=models.CharField(max_length=3,choices=CATEGORIES,blank=True,default='UNC')
    synopsis = models.TextField(blank=True,default="")
    image =  models.ImageField(blank=True,upload_to='Photo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)
    movie_seen = models.BooleanField(default=False)
    duration = models.IntegerField(blank=True,default="")

    def __str__(self):
        return self.name