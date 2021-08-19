from rest_framework.response import Response
from rest_framework.views import APIView


class Demo(APIView):
    def get(self, request):
        name = request.GET.get('name')
        return Response({"Name": name})
