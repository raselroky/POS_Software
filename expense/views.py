# views.py
from rest_framework import generics
from .models import ExpenseCategory, ExpenseSubcategory
from .serializers import ExpenseCategorySerializer, ExpenseSubcategorySerializer
from .models import Expense,Payment
from .serializers import ExpenseSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from datetime import timedelta


class ExpenseCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class ExpenseSubcategoryListCreateView(generics.ListCreateAPIView):
    queryset = ExpenseSubcategory.objects.all()
    serializer_class = ExpenseSubcategorySerializer

class ExpenseSubcategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpenseSubcategory.objects.all()
    serializer_class = ExpenseSubcategorySerializer


# views.py
from rest_framework import generics
from .models import Payment, Expense
from .serializers import PaymentSerializer, ExpenseSerializer


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset = Expense.objects.all()

        business_location = self.request.query_params.get('business_location')
        expense_for = self.request.query_params.get('expense_for')
        contact = self.request.query_params.get('contact')
        expense_category = self.request.query_params.get('expense_category')
        sub_category = self.request.query_params.get('sub_category')
        date_range = self.request.query_params.get('date_range')
        payment_status = self.request.query_params.get('payment_status')

        # Filter by Business Location
        if business_location:
            queryset = queryset.filter(business_location=business_location)

        # Filter by Expense For (User)
        if expense_for:
            queryset = queryset.filter(expense_for__username=expense_for)

        # Filter by Contact (assuming you have a contact field in your Expense model)
        if contact:
            queryset = queryset.filter(expense_for_contact__name=contact)

        # Filter by Expense Category (assuming you have a category field in your Expense model)
        if expense_category:
            queryset = queryset.filter(category=expense_category)

        # Filter by Sub Category (assuming you have a sub_category field in your Expense model)
        if sub_category:
            queryset = queryset.filter(sub_category=sub_category)

        # Filter by Date Range
        if date_range == 'today':
            start_date = datetime.now().date()
            end_date = start_date + timedelta(days=1)
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'yesterday':
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=1)
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'last7days':
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=7)
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'last30days':
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=30)
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'this_month':
            start_date = datetime.now().date().replace(day=1)
            end_date = timezone.now().date()
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'this_month_last_year':
            end_date = datetime.now().date().replace(day=1)
            start_date = end_date - timedelta(days=365)
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'this_year':
            start_date = datetime.now().date().replace(month=1, day=1)
            end_date = timezone.now().date()
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'last_year':
            end_date = datetime.now().date().replace(month=1, day=1)
            start_date = end_date - timedelta(days=365)
            queryset = queryset.filter(date__range=[start_date, end_date])

        elif date_range == 'current_financial_year':
            # Assuming your financial year starts from April 1st
            today = timezone.now().date()
            start_date = today.replace(month=4, day=1)
            end_date = today.replace(month=3, day=31) + timedelta(days=1)
            queryset = queryset.filter(date__range=[start_date, end_date])

        # Add similar filters for other date ranges

        # Filter by Payment Status
        if payment_status:
            queryset = queryset.filter(payment_status=payment_status)

        return queryset



class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Update the related payments
        payments_data = request.data.get('payments', [])
        for payment_data in payments_data:
            payment_id = payment_data.get('id', None)
            if payment_id:
                payment = instance.payments.get(id=payment_id)
                payment.amount = payment_data.get('amount', payment.amount)
                payment.date = payment_data.get('date', payment.date)
                payment.method = payment_data.get('method', payment.method)
                payment.payment_account = payment_data.get('payment_account', payment.payment_account)
                payment.card_number = payment_data.get('card_number', payment.card_number)
                payment.card_holder_name = payment_data.get('card_holder_name', payment.card_holder_name)
                payment.card_transaction_no = payment_data.get('card_transaction_no', payment.card_transaction_no)
                payment.card_type = payment_data.get('card_type', payment.card_type)
                payment.card_expiry_month = payment_data.get('card_expiry_month', payment.card_expiry_month)
                payment.card_expiry_year = payment_data.get('card_expiry_year', payment.card_expiry_year)
                payment.card_security_code = payment_data.get('card_security_code', payment.card_security_code)
                payment.cheque_no = payment_data.get('cheque_no', payment.cheque_no)
                payment.bank_account_no = payment_data.get('bank_account_no', payment.bank_account_no)
                payment.other = payment_data.get('other', payment.other)
                payment.payment_note = payment_data.get('payment_note', payment.payment_note)
                # ... update other payment fields as needed ...
                payment.save()
            else:
                Payment.objects.create(expense=instance, **payment_data)

        self.perform_update(serializer)

        instance.payment_due = max(0, instance.total_amount - sum(payment.amount for payment in instance.payments.all()))
        if instance.payment_due == 0:
            instance.payment_status = 'paid'
        elif instance.payment_due == instance.total_amount:
            instance.payment_status = 'due'
        else:
            instance.payment_status = 'partial'

        instance.save()

        return Response(serializer.data)