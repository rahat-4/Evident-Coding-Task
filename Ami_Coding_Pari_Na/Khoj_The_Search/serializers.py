from rest_framework import serializers

from User_Auth.models import MyUser
from .models import ValueList

class ValueListSerializer(serializers.ModelSerializer):
    #modify datetime format
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ValueList
        fields = ['timestamp', 'input_values']


class MyUserSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    #using nested serializer
    payload = ValueListSerializer(many=True, read_only=True)

    class Meta:
        model = MyUser
        fields = ['status', 'user_id', 'payload',]
    
    #get extra context which passing through ListAPIView
    def get_status(self,obj):
        status = self.context['status']
        return status
    
    #get individual user id
    def get_user_id(self,obj):
        return obj.pk