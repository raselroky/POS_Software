from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Suppliers,Customers,Customer_Group,Business_name,Contact_id
from .serializers import Suppliers_Serializer,Customers_Serializer,Customers_Group_Serializer,Business_name_Serializer,Contact_id_Serializer,Suppliers_All_Show_Serializer,Customers_All_Show_Serializer
from .models import Action
from smss.models import All_Number,All_Supplier_Number,All_Customer_Number
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.http import Http404
from rest_framework import status
from rest_framework import filters
from rest_framework import generics

class Suppliers_Api_List(APIView):
    def get(slef,request,format=None):
        suppliers=Suppliers.objects.all()
        serializer=Suppliers_Serializer(suppliers,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=Suppliers_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            number=All_Number()
            number.Number=serializer.data['Mobile']
            number.save()

            numbers=All_Supplier_Number()
            numbers.number=serializer.data['Mobile']
            numbers.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Suppliers_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Suppliers.objects.get(p_k=pk)
        except Suppliers.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Suppliers_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Suppliers_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

    
        
    
class Customers_Api_List(APIView):
    def get(self,request):
        customers=Customers.objects.all()
        serializer=Customers_Serializer(customers,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=Customers_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            number=All_Number()
            number.Number=serializer.data['Mobile']
            number.save()

            numberc=All_Customer_Number()
            numberc.number=serializer.data['Mobile']
            numberc.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Customers_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Customers.objects.get(p_k=pk)
        except Customers.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customers_All_Show_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customers_All_Show_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
    

class Customer_Group_Api_List(APIView):
    def get(self,request):
        customer_group=Customer_Group.objects.all()
        serializer=Customers_Group_Serializer(customer_group,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Customers_Group_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Customer_Group_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Customer_Group.objects.get(p_k=pk)
        except Customer_Group.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customers_Group_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customers_Group_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
            


class Business_name_Api_List(APIView):
    def get(self,request):
        business_name=Business_name.objects.all()
        serializer=Business_name_Serializer(business_name,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Business_name_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Business_name_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Business_name.objects.get(p_k=pk)
        except Business_name.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Business_name_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Business_name_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
    
    

class Contact_id_Api_List(APIView):
    def get(self,request):
        contact_id=Contact_id.objects.all()
        serializer=Contact_id_Serializer(contact_id,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Contact_id_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Contact_id_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Contact_id.objects.get(p_k=pk)
        except Contact_id.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =Contact_id_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Contact_id_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})
    
    

class Action_Api(APIView):
    def post(slef,request):
        action=request.data['action']

        


class Customer_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Name','Email','Mobile','Delivery_Address','Home_Address','Tax_Number','Credit_limit','Reward_Point','Pay_Term','Opening_Balance','Advance_Balance','Total_Sale_Due','Total_Sell_Return_Due','Shipping_Address','Created_At']
    #filter_backends = (filters.SearchFilter,)
    queryset = Customers.objects.all()
    serializer_class = Customers_Serializer
class Customer_All_Show_Api(generics.ListAPIView):
    search_fields = ['Name','Email','Mobile','Delivery_Address','Home_Address','Tax_Number','Credit_limit','Reward_Point','Pay_Term','Opening_Balance','Advance_Balance','Total_Sale_Due','Total_Sell_Return_Due','Shipping_Address','Created_At']
    filter_backends = (filters.SearchFilter,)
    queryset = Customers.objects.all()
    serializer_class = Customers_All_Show_Serializer

class Supplier_Add_Api(generics.ListCreateAPIView):
    #search_fields = ['Name','Email','Address','Mobile','Tax_Number','Pay_Term','Total_Amount','Advance_Amount','Due_Amount','Return_Due_Amount','Created_At']
    #filter_backends = (filters.SearchFilter,)
    queryset = Suppliers.objects.all()
    serializer_class = Suppliers_Serializer
    paginate_by = 10
class Supplier_All_Show_Api(generics.ListAPIView):
    search_fields = ['Name','Email','Address','Mobile','Tax_Number','Pay_Term','Total_Amount','Advance_Amount','Due_Amount','Return_Due_Amount','Created_At']
    filter_backends = (filters.SearchFilter,)
    queryset = Suppliers.objects.all()
    serializer_class = Suppliers_All_Show_Serializer
    paginate_by = 10

class Customer_Group_Search_Api(generics.ListCreateAPIView):
    search_fields = ['Customer_Group_Name','Calculation_Percentage','Selling_Price_Group']
    filter_backends = (filters.SearchFilter,)
    queryset = Customer_Group.objects.all()
    serializer_class = Customers_Group_Serializer

class Business_name_Search_Api(generics.ListCreateAPIView):
    search_fields = ['Business_Name','Category']
    filter_backends = (filters.SearchFilter,)
    queryset = Business_name.objects.all()
    serializer_class = Business_name_Serializer

class Contact_id_Add_Search_Api(generics.ListCreateAPIView):
    search_fields = ['Contact_Ids']
    filter_backends = (filters.SearchFilter,)
    queryset = Contact_id.objects.all()
    serializer_class = Contact_id_Serializer