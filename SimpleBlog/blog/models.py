from django.db import models
from django.utils.text import slugify


class PostCetgory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super().save(*arg, **kwargs)

class BlogPost(models.Model):
    status = [
        (0, 'draft'),
        (1, 'publish')
    ]
    title = models.CharField(max_length=150, help_text='Enter Your Title Here')
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post_status = models.IntegerField(choices=status, default=0)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)