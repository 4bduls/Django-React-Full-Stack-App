from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# Create your views here.

class NoteListCreate(generics.ListCreateAPIView): #list create view instead of just creating: either will list all note or create new note
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer): #overriding create function. saves (as a note) if serializing data is valid
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class=NoteSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #list of all diff objects so we dont create one we already have
    serializer_class=UserSerializer #what kinda data we need to accept to make a new user
    permission_classes= [AllowAny] #who can call this- anyone in this case