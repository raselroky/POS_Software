from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stock_Adjustment
from .serializers import Stock_Adjustment_Serializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import filters


class Stock_Adjustment_Api_List(APIView):
    def get(self,request):
        stock_adjustment=Stock_Adjustment.objects.all()
        serializer=Stock_Adjustment_Serializer(stock_adjustment,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Stock_Adjustment_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Stock_Adjustment_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Stock_Adjustment.objects.get(p_k=pk)
        except Stock_Adjustment.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Adjustment_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Adjustment_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class Stock_Adjustment_Search_Api(generics.ListCreateAPIView):
    search_fields=['Action','Date','Reference_No','Adjustment_Type','Total_Amount','Total_Amount_Recovered','Reason','Added_By']
    filter_backends=(filters.SearchFilter,)
    queryset=Stock_Adjustment.objects.all()
    serializer_class=Stock_Adjustment_Serializer