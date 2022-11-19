from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def todos_list(request, format=None):
    if request.method == 'GET':
        todos_all = todos.objects.all()
        serializer = TodosSerializer(todos_all, many=True)

        return JsonResponse({"Todos": serializer.data})

    if request.method == 'POST':
        serializer = TodosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id, format=None):

    try:
        todo = todos.objects.get(pk=id)
    except todos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodosSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodosSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
