from django.contrib import admin

# Register your models here.
from blog.models import Post



class PostAdmin(admin.ModelAdmin):
    fields = ['title','text','image','user','created_date','published_date']
    list_display = ['title','user','text','image','created_date','published_date']

admin.site.register(Post, PostAdmin)


#class CommentAdmin(admin.ModelAdmin):
#    fields = ['text', 'post', 'user', 'comment']
 #   list_display = ['text', 'post', 'user', 'comment']

#admin.site.register(Comment, CommentAdmin)


#class LikeAdmin(admin.ModelAdmin):
 #   fields = ['user', 'post']
  #  list_display = ['user','post']

#admin.site.register(Like, LikeAdmin)