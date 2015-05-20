from django.db import models

# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 250)
    def __str__(self):
        return str(self.name)
class Article(models.Model):
    type = models.ManyToManyField(ArticleCaegory)
    title = models.CharField(max_length = 40)
    keywords = models.TextField()
    background = models.TextField(blank=True)
    description = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True, blank=True)
    def __str__(self):
        return str(self.title) + "-" + type.