from rest_framework import serializers
from .models import *
# class RegisterAPIView(GenericAPIView):

#     serializer_class = RegisterSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return response.Response()