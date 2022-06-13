from pyexpat import model
from rest_framework import serializers
from .models import MyMerch

class MyMerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyMerch
        fields = ('id','name','description','price')