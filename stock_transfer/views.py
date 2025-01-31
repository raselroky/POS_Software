from django.shortcuts import render
from rest_framework.views import APIView
from .models import Stock_Transfer
from .serializers import Stock_Transfer_Serializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from rest_framework import generics


class Stock_Transfer_Api_List(APIView):
    def get(self,request):
        stock_transfer=Stock_Transfer.objects.all()
        serializer=Stock_Transfer_Serializer(stock_transfer,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Stock_Transfer_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Stock_Transfer_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Stock_Transfer.objects.get(p_k=pk)
        except Stock_Transfer.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Transfer_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Transfer_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class Stock_Transfer_Search_Api(generics.ListCreateAPIView):
    search_fields=['Date','Reference_No','Location_From','Location_To','Status','Shipping_Charges','Total_Amount','Additional_Notes']
    filter_backends=(filters.SearchFilter,)
    queryset=Stock_Transfer.objects.all()
    serializer_class=Stock_Transfer_Serializer