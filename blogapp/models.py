from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class NewPost(models.Model):
    title = models.CharField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    publication_time = models.DateTimeField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to = "images/")
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
class profilepage(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)  
        website = models.CharField(max_length=100, null=True, blank=True)
        instagram = models.CharField(max_length=100, null=True, blank=True)
        facebook = models.CharField(max_length=100, null=True, blank=True)
        twitter = models.CharField(max_length=100, null=True, blank=True)
        profile_image = models.ImageField(null=True, blank=True, upload_to="images/profile/")
        contact = models.CharField(max_length=100, null=True, blank=True)
        bio = models.CharField(max_length=1000, null=True, blank=True)
    
        def __str__(self):
         return str(self.firstname) + '|' + str(self.contact)
