from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import permissions , status
from rest_framework.response import Response

from .models import KeyValue
from .serializers import KeyValueSerializer

class KeyValueList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self , request):
        kv = KeyValue.objects.all()
        serializer = KeyValueSerializer(kv , many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = KeyValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class KeyValueDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,key):
        kv = get_object_or_404(KeyValue,key=key)
        serializer = KeyValueSerializer(kv)
        return Response(serializer.data)

    def put(self,request,key):
        try:
            kv = KeyValue.objects.get(key=key)
            serializer = KeyValueSerializer(kv,data=request.data,partial=True)
        except KeyValue.DoesNotExist :
            serializer = KeyValueSerializer(data = {"key":key , **request.data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)