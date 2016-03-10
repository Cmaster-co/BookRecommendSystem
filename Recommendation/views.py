from django.shortcuts import render
from django.db.models import Count
from DisplayLending.models import LendRecord
from Bookinfo.models import Book
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.
def recommend(request):
    user = request.user
    lend = LendRecord.objects.filter(user=user)
    lend_book = [i.book for i in lend]
    lend = LendRecord.objects.filter(book__in=lend_book)
    lend_user = [i.user for i in lend]
    rec_list = LendRecord.objects.filter(user__in=lend_user).values('book').annotate(dcount=Count('book'))

    rec_book = {}
    for i in rec_list:
        rec_book[i['book']]=i['dcount']
    rec_book = sorted(rec_book.iteritems(), key=lambda asd:asd[1], reverse=True)
    rec_bkl = []
    for i in rec_book:
        a = Book.objects.get(id=i[0])
        rec_bkl.append(a)
    t= loader.get_template("recommend.html")
    c = Context({'recommend':rec_bkl[:9]})
    return HttpResponse(t.render(c))