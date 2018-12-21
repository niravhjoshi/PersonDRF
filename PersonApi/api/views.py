from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from .serializers import PersonSerializer
from PersonApi.models import Person
from django.views.generic import View
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
from accounts.api.permissions import IsOwnerOnly
from PersonJango.restconf.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter,OrderingFilter

class PersonDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    #authentication_classes  = [SessionAuthentication]
    queryset                = Person.objects.all()
    serializer_class        = PersonSerializer
    lookup_field            ='PersonId'


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,reuest,*args,**kwargs):
        return self.destroy(reuest,*args,**kwargs)


class PersonAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    serializer_class        = PersonSerializer
    queryset                = Person.objects.all()
    filter_backends         = (IsOwnerFilterBackend,SearchFilter,OrderingFilter)
    search_fields           = ('PersonName', 'Person_sex')


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)

