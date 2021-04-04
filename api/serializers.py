from rest_framework import serializers

from api.models import Account, Customer, Transfer


class CustomerSerializer(serializers.ModelSerializer):
    initial_deposit = serializers.DecimalField(
        max_digits=6,
        decimal_places=2,
        write_only=True
    )

    class Meta:
        model = Customer
        fields = ["id", "name", "initial_deposit"]


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["customer","balance"]


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ["sender","receiver", "amount"]
