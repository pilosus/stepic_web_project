from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, question_id):
    return HttpResponse("You have reached question #%s" % question_id)
