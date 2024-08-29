from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username", "password"]
        extra_kwargs= {"password": {"write_only": True}} #write only means that we dont send the password when returning information about the user
        
    def create(self,validated_data): #func called when we wanna create new version of user
        user=User.objects.create_user(**validated_data) #validated data is data thats been checked by our serializer
        #seri
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author" : {"read_only":True}}