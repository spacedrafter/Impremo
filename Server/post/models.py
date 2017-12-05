from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta():
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['create']

    user = models.ForeignKey(User, verbose_name="User")
    text = models.TextField('Text', max_length=1000)
    image = models.ImageField('Image', upload_to='post/')
    create = models.DateTimeField('Create', auto_now_add=True)
    update = models.DateTimeField('Update', auto_now=True)
    moder = models.BooleanField('Moder', default=False)

    def __str__(self):
        return self.text


class Comment(models.Model):
    class Meta():
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['create']

    user = models.ForeignKey(User, verbose_name="User")
    post = models.ForeignKey(Post, verbose_name="Post")
    text = models.TextField("Comment's text")
    create = models.DateTimeField('Create', auto_now_add=True)
    moder = models.BooleanField('Moder', default=False)

