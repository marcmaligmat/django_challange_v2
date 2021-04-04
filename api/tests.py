import decimal
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Account, Customer, Transfer
from api.serializers import (AccountSerializer, CustomerSerializer,
                             TransferSerializer)


class AddCustomerTestCase(APITestCase):
    url = reverse("account-list")

    def setUp(self):
        self.customer1 = Customer.objects.create(
            name="test_customer"
        )

    def test_create_customer(self):
        data = {"name": "test_customer", "initial_deposit": 50}
        response = self.client.post('/api/customers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_account(self):
        data = {"customer":1, "balance": 50}
        response = self.client.post('/api/accounts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TransferTestCase(APITestCase):
    def setUp(self):
        c1 = Customer.objects.create(name="sender")
        c2 = Customer.objects.create(name="receiver")

        Account.objects.create(customer=c1,balance = 100)
        Account.objects.create(customer=c2,balance = 50)

    def test_transfer(self):
        sender = Account.objects.get(pk=1)
        receiver = Account.objects.get(pk=2)
        data = {"receiver": receiver.id, "sender": sender.id, "amount": 55.55}
        response = self.client.post("/api/transfers/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        json_response = json.loads(response.content)
        self.assertEqual(
            json_response,
            { "sender": 1, "receiver": 2,  "amount": '55.55'}
        )
        self.sender_balance = Account.objects.get(pk=1).balance
        self.assertEqual(float(self.sender_balance), 44.45)

        self.receiver_balance = Account.objects.get(pk=2).balance
        self.assertEqual(float(self.receiver_balance), 105.55)
