from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    #127.0.0.1:8000/polls
    url(r'^(?P<question_id>[0-9]+)/$',views.details,name='Details'),
    #127.0.0.1:8000/polls/1
    url(r'^(?P<question_id>[0-9]+)/results$',views.results,name='results'),
    #127.0.0.1:8000/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/vote$',views.vote,name='Votes'),
    #127.0.0.1:8000/polls/1/vote
]