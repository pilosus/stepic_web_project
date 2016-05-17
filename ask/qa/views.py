from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    context = {'var1': 1, 'var2': 2}
    return render(request, 'qa/index.html', context)
    #return HttpResponse('OK')

def question(request, question_id):
    return HttpResponse("You have reached question #%s" % question_id)
