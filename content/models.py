from django.db import models

# Create your models here.
class Article(models.Model):
    TYPE_CHOICES = (
        ('1', 'science'),
        ('2', 'arts'),
        ('3', 'history'),
        ('4', 'business'),
        ('5', 'computers'),
        ('6', 'engineering'),
        ('7', 'medicine'),
        ('8', 'everyday')
    )
    type = models.MultipleChoiceField(choices=TYPE_CHOICES)
    title = models.CharField(max_length = 40)
    keywords = models.TextField()
    background = models.TextField(blank=True)
    description = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True, blank=True)