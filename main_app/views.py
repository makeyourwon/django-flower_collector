
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to flower_collector app.'}
        return Response(content)