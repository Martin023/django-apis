from django import views
from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/merch/', views.MerchList.as_view()),

    ## sttting the path to our authentication token.
    path('api-token-auth/', obtain_auth_token ),
    path('api/merch/merch-id/<pk>/', views.MerchDescription.as_view())
]
