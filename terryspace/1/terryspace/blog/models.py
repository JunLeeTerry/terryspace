from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(blank=True)
    def __str__(self):
        return self.name

class Classification(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=30)
    subtitle=models.CharField(max_length=50,blank=True)
    author=models.ForeignKey('Author')
    publish_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    classification=models.ForeignKey('Classification')
    content=models.TextField()
