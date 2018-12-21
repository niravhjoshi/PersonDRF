from django.contrib import admin
from django.conf.urls import url, include
from .views import  PersonAPIView,PersonDetailAPIView

urlpatterns = [
    #url(r'^$',PersonListSearchAPIView.as_view()),
    url(r'^$',PersonAPIView.as_view()),
    url(r'^(?P<PersonId>\d+)/$',PersonDetailAPIView.as_view()),
    #url(r'^create/$',PersonCreateAPIView.as_view()),
    #url(r'^(?P<Pid>\d+)/$',PersonDetailAPIView.as_view()),
    #url(r'^(?P<Pid>\d+)/update/$',PersonUpdateAPIView.as_view()),
    #url(r'^(?P<Pid>\d+)/delete/$',PersonDeleteAPIView.as_view()),
]
#Start with
# /api/persons/ --> List view
# /api/persons/create -->create person
# /api/persons/12 ---> Detail view
# /api/persons/12 ---> Update view
# /api/persons/12 ---> Dlete view

#End with
# /api/persons/--> List -> CRUD
# /api/persons/12 --> Details -> CRUD

#Final with
# /api/persons/  -> CRUD and LS
