from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField('title', max_length = 100, null = False)
    description = models.TextField('description', max_length = 255, null = False)
    text = models.TextField('text', null = False)
    slug = models.SlugField('slug', unique = True, db_index = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('atricle_detail', kwargs={'slug': self.slug})
