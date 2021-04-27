from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',views.home,name="home"),
    #127.0.0.1:8000/
    url(r'^polls/$', views.index, name="index"),
    #127.0.0.1:8000/polls
    url(r'^polls/(?P<question_id>[0-9]+)/$',views.details,name='detail'),
    #127.0.0.1:8000/polls/1
    url(r'^polls/(?P<question_id>[0-9]+)/results$',views.results,name='results'),
    #127.0.0.1:8000/polls/1/results
    url(r'^polls/(?P<question_id>[0-9]+)/vote$',views.vote,name='votes'),
    #127.0.0.1:8000/polls/1/vote
]