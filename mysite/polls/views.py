from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request,"polls/index.html", context)

def details(request, question_id):
    question= Question.objects.get(pk = question_id)
    return render(request,'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse('This is results of the questions %s'% question_id)

def vote(request, question_id):
    return HttpResponse('votes on questions are %s'% question_id)