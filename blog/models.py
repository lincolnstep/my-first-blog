from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics',validators=[FileExtensionValidator(['jpg','gif','png'])],blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Project(models.Model):
    ptitile = models.CharField(max_length=200)
    ptext=RichTextField()
    location = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    designation=models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.ptitile

class Aboutme(models.Model):
    atitle = models.CharField(max_length=200, default="Welcome to My Blog")
    aimage = models.ImageField(upload_to='blog_images',validators=[FileExtensionValidator(['jpg','gif','png'])],blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    atext = RichTextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.atitle

class Quote(models.Model):
    qauthor = models.CharField(max_length=200)
    qdate = models.DateField()
    qtext = RichTextField()
    published_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.save()

    def __str__(self):
        return self.qauthor
