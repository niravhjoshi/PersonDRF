from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# from .permissions import  AnonPermission




#
# class AuthView(APIView):
#     # permission_classes     = [AnonPermission]
#     def post(self,request,*args,**kwargs):
#         print(request.user)
#         if request.user.is_authenticated():
#             return Response({'details':'You are authenticated '},status=400)
#
#         return Response({'Token':'Nirav'})   #
