from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from Recommendation.models import RecomendBook
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = str(request.POST.get('username',''))
        password = str(request.POST.get('password',''))
        user = auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/recommend/')
        else:
            return HttpResponseRedirect('/')


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def home(request):
    rb = RecomendBook.objects.filter(is_active=True)
    book_list = [i.book for i in rb]
    t= loader.get_template("home.html")
    c = Context({'book_list': book_list})
    return HttpResponse(t.render(c))