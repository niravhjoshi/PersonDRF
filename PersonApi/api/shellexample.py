'''

Python 2.7.14 |Anaconda, Inc.| (default, Nov  8 2017, 13:40:45) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
from DjangoE2ISAapi import wsgi
from persons.models import Person
from e2isaAPI.serializers import PersonSerializer
obj = Person.objects.first()
obj
#<Person: Nirav Joshi8((u'M', u'Male'), (u'F', u'Female'), (u'N', u'None'))1950-12-271>
data = PersonSerializer(obj)
data
#PersonSerializer(<Person: Nirav Joshi8((u'M', u'Male'), (u'F', u'Female'), (u'N', u'None'))1950-12-271>):
#    id = PrimaryKeyRelatedField(queryset=User.objects.all())
#    Pid = IntegerField(read_only=True)
#    PersonName = CharField(label=u"Person's first name", max_length=30)
#    Person_sex = ChoiceField(choices=((u'M', u'Male'), (u'F', u'Female'), (u'N', u'None')))
#    Person_BDate = DateField(label='Person BDate')
#    Person_CDate = DateField(label='Person CDate', read_only=True)
data.data
#{'Person_sex': u'M', 'PersonName': u'Nirav Joshi', 'Person_BDate': '1950-12-27', 'Pid': 8, 'Person_CDate': '2018-08-08',
# 'id': 1L}
import json
from rest_framework.renderers import JSONRenderer
new_json_renderdata = JSONRenderer().render(data.data)
print(new_json_renderdata)
#{"id":1,"Pid":8,"PersonName":"Nirav Joshi","Person_sex":"M","Person_BDate":"1950-12-27","Person_CDate":"2018-08-08"}
print type(new_json_renderdata)
#<type 'str'>
json.loads(new_json_renderdata)
#{u'Person_sex': u'M', u'PersonName': u'Nirav Joshi', u'Person_BDate': u'1950-12-27', u'Pid': 8, u'Person_CDate': u'2018-
#08-08', u'id': 1}
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
stream = BytesIO(json)
data = JSONParser().parse(stream)
json = new_json_renderdata
stream = BytesIO(json)
data = JSONParser().parse(stream)
data
#{u'Person_sex': u'M', u'PersonName': u'Nirav Joshi', u'Person_BDate': u'1950-12-27', u'Pid': 8, u'Person_CDate': u'2018-
#08-08', u'id': 1}
#>>>
qs = Person.objects.all()
serializer = PersonSerializer(qs,many=True)
serializer.data
#[OrderedDict([('id', 1L), ('Pid', 8), ('PersonName', u'Nirav Joshi'), ('Person_sex', u'M'), ('Person_BDate', '1950-12-27
#'), ('Person_CDate', '2018-08-08')]), OrderedDict([('id', 1L), ('Pid', 9), ('PersonName', u'Luke'), ('Person_sex', u'F')
#, ('Person_BDate', '2018-08-30'), ('Person_CDate', '2018-08-08')]), OrderedDict([('id', 1L), ('Pid', 10), ('PersonName',
# u'Darth'), ('Person_sex', u'N'), ('Person_BDate', '2018-08-30'), ('Person_CDate', '2018-08-08')]), OrderedDict([('id',
#1L), ('Pid', 11), ('PersonName', u'Pareen Joshi'), ('Person_sex', u'F'), ('Person_BDate', '2018-08-30'), ('Person_CDate'
#, '2018-08-13')])]
json_data = JSONRenderer().render(serializer.data)
json_data
#'[{"id":1,"Pid":8,"PersonName":"Nirav Joshi","Person_sex":"M","Person_BDate":"1950-12-27","Person_CDate":"2018-08-08"},{
#"id":1,"Pid":9,"PersonName":"Luke","Person_sex":"F","Person_BDate":"2018-08-30","Person_CDate":"2018-08-08"},{"id":1,"Pi
#d":10,"PersonName":"Darth","Person_sex":"N","Person_BDate":"2018-08-30","Person_CDate":"2018-08-08"},{"id":1,"Pid":11,"P
#ersonName":"Pareen Joshi","Person_sex":"F","Person_BDate":"2018-08-30","Person_CDate":"2018-08-13"}]'
json.loads(json_data)
import json
json.loads(json_data)
#[{u'Person_sex': u'M', u'PersonName': u'Nirav Joshi', u'Person_BDate': u'1950-12-27', u'Pid': 8, u'Person_CDate': u'2018
#-08-08', u'id': 1}, {u'Person_sex': u'F', u'PersonName': u'Luke', u'Person_BDate': u'2018-08-30', u'Pid': 9, u'Person_CD
#ate': u'2018-08-08', u'id': 1}, {u'Person_sex': u'N', u'PersonName': u'Darth', u'Person_BDate': u'2018-08-30', u'Pid': 1
#0, u'Person_CDate': u'2018-08-08', u'id': 1}, {u'Person_sex': u'F', u'PersonName': u'Pareen Joshi', u'Person_BDate': u'2
#018-08-30', u'Pid': 11, u'Person_CDate': u'2018-08-13', u'id': 1}]


#Create Person
data = {
    'id':1,
    'PersonName':'XXX Joshi',
    'Person_sex':'M',
    'Person_BDate':'2018-08-13'
}

serializer = PersonSerializer(data=data)
serializer.is_valid()
serializer.save()

#Update Serializer

upddata = {
    'id': 1,
    'PersonName':'Update Joshi',
    'Person_sex':'F',
    'Person_BDate':'2018-08-05'
}
serializer = PersonSerializer(data = upddata)
obj = Person.objects.first()
updateserialize = PersonSerializer(obj, data=upddata)
updateserialize.is_valid()
updateserialize.save()

Person.objects.all()


#Delete Serializer
data = {
    'id':1,
    'PersonName':'Valid Joshi',
    'Person_sex':'F',
    'Person_BDate':'2018-12-13'
}

create_obj_serializer = PersonSerializer(data=data)
create_obj_serializer.is_valid()
create_obj_serializer.save()
print(create_obj_serializer)
print create_obj_serializer.data['Pid']

#Original delete method.
obj = Person.objects.last()
get_data_serilizer = PersonSerializer(obj)
print get_data_serilizer
print get_data_serilizer.data['Pid']
print obj.delete()
'''







