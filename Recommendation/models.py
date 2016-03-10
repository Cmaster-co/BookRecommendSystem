from django.db import models
from django.contrib import admin
from Bookinfo.models import Book
# Create your models here.
class RecomendBook(models.Model):
    book = models.ForeignKey(Book)
    is_active = models.BooleanField()
    def __str__(self):
        return self.book.title

class RecommendBookAdmin(admin.ModelAdmin):
    list_display = ('book','is_active')

admin.site.register(RecomendBook, RecommendBookAdmin)