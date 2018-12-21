from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,mixins,permissions
from .serializers import FileSecureSerializer
from FileSecure.models import FileSecureEntry
from django.views.generic import View
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
from accounts.api.permissions import IsOwnerOnly
from PersonJango.restconf.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter,OrderingFilter

class FileSecureDetailAPIView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.RetrieveAPIView):
    permission_classes      = [IsOwnerOnly]
    #authentication_classes  = [SessionAuthentication]
    queryset                = FileSecureEntry.objects.all()
    serializer_class        = FileSecureSerializer
    lookup_field            ='File_ID'


    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,reuest,*args,**kwargs):
        return self.destroy(reuest,*args,**kwargs)


class FileSecureAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes      = [IsOwnerOnly]
    serializer_class        = FileSecureSerializer
    queryset                = FileSecureEntry.objects.all()
    filter_backends         = (IsOwnerFilterBackend,SearchFilter,OrderingFilter)
    search_fields           = ('File_Module', 'File_CDate')


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save(UserName=self.request.user)

