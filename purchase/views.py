from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Purchases,Add_Purchase,List_Purchase_Return
from .serializers import Purchases_Serializer,Add_Purchases_Serializer,List_Purchase_Return_Serializer
from django.http import Http404
from rest_framework import status


class Purchases_Api_List(APIView):
    def get(self,request):
        purchase=Purchases.objects.all()
        serializer=Purchases_Serializer(purchase,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Purchases_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Purchase_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Purchases.objects.get(p_k=pk)
        except Purchases.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchases_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchases_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Add_Purchases_Api_List(APIView):
    def get(self,request):
        add_purchase=Add_Purchase.objects.all()
        serializer=Add_Purchases_Serializer(add_purchase,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Add_Purchases_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Add_Purchase_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Add_Purchase.objects.get(p_k=pk)
        except Add_Purchase.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Add_Purchases_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Add_Purchases_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class List_Purchase_Return_Api_List(APIView):
    def get(self,request):
        list_purchase_return=List_Purchase_Return.objects.all()
        serializer=List_Purchase_Return_Serializer(list_purchase_return,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=List_Purchase_Return_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class List_Purchase_Return_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return List_Purchase_Return.objects.get(p_k=pk)
        except List_Purchase_Return.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Purchase_Return_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = List_Purchase_Return_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class Purchase_Filter_Api(APIView):
    def post(self,request):
        Supplier=request.data['Supplier']
        Location=request.data['Location']

        purchase=Purchases.objects.filter(Supplier=Supplier,Location=Location)
        serializer=Purchases_Serializer(purchase,many=True)
        return Response(serializer.data)

