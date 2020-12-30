from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    
    def get(self,request,format=None):
        """return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function(get,put,post,delete,patch)',
            'Is similar to a traditional django view',
            'Gives you the most control over you appliction logic',
            'Is mapped manually to URLs.',
        ]
        return Response({'message':'hello!','an_apiview':an_apiview})