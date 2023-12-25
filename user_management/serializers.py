# in user_management/serializers.py
from rest_framework import serializers
from .models import CustomUser,Roles,Adds,Sales_Commission_Ager
from django.contrib.auth.models import Group, Permission

class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = CustomUser
        fields = ('id','first_name', 'last_name','email','mobile_number','position', 'image','password', 'confirm_password','is_active','Role','Sales_Commission_Percentage','Max_Sales_Discount_Percentage','contact','Date_Of_Birth','Gender','Marital_Status','Blood_Group','Phone_Number','Alternate_Contact_Number','Family_Contact_Number','Facebook_Link','Twitter_Link','Permanent_Address','Current_Address','Account_Holders_Name','Account_Number','Bank_Name','Bank_Identifier_Code','Branch','Tax_Payer_ID','Basic_Salary','Basic_Salary','Pay_Term','Pay_Components')
        #fields=('__all__')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def update(self, instance, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        instance = super().update(instance, validated_data)

        if 'password' in validated_data and validated_data['password']:
            instance.set_password(validated_data['password'])
            instance.save()

        return instance
        


class Roles_All_Show_Serailizer(serializers.ModelSerializer):
    groups=serializers.SlugRelatedField(
        slug_field='name',
        queryset=Group.objects.all(),
        many=True
        )
    user_permissions=serializers.SlugRelatedField(
        slug_field="name",
        queryset=Permission.objects.all(),
        many=True
        )

    class Meta:
        model=Roles
        fields=('__all__')
        
class Roles_Serailizer(serializers.ModelSerializer):

    class Meta:
        model=Roles
        fields=('__all__')


class Sales_Commission_Ager_Serailizer(serializers.ModelSerializer):
    class Meta:
        model=Sales_Commission_Ager
        fields=('__all__')

class Adds_Serailizer(serializers.ModelSerializer):
    class Meta:
        model=Adds
        fields=('__all__')
