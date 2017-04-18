from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    image=models.FileField(null=True,blank=True)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True,blank=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()



    def __str__(self):
        return self.title


    class Meta:
        db_table = "post"


#class Comment(models.Model):
 #   text = models.TextField()
  #  post = models.ForeignKey('blog.Post', null=True)
   # user = models.ForeignKey(User)
    #recomment = models.ForeignKey('self',null=True)

    #class Meta:    
     #   db_table = "comment"





