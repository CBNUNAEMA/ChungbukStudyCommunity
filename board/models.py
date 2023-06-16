from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from accounts.models import *

class like(models.Model):
    username = models.CharField(max_length=150)
    likeIt = models.IntegerField(default=0)

class evalLect(models.Model):
    lectName = models.CharField(max_length= 150)
    professor = models.CharField(max_length = 150)
    content = models.TextField()
    rating = models.IntegerField(default= 1)
    author = models.CharField(max_length = 150, default='')

    def __str__(self):
        return f"{self.lectName}, {self.professor}"

class Comment(models.Model):
    content = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=150)
    likes = models.ManyToManyField(like)

class Post(models.Model):
    tag = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    content = models.TextField()
    pubDate = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=15)
    lectName = models.CharField(max_length=20)
    comments = models.ManyToManyField(Comment)
    likes = models.ManyToManyField(like)
    files = models.FileField(upload_to='post_files', blank=True, null=True)
    images = models.ImageField(upload_to='post_images', blank=True, null=True)
    font = models.CharField(max_length=50, blank=True)
    fontSize = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.pk}. {self.title} - {self.author} ({self.pubDate})"
    # 글 번호, 제목, 작성자, 작성시간 표시
    def likeCount(self):
        return self.likes.count()
