
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'assoc_type', 'assoc_id','publish_email','seq')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name','last_name','country','email','user_group')

