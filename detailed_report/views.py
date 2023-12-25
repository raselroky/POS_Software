from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Purchases,Sale_Purchase,Due_Amount,Sales,Supplier_And_Customer_Report,Input_Tax,Output_Tax,Expense_Tax,Customer_Group_Report,Stock_Adjustment_Report,Item_Report,Product_Purchase_Report,Product_Sell_Report,Purchase_Payment_Report,Sell_Payment_Report,Expense_Report,Register_Report,Sales_Report_Added,Sales_Report_With_Commission,Sales_Report_Expense,Stock_Report,Expense_Categories_List
from . serializers import Purchase_Serializer,Sale_Purchase_Serializer,Due_Amount_Serializer,Sales_Serializer,Supplier_And_Customer_Report_Serializer,Input_Tax_Serializer,Output_Tax_Serializer,Expense_Tax_Serializer,Customer_Group_Report_Serializer,Stock_Adjustment_Report_Serializer,Item_Report_Serializer,Product_Purchase_Report_Serializer,Product_Sell_Report_Serializer,Purchase_Payment_Report_Serializer,Sell_Payment_Report_Serializer,Expense_Report_Serializer,Register_Report_Serializer,Sales_Report_Added_Serializer,Sales_Report_With_Commission_Serializer,Sales_Report_Expense_Serializer,Stock_Report_Serializer,Expense_Categories_List_Serializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import filters


