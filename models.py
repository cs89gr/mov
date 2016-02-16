from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


CATEGORY_CHOICES = (
    ('Animation','Animation'),
    ('Action','Action'),
    ('Adventure','Adventure'),
    ('Biography','Biography'),
    ('Crime','Crime'),
    ('Comedy','Comedy'),
    ('Drama','Drama'),
    ('Fantasy','Fantasy'),
    ('Familly','Familly'),
    ('Horror','Horror'),
    ('History','History'),
    ('Sport','Sport'),
    ('Sci-Fi','Sci-Fi'),
    ('Thriller','Thriller'),
)

RATING_CHOICES=(
    ("★","★"),
    ("★★","★★"),
    ("★★★","★★★"),
    ("★★★★","★★★★"),
    ("★★★★★","★★★★★"),
    ("★★★★★★","★★★★★★"),
    ("★★★★★★★","★★★★★★★"),
    ("★★★★★★★★","★★★★★★★★"),
    ("★★★★★★★★★","★★★★★★★★★"),
    ("★★★★★★★★★★","★★★★★★★★★★"),
)

class Category(models.Model):
    categorytitle = models.CharField(max_length=9,choices=CATEGORY_CHOICES,unique=True)
    slug= models.SlugField()

    def __str__(self):
        return self.categorytitle


    class Meta:
        ordering = ('categorytitle',)



class Movies(models.Model):
    author = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=100,blank=True)
    slug= models.SlugField()
    Desciption = models.TextField()
    video = EmbedVideoField()
    director = models.ForeignKey('Director')
    category = models.ManyToManyField(Category)
    Imdblink = models.URLField(max_length=400)
    Imdbrank = models.FloatField(null=True)
    Releasedate = models.DateField(blank=True, null=True)
    Durationmin = models.IntegerField()
    createddate = models.DateTimeField(default=timezone.now)
    publisheddate=models.DateTimeField(blank=True, null=True)
    image1 = models.ImageField(upload_to="images/moviesthumb/")
    rating = models.CharField(max_length=10,choices=RATING_CHOICES,null=True)
    like =models.IntegerField(default=0)

    def publish(self):
        self.publisheddate=timezone.now()
        self.save()

    def __str__(self):
        return self.Title



class Director(models.Model):
    Name = models.CharField(max_length=100,blank=True)
    slug= models.SlugField()
    Deteborn = models.DateField(blank=True, null=True)
    descr = models.TextField()
    image2 = models.ImageField(upload_to="images/moviesthumb/",null=True)

    def __str__(self):
        return self.Name
