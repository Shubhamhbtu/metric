from rest_framework import serializers
from .models import MyData


class MyDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyData
        fields = ('input_list',)
