from django.shortcuts import render
from DisplayLending.models import LendRecord
from django.template import loader,Context
from django.http import HttpResponse
# Create your views here.
def dis_lend(request):
    user_id = request.user.id
    records = LendRecord.objects.filter(user_id=user_id)
    t= loader.get_template("lendrecord.html")
    c = Context({'lend_record': records})
    return HttpResponse(t.render(c))