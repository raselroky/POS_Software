from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import All_Reports
from .serializers import All_Reports_Serializer
from contact.models import Customers,Suppliers,Customer_Group
from purchase.models import Purchases,List_Purchase_Return
from sell.models import List_Draft,All_Sales,Discount,Shipments


class All_Reports_Api(APIView):
    def get(self,request):
        total=All_Reports()

        total_supplier_opening_balance_due_data=Suppliers.objects.values_list('Opening_Balance_Due',flat=True)
        total_supplier_opening_balance_due_data_int=str(sum(list(map(int,total_supplier_opening_balance_due_data))))
        #print(total_supplier_opening_balance_due_data_int)

        total_supplier_due_data=Suppliers.objects.values_list('Due_Amount',flat=True)
        total_supplier_due_data_int=str(sum(list(map(int,total_supplier_due_data))))
        #print(total_supplier_due_data_int)

        total_customer_opening_balance_due_data=Customers.objects.values_list('Opening_Balance_Due',flat=True)
        total_customer_opening_balance_due_data_int=str(sum(list(map(int,total_customer_opening_balance_due_data))))
        #print(total_customer_opening_balance_due_data_int)

        total_customer_due_data=Customers.objects.values_list('Total_Sale_Due',flat=True)
        total_customer_due_data_int=str(sum(list(map(int,total_customer_due_data))))
        #print(total_customer_due_data_int)

        total_purchase_data=Purchases.objects.values_list('Grand_Total',flat=True)
        total_purchase_data_int=str(sum(list(map(int,total_purchase_data))))
        #print(total_purchase_data_int)

        total_product_item_data=All_Sales.objects.values_list('Total_Items',flat=True)
        total_product_item_int=str(sum(list(map(int,total_product_item_data))))
        #print(total_product_item_int)

        total_sell_return_due_data=All_Sales.objects.values_list('Sell_Return_Due',flat=True)
        total_sell_return_due_int=str(sum(list(map(int,total_sell_return_due_data))))
        #print(total_sell_return_due_int)

        


        total.Total_Supplier_Opening_Balance_Due=total_supplier_opening_balance_due_data_int
        total.Total_Supplier_Due=total_supplier_due_data_int
        total.Total_Customer_Opening_Balance_Due=total_customer_opening_balance_due_data_int
        total.Total_Customer_Due=total_customer_due_data_int
        total.Total_Purchase=total_purchase_data_int
        total.Total_Products_Item=total_product_item_int
        total.Total_Sell_Return=total_sell_return_due_int

        total.save()
        tt=All_Reports.objects.values_list('p_k',flat=True)
        tt0=list(map(int,tt))
        print(tt0,'tt0')
        ttm=max(list(tt0))
        print(ttm,"tt1m")

        tt2=All_Reports.objects.get(p_k=ttm)
        sd=All_Reports_Serializer(tt2)
        
        
        
        return Response(sd.data)
    
    def post(slef,request):
        serializer=All_Reports_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"Message":"Successfully Created"})
        return Response({"Error":"check safely"})
        

        
















        reports=All_Reports.objects.all()
        serializer=All_Reports_Serializer(reports,many=True)
        return Response(serializer.data)
    