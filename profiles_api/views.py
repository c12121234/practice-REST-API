from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer
    
    def get(self,request,format=None):
        """return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function(get,put,post,delete,patch)',
            'Is similar to a traditional django view',
            'Gives you the most control over you appliction logic',
            'Is mapped manually to URLs.',
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request,pk=None):
        """updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """ a partial update of object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """ delete an object"""
        return Response({'method':'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    
    serializer_class = serializers.HelloSerializer
    
    def list(self,request):
        """return hello string"""
        a_viewset = [
            'uses actions (list,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        
        return Response({'message':'hello','a_viewset':a_viewset})
    
    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self,request,pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        """handle update an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """handle update part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    #notice typo
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) 
    permission_classes = (permissions.UpdateOwnProfile,)