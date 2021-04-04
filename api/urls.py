from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.serializers import CustomerSerializer
from api.views import (AccountTransferAPIView,
                       AccountAPI, CustomerAPI, TransferAPI)

router = DefaultRouter()
router.register("customers", CustomerAPI)
router.register("accounts", AccountAPI)
router.register("transfers", TransferAPI)

urlpatterns = [
    path("", include(router.urls)),
    path("accounts/<int:pk>/transfers/",
         AccountTransferAPIView.as_view(),
         name="account-transfer"),

]
