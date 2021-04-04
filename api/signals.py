# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from api.models import Account, Customer


# @receiver(post_save, sender=Customer)
# def create_account(sender, instance, created, **kwargs):

#     if created:
#         account_created = Account.objects.create(
#             customer=instance,
#             balance=instance.initial_deposit
#         )
