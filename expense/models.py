# models.py
from django.db import models
from contact.models import Customers
from django.conf import settings 


class ExpenseSubcategory(models.Model):
    subcategory_name = models.CharField(max_length=200)

class ExpenseCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_code = models.CharField(max_length=200)
    subcategory = models.ForeignKey(ExpenseSubcategory, on_delete=models.CASCADE, blank=True, null=True)


# models.py
from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    business_location = models.CharField(max_length=100, blank=True, null=True, unique=True)
    reference_no = models.CharField(max_length=100, blank=True, null=True, unique=True)
    date = models.DateTimeField()
    expense_for = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expenses',
    )
    expense_for_contact = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    attached_document = models.FileField(upload_to='expense_documents/', blank=True, null=True)
    applicable_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_refund = models.BooleanField(default=False)
    expense_note = models.TextField(blank=True, null=True)
    is_recurring = models.BooleanField(default=False)
    recurring_interval = models.CharField(max_length=50, choices=[
        ('Years', 'Years'),
        ('Months', 'Months'),
        ('Days', 'Days'),
    ])
    recurring_interval_value = models.IntegerField(blank=True, null=True)
    number_of_receipts = models.IntegerField(blank=True, null=True)

    payment_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('due', 'Due'),
        ('partial', 'Partial')
    ], default='due')



    def __str__(self):
        return f"Expense - {self.total_amount} for {self.expense_for}"









    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    method = models.CharField(max_length=50, choices=[
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('bank_transfer', 'Bank Transfer')
    ])

    payment_account = models.CharField(max_length=200, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_holder_name = models.CharField(max_length=200, blank=True, null=True)
    card_transaction_no = models.CharField(max_length=100, blank=True, null=True)
    card_type = models.CharField(max_length=50, choices=[
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
        ('visa', 'Visa Card'),
        ('master', 'Master Card')
    ], blank=True, null=True)
    card_expiry_month = models.IntegerField(blank=True, null=True)
    card_expiry_year = models.IntegerField(blank=True, null=True)
    card_security_code = models.CharField(max_length=4, blank=True, null=True)
    cheque_no = models.CharField(max_length=50, blank=True, null=True)
    bank_account_no = models.CharField(max_length=50, blank=True, null=True)

    other = models.CharField(max_length=200, blank=True, null=True)
    payment_note = models.TextField(blank=True, null=True)   
    expense = models.ForeignKey(Expense, related_name='payments', on_delete=models.CASCADE)

    def __str__(self):
        return "Amount: "+str(self.amount) + " payed by -" + str(self.method)




