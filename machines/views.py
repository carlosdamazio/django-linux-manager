from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from machines.models import Machine
from machines.serializers import MachineSerializer


class MachineList(APIView):

    @staticmethod
    def get(request):
        data = Machine.objects.all()
        serializer = MachineSerializer(data, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)