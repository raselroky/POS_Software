from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import All_Number,All_Number_Sms,All_Supplier_Number,All_Supplier_Number_Smss,All_Customer_Number,All_Customer_Number_Smss
from .serializers import All_Number_Serializer,All_Number_Sms_Serializer,All_Supplier_Number_Serializer,All_Supplier_Number_Smss_Serializer,All_Customer_Number_Serializer,All_Customer_Number_Smss_Serializer


class All_Number_Sms_Api(APIView):
    def get(self,request):
        all_number=All_Number.objects.all()
        serializer=All_Number_Serializer(all_number,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=All_Number_Sms_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class All_Supplier_Number_Smss_Api(APIView):
    def get(self,request):
        all_supplier_number=All_Supplier_Number.objects.all()
        serializer=All_Supplier_Number_Serializer(all_supplier_number,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=All_Supplier_Number_Smss_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class All_Customer_Number_Smss_Api(APIView):
    def get(self,request):
        all_customer_number=All_Customer_Number.objects.all()
        serializer=All_Customer_Number_Serializer(all_customer_number,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=All_Customer_Number_Smss_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
