from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("title", max_length=200)
    text = models.TextField("text")
    author = models.CharField("author", max_length=50)
    pub_date = models.DateTimeField('pub_date')
    files = models.FileField("files", blank = True, null = True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["pub_date"]

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    author = models.CharField('author', max_length=50)
    text = models.CharField('text', max_length=1000)
    pub_date = models.DateTimeField('pub_date', blank = True, null = True)
    files = models.FileField("files", blank = True, null = True)

    def __str__(self):
        return self.author
    
    class Meta:
        ordering = ["pub_date"]