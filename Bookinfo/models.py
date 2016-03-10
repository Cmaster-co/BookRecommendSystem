from django.db import models
from django.contrib import admin
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='static/images/')
    auther = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    page_num = models.IntegerField()
    index = models.CharField(max_length=150)
    info = models.TextField()
    def __str__(self):
        return self.title

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'index')

admin.site.register(Book, BookAdmin)