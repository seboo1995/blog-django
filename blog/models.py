from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table = 'blog'
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'comment'


class Like(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'like'
