from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    summary = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

        def __str__(self):
            return self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

