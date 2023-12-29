from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser,Roles,Adds,Sales_Commission_Ager
from .serializers import CustomUserSerializer,Roles_Serailizer,Sales_Commission_Ager_Serailizer,Adds_Serailizer,Roles_All_Show_Serailizer,Permission_Serializer
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from smss.models import All_Number
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
#from multiple_permissions.permissions import IsAuthenticated, IsSuperuser, IsManager
from django.contrib.auth.models import Group, Permission


class User_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomUserSerializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomUserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})

class User_Add_Search_Api(generics.ListCreateAPIView):
    search_fields=['email', 'first_name', 'last_name','mobile_number','position','Sales_Commission_Percentage','Max_Sales_Discount_Percentage','Date_Of_Birth','Gender','Marital_Status','Blood_Group','Phone_Number','Alternate_Contact_Number','Family_Contact_Number','Facebook_Link','Twitter_Link','Permanent_Address','Current_Address','Account_Holders_Name','Account_Number','Bank_Name','Bank_Identifier_Code','Branch','Tax_Payer_ID','Basic_Salary','Pay_Term','Pay_Components']
    filter_backends=(filters.SearchFilter,)
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    paginate_by = 10
    

class Roles_Add_Search_Api(generics.ListCreateAPIView):
    #multiple_permissions = (IsSuperuser, IsManager,IsAuthenticated)
    #exception_class = PermissionError
    #search_fields=['Role']
    #filter_backends=(filters.SearchFilter,)
    queryset=Roles.objects.all()
    serializer_class=Roles_Serailizer
    paginate_by = 10


class Permission_Show_Search_Api(generics.ListAPIView):
    search_fields=['id','codename','name']
    filter_backends=(filters.SearchFilter,)
    
    queryset=Permission.objects.all()
    serializer_class=Permission_Serializer
   


class Roles_Show_Search_Api(generics.ListAPIView):
    search_fields=['Role']
    filter_backends=(filters.SearchFilter,)
    
    queryset=Roles.objects.all()
    serializer_class=Roles_All_Show_Serailizer
    paginate_by = 10

class Roles_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Roles.objects.get(id=pk)
        except Roles.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Roles_Serailizer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Roles_Serailizer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Sales_Commission_Ager_Api_List(generics.ListCreateAPIView):
    search_fields=['Name','Email','Contact_Number','Address','Sales_Commission_Percentage']
    filter_backends=(filters.SearchFilter,)
    queryset=Sales_Commission_Ager.objects.all()
    serializer_class=Sales_Commission_Ager_Serailizer
class Sales_Commission_Ager_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Sales_Commission_Ager.objects.get(id=pk)
        except Sales_Commission_Ager.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Commission_Ager_Serailizer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Commission_Ager_Serailizer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})



class Adds_Api_List(generics.ListCreateAPIView):
    search_fields=['Prefix','First_Name','Last_Name','Email','Contact_Number','Address','Sales_Commission_Percentage']
    filter_backends=(filters.SearchFilter,)
    queryset=Adds.objects.all()
    serializer_class=Adds_Serailizer
class Adds_Api_Detail(APIView):
    def get_object(self,pk):
        try:
            return Adds.objects.get(id=pk)
        except Adds.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Adds_Serailizer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Adds_Serailizer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response({"Message":"Successfully data deleted"})




class Login_Api(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        if(CustomUser.objects.filter(email=email).exists()):
            usr=CustomUser.objects.get(email=email)
            if check_password(password, usr.password):
            #print(usr)
                serializer=CustomUserSerializer(usr)
                return Response(serializer.data['image'])
            else:
                return Response({"Message":"Password Does not Matched"})
            
        return Response({"Message":"Plz register,this username or email does not exist"})
        