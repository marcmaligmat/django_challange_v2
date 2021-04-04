from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Account(models.Model):
    customer = models.ForeignKey(Customer, 
                                 related_name='account', 
                                 on_delete=models.CASCADE
                            )
    balance = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.customer.name} account id: {self.id}"


class Transfer(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE)
    receiver = models.IntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
