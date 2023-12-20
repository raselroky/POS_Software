# serializers.py
from rest_framework import serializers
from .models import ExpenseCategory, ExpenseSubcategory
from .models import Expense

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

class ExpenseSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseSubcategory
        fields = '__all__'






# serializers.py
from rest_framework import serializers
from .models import Payment, Expense

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','amount', 'date', 'method', 'payment_account', 
                  'card_number', 'card_holder_name', 'card_transaction_no',
                  'card_type', 'card_expiry_month', 'card_expiry_year', 
                  'card_security_code', 'cheque_no', 'bank_account_no',
                  'other', 'payment_note']

class ExpenseSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True)

    class Meta:
        model = Expense
        fields = ['id','reference_no', 'date', 
                  'expense_for', 'expense_for_contact',
                  'attached_document', 'applicable_tax',
                  'total_amount', 'is_refund', 'expense_note',
                  'is_recurring', 'recurring_interval', 'number_of_receipts',
                  'payment_due', 'payment_status', 'payments']

    def create(self, validated_data):
        payments_data = validated_data.pop('payments', [])
        expense = Expense.objects.create(**validated_data)
        if not expense.reference_no:
            expense.reference_no = f"REF-{expense.id}"
            expense.save()
        # Calculate payment_due and payment_status
        expense.payment_due = max(0, expense.total_amount - sum(payment_data['amount'] for payment_data in payments_data))
        if expense.payment_due == 0:
            expense.payment_status = 'paid'
        elif expense.payment_due == expense.total_amount:
            expense.payment_status = 'due'
        else:
            expense.payment_status = 'partial'

        # Save the Expense instance with updated payment_due and payment_status
        expense.save()

        # Create and associate payments with the expense
        for payment_data in payments_data:
            Payment.objects.create(expense=expense, **payment_data)

        return expense
    
    


    def update(self, instance, validated_data):
        payments_data = validated_data.pop('payments', [])
        payments = list(instance.payments.all())

        # Explicitly update each field in the Expense instance
        instance.reference_no = validated_data.get('reference_no', instance.reference_no)
        instance.business_location = validated_data.get('business_location', instance.reference_no)
        instance.date = validated_data.get('date', instance.date)
        instance.expense_for = validated_data.get('expense_for', instance.expense_for)
        instance.expense_for_contact = validated_data.get('expense_for_contact', instance.expense_for_contact)
        instance.attached_document = validated_data.get('attached_document', instance.attached_document)
        instance.applicable_tax = validated_data.get('applicable_tax', instance.applicable_tax)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.is_refund = validated_data.get('is_refund', instance.is_refund)
        instance.expense_note = validated_data.get('expense_note', instance.expense_note)
        instance.is_recurring = validated_data.get('is_recurring', instance.is_recurring)
        instance.recurring_interval = validated_data.get('recurring_interval', instance.recurring_interval)
        instance.recurring_interval_value = validated_data.get('recurring_interval_value', instance.recurring_interval_value)
        instance.number_of_receipts = validated_data.get('number_of_receipts', instance.number_of_receipts)

        instance.payment_due = validated_data.get('payment_due', instance.payment_due)
        instance.payment_status = validated_data.get('payment_status', instance.payment_status)

        instance.save()

        for payment_data in payments_data:
            payment = payments.pop(0) if payments else None
            if payment:
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

        return instance
