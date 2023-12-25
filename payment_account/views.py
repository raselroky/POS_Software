from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import List_Account,Account_type,Liability,Assets,Trial_Balance,Cash_Flow,Payment_Account_Report
from .serializers import List_Account_Serializer,Account_type_Serialzer,Liability_Serializer,Assets_Serializer,Trial_Balance_Serializer,Cash_Flow_Serializer,Payment_Account_Report_Serializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import filters

class List_Account_Api_List(APIView):
    def get(self,request):
        list_account=List_Account.objects.all()
        serializer=List_Account_Serializer(list_account,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=List_Account_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class List_Account_Api_Detial(APIView):
    def get_object(self, pk):
        try:
            return List_Account.objects.get(p_k=pk)
        except List_Account.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Account_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Account_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class Account_Types_Api_List(APIView):
    def get(self,request):
        account_types=Account_type.objects.all()
        serializer=Account_type_Serialzer(account_types,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        serializer=Account_type_Serialzer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Account_Types_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Account_type.objects.get(p_k=pk)
        except Account_type.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Account_type_Serialzer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Account_type_Serialzer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Liability_Api_List(APIView):
    def get(self,request):
        liability=Liability.objects.all()
        serializer=Liability_Serializer(liability,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Liability_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Liability_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Liability.objects.get(p_k=pk)
        except Liability.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Liability_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Liability_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})




class Assets_Api_List(APIView):
    def get(self,request):
        assets=Assets.objects.all()
        serializer=Assets_Serializer(assets,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Assets_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Assets_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Assets.objects.get(p_k=pk)
        except Assets.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Assets_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Assets_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Trial_Balance_Api_List(APIView):
    def get(self,request):
        trial_balance=Trial_Balance.objects.all()
        serializer=Trial_Balance_Serializer(trial_balance,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Trial_Balance_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Trial_Balance_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Trial_Balance.objects.get(p_k=pk)
        except Trial_Balance.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Trial_Balance_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Trial_Balance_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Cash_Flow_Api_List(APIView):
    def get(self,request):
        cash_flow=Cash_Flow.objects.all()
        serializer=Trial_Balance_Serializer(cash_flow,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Cash_Flow_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Cash_Flow_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Cash_Flow.objects.get(p_k=pk)
        except Cash_Flow.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Cash_Flow_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Cash_Flow_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Payment_Account_Report_Api_List(APIView):
    def get(self,request):
        payment_account_report=Payment_Account_Report.objects.all()
        serializer=Payment_Account_Report_Serializer(payment_account_report,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Payment_Account_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Payment_Account_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Payment_Account_Report.objects.get(p_k=pk)
        except Payment_Account_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Payment_Account_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Payment_Account_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class List_Account_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=List_Account.objects.all()
    serializer_class=List_Account_Serializer

class Account_Type_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=Account_type.objects.all()
    serializer_class=Account_type_Serialzer

class Liability_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=Liability.objects.all()
    serializer_class=Liability_Serializer

class Assets_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=Assets.objects.all()
    serializer_class=Assets_Serializer

class Trial_Balance_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=Trial_Balance.objects.all()
    serializer_class=Trial_Balance_Serializer

class Cash_Flow_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=Cash_Flow.objects.all()
    serializer_class=Cash_Flow_Serializer

class Payment_Account_Report_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    queryset=Payment_Account_Report.objects.all()
    serializer_class=Payment_Account_Report_Serializer