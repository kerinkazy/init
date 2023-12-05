from django import forms
from .models import Blog, Area


class CreateBlog(forms.ModelForm):
   class Meta:
       model = Blog
       fields = "__all__"


class UpdateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class UpdateArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"