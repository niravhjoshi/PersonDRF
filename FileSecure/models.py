from django.db import models
from django.conf import settings
import json
from django.core.serializers.json import DjangoJSONEncoder
import binascii
from PersonApi import models as PersonModel
from django.contrib.auth.models import User


def upload_file(instance,filename):
    import os
    from django.utils.timezone import now
    fname = binascii.hexlify(os.urandom(32))
    fnam = fname.decode("utf-8")
    filename_base, filename_ext = os.path.splitext(filename)
    print("persons/{user}/{filename}".format(user=instance.UserName,filename=fnam+filename_ext.lower()))
    return "persons/{user}/{filename}".format(user=instance.UserName,
                                              filename=fnam+filename_ext.lower())


class FileSecureQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('File_ID', 'UserNameID', 'PersonNameID', 'File_Module', 'File_Image', 'File_CDate'))
        print(list_values)
        return json.dumps(list_values, sort_keys=True, indent=1, cls=DjangoJSONEncoder)


class FileSecureManager(models.Manager):
    def get_queryset(self):
        return FileSecureQuerySet(self.model, using=self._db)


# Create your models here.
class FileSecureEntry(models.Model):
    File_ID         = models.AutoField(primary_key=True)
    UserNameID      = models.OneToOneField(User)
    #UserNameID=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    File_Image      = models.FileField(upload_to=upload_file, null=True, blank=True)
    File_CDate      = models.DateField(null=False, auto_now_add=True)



    def __str__(self):
        return str(self.File_ID) + str(self.UserNameID) +  +str(self.File_Image)+str(self.File_CDate)

    def serialize(self):
        data = {
            'File_ID': self.File_ID,
            'UserNameID': self.UserNameID,
            'File_Image': self.File_Image,
            'File_CDate': self.File_CDate

        }
        data = json.dumps(data, sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return data

    @property
    def owner(self):
        return self.UserNameID