from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import All_Sales,List_Draft,Shipments,Discount,Location_Set,List_Sell_Return
from .serializers import All_Sales_Serializer,List_Draft_Serializer,Shipments_Serializer,Discount_Serializer,Location_Set_Serializer,List_Sell_Return_Serializer,All_Sales__All_Show_Serializer,List_Draft_All_Show_Serializer,Shipments_All_Show_Serializer,Discount_All_Show_Serializer,List_Sell_Return_All_Show_Serializer
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from rest_framework import generics


class All_Sales_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return All_Sales.objects.get(p_k=pk)
        except All_Sales.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = All_Sales__All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = All_Sales__All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

    
    
class List_Draft_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return List_Draft.objects.get(p_k=pk)
        except List_Draft.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Draft_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Draft_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class List_Sell_Return_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return List_Sell_Return.objects.get(p_k=pk)
        except List_Sell_Return.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Sell_Return_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Sell_Return_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


    

class Shipments_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Shipments.objects.get(p_k=pk)
        except Shipments.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Shipments_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Shipments_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Discount_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Discount.objects.get(p_k=pk)
        except Discount.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Discount_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Discount_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})


class Location_Set_Api_List(APIView):
    def get(self,request):
        location_set=Location_Set.objects.all()
        serializer=Location_Set_Serializer(location_set,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Location_Set_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Location_Set_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Location_Set.objects.get(p_k=pk)
        except Location_Set.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Location_Set_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Location_Set_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})




class All_Sales_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Created_At','Invoice_No','Contact_Number','Payment_Status','Payment_Method','Total_Amount','Total_Paid','Sell_Due','Sell_Return_Due','Shipping_Status','Shipping_Address','Total_Items','Added_By']
    #filter_backends = (filters.SearchFilter,)
    queryset = All_Sales.objects.all()
    serializer_class = All_Sales_Serializer
class All_Sales_All_Show_Searh_Api(generics.ListAPIView):
    search_fields = ['Created_At','Invoice_No','Contact_Number','Payment_Status','Payment_Method','Total_Amount','Total_Paid','Sell_Due','Sell_Return_Due','Shipping_Status','Shipping_Address','Total_Items','Added_By']
    filter_backends = (filters.SearchFilter,)
    queryset = All_Sales.objects.all()
    serializer_class = All_Sales__All_Show_Serializer


class List_Sell_Return_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Created_At','Invoice_No','Parent_Sale','Contact_Number','Payment_Status','Total_Amount','Payment_Due']
    #filter_backends = (filters.SearchFilter,)
    queryset = List_Sell_Return.objects.all()
    serializer_class = List_Sell_Return_Serializer
class List_Sell_Return_All_Show_Searh_Api(generics.ListAPIView):
    search_fields = ['Created_At','Invoice_No','Parent_Sale','Contact_Number','Payment_Status','Total_Amount','Payment_Due']
    filter_backends = (filters.SearchFilter,)
    queryset = List_Sell_Return.objects.all()
    serializer_class = List_Sell_Return_All_Show_Serializer


class List_Draft_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Created_At','Reference_No','Contact_Number','Total_Items','Added_By']
    #filter_backends = (filters.SearchFilter,)
    queryset = List_Draft.objects.all()
    serializer_class = List_Draft_Serializer
class List_Draft_All_Show_Searh_Api(generics.ListAPIView):
    search_fields = ['Created_At','Reference_No','Contact_Number','Total_Items','Added_By']
    filter_backends = (filters.SearchFilter,)
    queryset = List_Draft.objects.all()
    serializer_class = List_Draft_All_Show_Serializer


class Shipment_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Created_At','Invoice_No','Contact_Number','Shipping_Status','Payment_Status','Service_Staff']
    #filter_backends = (filters.SearchFilter,)
    queryset = Shipments.objects.all()
    serializer_class = Shipments_Serializer
class Shipment_All_Show_Searh_Api(generics.ListAPIView):
    search_fields = ['Created_At','Invoice_No','Contact_Number','Shipping_Status','Payment_Status','Service_Staff']
    filter_backends = (filters.SearchFilter,)
    queryset = Shipments.objects.all()
    serializer_class = Shipments_All_Show_Serializer


class Discount_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Starts_At','Ends_At','Discount_Amount','Priority','Brand','Category','Product']
    #filter_backends = (filters.SearchFilter,)
    queryset = Discount.objects.all()
    serializer_class = Discount_Serializer
class Discount_All_Show_Searh_Api(generics.ListAPIView):
    search_fields = ['Starts_At','Ends_At','Discount_Amount','Priority','Brand','Category','Product']
    filter_backends = (filters.SearchFilter,)
    queryset = Discount.objects.all()
    serializer_class = Discount_All_Show_Serializer


class Location_Search_Api(generics.ListCreateAPIView):
    search_fields = ['Location']
    filter_backends = (filters.SearchFilter,)
    queryset =Location_Set.objects.all()
    serializer_class = Location_Set_Serializer