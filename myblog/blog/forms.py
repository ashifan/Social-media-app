from django import forms
from django.contrib.auth.models import User
from blog.models import Post




class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","text","image",]




#class CommentForm(forms.ModelForm):
 #   class Meta:
  #      model=Comment
   #     fields=["text", "post", "user", "comment"]


#class LikeForm(forms.ModelForm):
 #   class Meta:
  #      model=Like
   #     fields=["user", "post"]
        





        
