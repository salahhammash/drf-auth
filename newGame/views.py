from django.shortcuts import render
from rest_framework import generics
from .models import Games
from .serializers import GameSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class GameList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class= GameSerializer
    permission_classes = [IsAuthenticated]

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]