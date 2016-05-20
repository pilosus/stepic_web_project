from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

# Create your views here.
from django.http import HttpResponse 

@require_GET
def index(request, *args, **kwargs):
    # list of questions in desc order by publication datetime
    question_list = Question.objects.order_by('-added_at')

    # pagination
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    paginator = Paginator(question_list, limit)
        
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    
    try:
        questions = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    context = {
        'questions': questions,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/index.html', context)

@require_GET
def popular(request, *args, **kwargs):
    # list of questions in desc order by rating
    question_list = Question.objects.order_by('-rating')

    # pagination
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    paginator = Paginator(question_list, limit)
        
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    
    try:
        questions = paginator.page(page)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    
    context = {
        'questions': questions,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/popular.html', context)


def test(request, *args, **kwargs):
    context = {'var1': 1, 'var2': 2}
    return render(request, 'qa/index.html', context)
    #return HttpResponse('OK')

def question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    a = Answer.objects.filter(question=q.id).order_by('-added_at')
    
    context = {
        'question': q,
        'answers': a,
    }
    return render(request, 'qa/question.html', context)    