class Purchases_Api_List(APIView):
    def get(slef,request):
        purchase=Purchases.objects.all()
        serializer=Purchase_Serializer(purchase,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Purchase_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Purchases_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Purchases.objects.get(p_k=pk)
        except Purchases.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchase_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchase_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class Sales_Api_List(APIView):
    def get(slef,request):
        sales=Sales.objects.all()
        serializer=Sales_Serializer(sales,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Sales_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sales_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Sales.objects.get(p_k=pk)
        except Sales.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Sale_Purchase_Api_List(APIView):
    def get(slef,request):
        sale_purchase=Sale_Purchase.objects.all()
        serializer=Sale_Purchase_Serializer(sale_purchase,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Sale_Purchase_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sale_Purchase_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Sale_Purchase.objects.get(p_k=pk)
        except Sale_Purchase.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sale_Purchase_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sale_Purchase_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Due_Amount_Api_List(APIView):
    def get(slef,request):
        due_amount=Due_Amount.objects.all()
        serializer=Due_Amount_Serializer(due_amount,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Due_Amount_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Due_Amount_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Due_Amount.objects.get(p_k=pk)
        except Due_Amount.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Due_Amount_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Due_Amount_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Input_Tax_Api_List(APIView):
    def get(self,request):
        input_tax=Input_Tax.objects.all()
        serializer=Input_Tax_Serializer(input_tax,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Input_Tax_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Input_Tax_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Input_Tax.objects.get(p_k=pk)
        except Input_Tax.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Input_Tax_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Input_Tax_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Output_Tax_Api_List(APIView):
    def get(self,request):
        output_tax=Output_Tax.objects.all()
        serializer=Output_Tax_Serializer(output_tax,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Output_Tax_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Output_Tax_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Output_Tax.objects.get(p_k=pk)
        except Output_Tax.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Output_Tax_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Output_Tax_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Expense_Tax_Api_List(APIView):
    def get(self,request):
        expense_tax=Expense_Tax.objects.all()
        serializer=Expense_Tax_Serializer(expense_tax,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Expense_Tax_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Expense_Tax_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Expense_Tax.objects.get(p_k=pk)
        except Expense_Tax.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Expense_Tax_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Expense_Tax_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Supplier_And_Customer_Report_Api_List(APIView):
    def get(slef,request):
        supplier_and_customer=Supplier_And_Customer_Report.objects.all()
        serializer=Supplier_And_Customer_Report_Serializer(supplier_and_customer,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Supplier_And_Customer_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Supplier_And_Customer_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Supplier_And_Customer_Report.objects.get(p_k=pk)
        except Supplier_And_Customer_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Supplier_And_Customer_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Supplier_And_Customer_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Customer_Group_Report_Api_List(APIView):
    def get(self,request):
        customer_group_report=Customer_Group_Report.objects.all()
        serializer=Customer_Group_Report_Serializer(customer_group_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Customer_Group_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Customer_Group_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Customer_Group_Report.objects.get(p_k=pk)
        except Customer_Group_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customer_Group_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Customer_Group_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Stock_Adjustment_Report_Api_List(APIView):
    def get(self,request):
        stock_adjustment_report=Stock_Adjustment_Report.objects.all()
        serializer=Stock_Adjustment_Report_Serializer(stock_adjustment_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Stock_Adjustment_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Stock_Adjustment_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Stock_Adjustment_Report.objects.get(p_k=pk)
        except Stock_Adjustment_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Adjustment_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Adjustment_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Item_Report_Api_List(APIView):
    def get(self,request):
        item_report=Item_Report.objects.all()
        serializer=Item_Report_Serializer(item_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Item_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Item_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Item_Report.objects.get(p_k=pk)
        except Item_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Item_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Item_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Product_Purchase_Report_Api_List(APIView):
    def get(self,request):
        product_purchase_report=Product_Purchase_Report.objects.all()
        serializer=Product_Purchase_Report_Serializer(product_purchase_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Product_Purchase_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Product_Purchase_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Product_Purchase_Report.objects.get(p_k=pk)
        except Product_Purchase_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Product_Purchase_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Product_Purchase_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Product_Sell_Report_Api_List(APIView):
    def get(self,request):
        product_sell_report=Product_Sell_Report.objects.all()
        serializer=Product_Sell_Report_Serializer(product_sell_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Product_Sell_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Product_Sell_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Product_Sell_Report.objects.get(p_k=pk)
        except Product_Sell_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Product_Sell_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Product_Sell_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Purchase_Payment_Report_Api_List(APIView):
    def get(self,request):
        purhcase_payment_report=Purchase_Payment_Report.objects.all()
        serializer=Purchase_Payment_Report_Serializer(purhcase_payment_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Purchase_Payment_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Purchase_Payment_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Purchase_Payment_Report.objects.get(p_k=pk)
        except Purchase_Payment_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchase_Payment_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Purchase_Payment_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Sell_Payment_Report_Api_List(APIView):
    def get(self,request):
        sell_payment_report=Sell_Payment_Report.objects.all()
        serializer=Sell_Payment_Report_Serializer(sell_payment_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Sell_Payment_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Sell_Payment_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Sell_Payment_Report.objects.get(p_k=pk)
        except Sell_Payment_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sell_Payment_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sell_Payment_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Expense_Report_Api_List(APIView):
    def get(self,request):
        expense_report=Expense_Report.objects.all()
        serializer=Expense_Report_Serializer(expense_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Expense_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Expense_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Expense_Report.objects.get(p_k=pk)
        except Expense_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Expense_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Expense_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Register_Report_Api_List(APIView):
    def get(self,request):
        register_report=Register_Report.objects.all()
        serializer=Register_Report_Serializer(register_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Register_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Register_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Register_Report.objects.get(p_k=pk)
        except Register_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Register_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Register_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Sales_Report_Added_Api_List(APIView):
    def get(self,request):
        sales_report_added=Sales_Report_Added.objects.all()
        serializer=Sales_Report_Added_Serializer(sales_report_added,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Sales_Report_Added_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sales_Report_Added_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Sales_Report_Added.objects.get(p_k=pk)
        except Sales_Report_Added.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Report_Added_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Report_Added_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Sales_Report_With_Commission_Api_List(APIView):
    def get(self,request):
        sales_report_with_commission=Sales_Report_With_Commission.objects.all()
        serializer=Sales_Report_With_Commission_Serializer(sales_report_with_commission,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Sales_Report_With_Commission_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sales_Report_With_Commission_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Sales_Report_With_Commission.objects.get(p_k=pk)
        except Sales_Report_With_Commission.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Report_With_Commission_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Report_With_Commission_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Sales_Report_Expense_Api_List(APIView):
    def get(self,request):
        sales_report_expense=Sales_Report_Expense.objects.all()
        serializer=Sales_Report_Expense_Serializer(sales_report_expense,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Sales_Report_Expense_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sales_Report_Expense_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Sales_Report_Expense.objects.get(p_k=pk)
        except Sales_Report_Expense.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Report_Expense_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Sales_Report_Expense_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Stock_Report_Api_List(APIView):
    def get(self,request):
        stock_report=Stock_Report.objects.all()
        serializer=Stock_Report_Serializer(stock_report,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Stock_Report_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Stock_Report_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Stock_Report.objects.get(p_k=pk)
        except Stock_Report.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Report_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Stock_Report_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Expense_Categories_List_Api_List(APIView):
    def get(self,request):
        expense_categories_list=Expense_Categories_List.objects.all()
        serializer=Expense_Categories_List_Serializer(expense_categories_list,many=True)
        return Response(serializer.data)
    def post(slef,request):
        serializer=Expense_Categories_List_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Expense_Categories_List_Api_Detail(APIView):
    def get_object(self, pk):
        try:
            return Expense_Categories_List.objects.get(p_k=pk)
        except Expense_Categories_List.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Expense_Categories_List_Serializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = Expense_Categories_List_Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Expense_Categories_Search_Api(generics.ListCreateAPIView):
    search_fields=[]
    filter_backends=(filters.SearchFilter,)
    