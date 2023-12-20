from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from smss.models import All_Number


class User_Api_List(APIView):
    def get(self,request):
        usr=CustomUser.objects.all()
        serializer=CustomUserSerializer(usr,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=CustomUserSerializer(data=request.data)
        if(serializer.is_valid()):
            p1=request.data['password']
            p2=request.data['confirm_password']

            if(p1!=p2):
                return Response({"Message":"Password did not matched!"})
            if(len(str(p1))<5 and len(str(p2))<5):
                return Response({"Message":"Password Too short! try Again."})
            if(any(map(str.isdigit, p1))==False or any(map(str.isalpha, p1))==False):
                return Response({"Message":"Character or Number missing ,try again!"})

            serializer.save()
            number=All_Number()
            number.Number=serializer.data['mobile_number']
            number.save()
            return Response({"Message":"Successfully Registration complete!"})
        
        return Response({"error":"Not valid!"})

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
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        
