from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MyMerch
from .serializer import MyMerchSerializer
from .permissions import IsAdminOrReadOnly #add the permissions to the API view class.
from rest_framework import status #We first import the status module that will handle all the status code responses. 
# Create your views here.
## We import Response to handle the response for the API requests and
#  the the APIView as a base class for our API view function.
class MerchList(APIView):

    permission_classes = (IsAdminOrReadOnly,)
#We add an attribute permission_classes where we pass in the IsAdminOrReadOnly permission class.


    #We then define a get method where we query the database to get all the MyMerchobjects.
    #We then serialize the Django model objects and return the serialized data as a response.
    def get(self, request, format=None):
        all_merch = MyMerch.objects.all()
        serializers = MyMerchSerializer(all_merch, many=True)
        return Response(serializers.data)
# posting data to our databse


# adding post function method
    def post(self, request, format=None):
        #Since the post method will be triggered when we are getting form data,
        #  we will serialize the data in the request.
        serializers = MyMerchSerializer(data=request.data)
        if serializers.is_valid():
            ## We then confirm if the serialized data is valid. 
            serializers.save()
            #If valid we save the new data to the database and return the appropriate status code.


            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


## class for getting a single item fromthe list of items
class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return MyMerch.objects.get(pk=pk)
        except MyMerch.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MyMerchSerializer(merch)
        return Response(serializers.data)