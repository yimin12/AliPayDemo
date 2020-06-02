#coding=utf-8
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index_veiw),
    path('topay/',views.pay_view),
    path('checkPay/',views.checkPay_view),
]