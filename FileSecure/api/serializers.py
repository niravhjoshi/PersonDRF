from rest_framework import serializers
import datetime
from FileSecure.models import FileSecureEntry
from accounts.api.serializers import UserPublicSerializer
from django.core.exceptions import PermissionDenied
from PersonApi.models import Person


class FileSecureSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    UserNameID = UserPublicSerializer(read_only=True)


    class Meta:
        model = FileSecureEntry
        fields = [
            'uri'
            'File_ID',
            'UserNameID',
            'PersonNameID',
            'File_Module',
            'File_Image',
            'File_CDate'

        ]
        read_only_fields = ['UserNameID','File_ID','PersonNameID']  # Get calls its gone be read only.

        uri             = serializers.SerializerMethodField(read_only=True)
        UserNameID      = UserPublicSerializer(read_only=True)

    def get_uri(self,obj):
        return "/api/Persons/{id}".format(id=obj.PersonNameID)
