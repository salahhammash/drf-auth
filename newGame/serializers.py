from rest_framework import serializers
from .models import Games

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        # fields='__all__'
        fields = ('id','owner','name','desc','created_at','updated_at')