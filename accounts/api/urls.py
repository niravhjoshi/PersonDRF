from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
# from .views import AuthView
urlpatterns = [
    # url(r'^',AuthView.as_view()),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('allauth.urls')),
]