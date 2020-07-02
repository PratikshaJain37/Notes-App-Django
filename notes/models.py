from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    tag_text = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.tag_text


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited_date = models.DateTimeField(auto_now=True)
    tags = models.ForeignKey('Tag', related_name='notes', on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title
    


