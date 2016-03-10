from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from Bookinfo.models import Book
# Create your models here.
class LendRecord(models.Model):
    user = models.ForeignKey(User, related_name='lend_user')
    book = models.ForeignKey(Book, related_name='lend_book')
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True)
    is_return = models.NullBooleanField()
    def __str__(self):
        return self.book.title

class LendRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')

admin.site.register(LendRecord, LendRecordAdmin)