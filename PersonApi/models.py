from django.db import models
from django.conf import settings
import json
from django.core.serializers.json import DjangoJSONEncoder
import binascii

# Create your models here.
def upload_file(instance,filename):
    import os
    from django.utils.timezone import now
    fname = binascii.hexlify(os.urandom(32))
    fnam = fname.decode("utf-8")
    filename_base, filename_ext = os.path.splitext(filename)
    print("persons/{user}/{filename}".format(user=instance.UserName,filename=fnam+filename_ext.lower()))
    return "persons/{user}/{filename}".format(user=instance.UserName,
                                              filename=fnam+filename_ext.lower())
class PersonQuerySet(models.QuerySet):
    def serialize(self):
        list_values=list(self.values('UserName','PersonId','PersonName','Person_Image','Person_sex','Person_BDate'))
        print (list_values)
        return json.dumps(list_values,sort_keys=True,indent=1,cls=DjangoJSONEncoder)

class PersonManager(models.Manager):
        def get_queryset(self):
            return PersonQuerySet(self.model,using=self._db)


class Person(models.Model):
    UserName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    PersonId = models.AutoField(primary_key=True)
    PersonName = models.CharField("person's first name", max_length=30,null=False)
    Person_Image = models.SlugField(null=True, blank=True)
    SEX = (('M','Male'),('F','Female'), ('N','None'), )
    Person_sex = models.CharField(max_length=1,choices=SEX,null=False)
    Person_BDate = models.DateField(null=False)
    Person_CDate =  models.DateField(null=False,auto_now_add=True)
    objects = PersonManager()

    def __str__(self):
        return str(self.PersonName) or ""

    def serialize(self):
        data={
            'UserName': self.UserName,
            'PersonId': self.PersonId,
            'PersonName': self.PersonName,
            'Person_Image':self.Person_Image,
            'Person_sex': self.Person_sex,
            'Person_Bdate': self.Person_BDate
        }
        data = json.dumps(data,sort_keys=True,indent=1,cls=DjangoJSONEncoder)
        return data

    @property
    def owner(self):
        return self.UserName
