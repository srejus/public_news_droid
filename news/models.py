from django.db import models
from accounts.models import Account

# Create your models here.
class News(models.Model):
    posted_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='posted_by')
    title = models.CharField(max_length=100)
    news_cover_img = models.ImageField(upload_to='news_cover')
    content = models.TextField()
    tags = models.TextField(null=True,blank=True)
    catgegory = models.CharField(max_length=100,default='others')
    is_fake = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    commented_by = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='commented_by')
    news = models.ForeignKey(News,on_delete=models.CASCADE,related_name='news')
    comment = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)