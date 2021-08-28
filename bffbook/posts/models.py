from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.base import Model
from profiles.models import Profile
# Create your models here.
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="posts_img", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return str(self.content[0:20])

    def num_likes(self):
        return self.liked.all().count()
    
    #numberofcommentshere
    def num_comment(self):
        return self.comment_set.all().all()

    class Meta:
        ordering = ('-created',)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('unlike', 'unlike')
)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    
