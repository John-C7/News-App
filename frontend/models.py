from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    region = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
