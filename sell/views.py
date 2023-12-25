from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import All_Sales,List_Draft,Shipments,Discount,Location_Set,List_Sell_Return
from .serializers import All_Sales_Serializer,List_Draft_Serializer,Shipments_Serializer,Discount_Serializer,Location_Set_Serializer,List_Sell_Return_Serializer
from rest_framework import status
from django.http import Http404
from rest_framework import filters
from rest_framework import generics


class All_Sales_Api_List(APIView):
    def get(self,request):
        all_sales=All_Sales.objects.all()
        serializer=All_Sales_Serializer(all_sales,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=All_Sales_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class All_Sales_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return All_Sales.objects.get(p_k=pk)
        except All_Sales.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = All_Sales_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = All_Sales_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


class List_Draft_Api_List(APIView):
    def get(self,request):
        list_draft=List_Draft.objects.all()
        serializer=List_Draft_Serializer(list_draft,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=List_Draft_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class List_Draft_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return List_Draft.objects.get(p_k=pk)
        except List_Draft.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Draft_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Draft_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class List_Sell_Return_Api_List(APIView):
    def get(self,request):
        list_sell_return=List_Sell_Return.objects.all()
        serializer=List_Sell_Return_Serializer(list_sell_return,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=List_Sell_Return_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class List_Sell_Return_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return List_Sell_Return.objects.get(p_k=pk)
        except List_Sell_Return.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Sell_Return_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Sell_Return_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class Shipments_Api_List(APIView):
    def get(self,request):
        shipment=Shipments.objects.all()
        serializer=Shipments_Serializer(shipment,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Shipments_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Shipments_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Shipments.objects.get(p_k=pk)
        except Shipments.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Shipments_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Shipments_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Discount_Api_List(APIView):
    def get(self,request):
        discount=Discount.objects.all()
        serializer=Discount_Serializer(discount,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Discount_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Discount_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Discount.objects.get(p_k=pk)
        except Discount.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Discount_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Discount_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        return Response(status=status.HTTP_204_NO_CONTENT)




class All_Sales_Searh_Api(generics.ListCreateAPIView):
    search_fields = ['Created_At','Invoice_No','Contact_Number','Payment_Status','Payment_Method','Total_Amount','Total_Paid','Sell_Due','Sell_Return_Due','Shipping_Status','Shipping_Address','Total_Items','Added_By']
    filter_backends = (filters.SearchFilter,)
    queryset = All_Sales.objects.all()
    serializer_class = All_Sales_Serializer

class List_Sell_Return_Searh_Api(generics.ListCreateAPIView):
    search_fields = ['Created_At','Invoice_No','Parent_Sale','Contact_Number','Payment_Status','Total_Amount','Payment_Due']
    filter_backends = (filters.SearchFilter,)
    queryset = List_Sell_Return.objects.all()
    serializer_class = List_Sell_Return_Serializer

class List_Draft_Searh_Api(generics.ListCreateAPIView):
    search_fields = ['Created_At','Reference_No','Contact_Number','Total_Items','Added_By']
    filter_backends = (filters.SearchFilter,)
    queryset = List_Draft.objects.all()
    serializer_class = List_Draft_Serializer

class Shipment_Searh_Api(generics.ListCreateAPIView):
    search_fields = ['Created_At','Invoice_No','Contact_Number','Shipping_Status','Payment_Status','Service_Staff']
    filter_backends = (filters.SearchFilter,)
    queryset = Shipments.objects.all()
    serializer_class = Shipments_Serializer

class Discount_Searh_Api(generics.ListCreateAPIView):
    search_fields = ['Starts_At','Ends_At','Discount_Amount','Priority','Brand','Category','Product']
    filter_backends = (filters.SearchFilter,)
    queryset = Discount.objects.all()
    serializer_class = Discount_Serializer

class Location_Search_Api(generics.ListCreateAPIView):
    search_fields = ['Location']
    filter_backends = (filters.SearchFilter,)
    queryset =Location_Set.objects.all()
    serializer_class = Location_Set_Serializer