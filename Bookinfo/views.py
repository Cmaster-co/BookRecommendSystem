from django.shortcuts import render
from Bookinfo.models import Book
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.
def dis_info(request):
    bookid= request.POST.get('bookid','')
    bookinfo = Book.objects.get(index=bookid)
    t= loader.get_template("bookinfo.html")
    c = Context({'book_info': bookinfo})
    return HttpResponse(t.render(c))