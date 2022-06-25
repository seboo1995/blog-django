from django.contrib import admin
from .models import Blog,Comment,Like

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content','timestamp','is_edited','is_published','user_id')
    model = Blog
    list_filter = ('timestamp','is_edited','is_published')


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment','user_id','timestamp','blog_id']
    model = Comment
    list_filter = ['blog_id','user_id','timestamp']


class LikeAdmin(admin.ModelAdmin):
    list_display = ['user_id','blog_id','timestamp']
    model = Like
    list_filter = ['user_id','blog_id','timestamp']









admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)