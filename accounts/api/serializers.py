from django.contrib.auth import get_user_model
from rest_framework import serializers
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import models
#from rest_social_auth.views import SocialSessionAuthView


User = get_user_model()

#
# class MyUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         exclude = ('password', 'user_permissions', 'groups')
#
#
# class MySocialView(SocialSessionAuthView):
#     serializer_class = MyUserSerializer

class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]

    def get_uri(self,obj):
        return '/api/users/{id}'.format(id = obj.id)



