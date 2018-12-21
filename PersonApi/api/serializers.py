from rest_framework import serializers
import datetime
from PersonApi.models import Person
from accounts.api.serializers import UserPublicSerializer
from django.core.exceptions import PermissionDenied



class PersonSerializer(serializers.ModelSerializer):

    uri      = serializers.SerializerMethodField(read_only=True)
    UserName = UserPublicSerializer(read_only=True)
    class Meta:
        model = Person
        fields = [
            'uri',
            'UserName',
            'PersonId',
            'PersonName',
            'Person_Image',
            'Person_sex',
            'Person_BDate',
            'Person_CDate'
        ]
        read_only_fields=['UserName'] # Get calls its gone be read only.

    def get_uri(self,obj):
        return "/api/Persons/{id}".format(id=obj.PersonId)

    def validate_personName(self,value):
        if len(value) > 30:
            raise serializers.ValidationError("PersonName should not be more than 30 Char")
        return value
    def validate_personsex(self,value):
        if value not in ['M','F','N']:
            raise  serializers.ValidationError("PersonSex should be M F or N")
        return value
    def validate_personbdate(self,value):
        if datetime.datetime.strptime(value, '%Y-%m-%d'):
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")
        return value
    def validate_personimg(self,value):
        pass
