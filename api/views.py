import decimal

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

from api.models import Account, Customer, Transfer
from api.serializers import (AccountSerializer, CustomerSerializer,
                             TransferSerializer)


class CustomerAPI(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        customer = Customer.objects.create(name=self.request.data['name'])
        if customer:
            Account.objects.create(
                customer=customer,
                balance=self.request.data['initial_deposit']
            )


class AccountAPI(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransferAPI(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def perform_create(self, serializer):
        sender_account_pk = self.request.data['sender']
        receiver_account_pk = self.request.data['receiver']
        amount = decimal.Decimal(self.request.data['amount'])

        sender_account = get_object_or_404(Account, pk=sender_account_pk)
        receiver_account = get_object_or_404(Account, pk=receiver_account_pk)

        if(receiver_account_pk == sender_account_pk):
            raise ValidationError("Cannot send the same account")

        if(amount > sender_account.balance):
            raise ValidationError("Sender Has Insufficient Funds!")

        transfer_successful = serializer.save(
            sender=sender_account,
            receiver=int(receiver_account.id),
            amount=amount
        )

        if transfer_successful:
            sender_account.balance -= amount
            receiver_account.balance += amount
            if (sender_account.save() == False
                    or receiver_account.save() == False):
                transfer_successful.delete()


class AccountTransferAPIView(generics.ListAPIView):
    serializer_class = TransferSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        print(pk)
        return Transfer.objects.all().filter(sender__pk=pk)
