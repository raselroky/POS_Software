from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Purchases,Add_Purchase,List_Purchase_Return,Additional_Expense
from .serializers import Purchases_Serializer,Add_Purchases_Serializer,List_Purchase_Return_Serializer,Additonal_Expense_Serializer,Purchases_All_Show_Serializer,Add_Purchases_All_Show_Serializer,List_Purchase_Return_All_Show_Serializer
from django.http import Http404
from rest_framework import status
from rest_framework import filters
from rest_framework import generics


class Purchase_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Purchases.objects.get(p_k=pk)
        except Purchases.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchases_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchases_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class Add_Purchase_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Add_Purchase.objects.get(p_k=pk)
        except Add_Purchase.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Add_Purchases_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Add_Purchases_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



    
class List_Purchase_Return_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return List_Purchase_Return.objects.get(p_k=pk)
        except List_Purchase_Return.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Purchase_Return_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Purchase_Return_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class Additional_Expense_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Additional_Expense.objects.get(p_k=pk)
        except Additional_Expense.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Additonal_Expense_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Additonal_Expense_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})





class Purchase_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Created_At','Reference_No','Purchase_Status','Payment_Status','Grand_Total','Payment_Due','Added_By']
    #filter_backends = (filters.SearchFilter,)
    queryset = Purchases.objects.all()
    serializer_class = Purchases_Serializer

class Purchase_All_Show_Search_Api(generics.ListAPIView):
    search_fields = ['Created_At','Reference_No','Purchase_Status','Payment_Status','Grand_Total','Payment_Due','Added_By']
    filter_backends = (filters.SearchFilter,)
    queryset = Purchases.objects.all()
    serializer_class = Purchases_All_Show_Serializer


class Add_Purchase_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Reference_No','Purchase_Date','Purchase_Status','Address','Pay_Term','Attached_Document','Discount_Type','Discount_Amount','Purchase_Tax','Additional_Notes','Shipping_Details','Additional_Shipping_Charges','Amount','Paid_On','Payment_Method','Payment_Note']
    #filter_backends = (filters.SearchFilter,)
    queryset = Add_Purchase.objects.all()
    serializer_class = Add_Purchases_Serializer
class Add_Purchase_All_Show_Search_Api(generics.ListAPIView):
    search_fields = ['Reference_No','Purchase_Date','Purchase_Status','Address','Pay_Term','Attached_Document','Discount_Type','Discount_Amount','Purchase_Tax','Additional_Notes','Shipping_Details','Additional_Shipping_Charges','Amount','Paid_On','Payment_Method','Payment_Note']
    filter_backends = (filters.SearchFilter,)
    queryset = Add_Purchase.objects.all()
    serializer_class = Add_Purchases_All_Show_Serializer

class List_Purchase_Return_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Created_At','Reference_No','Parent_Purchase','Payment_Status','Grand_Total','Payment_Due']
    #filter_backends = (filters.SearchFilter,)
    queryset = List_Purchase_Return.objects.all()
    serializer_class = List_Purchase_Return_Serializer
class List_Purchase_Return_All_Show_Search_Api(generics.ListAPIView):
    search_fields = ['Created_At','Reference_No','Parent_Purchase','Payment_Status','Grand_Total','Payment_Due']
    filter_backends = (filters.SearchFilter,)
    queryset = List_Purchase_Return.objects.all()
    serializer_class = List_Purchase_Return_All_Show_Serializer


class Additional_Expense_Add_Search_APi(generics.ListCreateAPIView):
    search_fields = ['Expense_Name','Amount']
    filter_backends = (filters.SearchFilter,)
    queryset = Additional_Expense.objects.all()
    serializer_class = Additonal_Expense_Serializer