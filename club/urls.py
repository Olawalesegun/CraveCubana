from django.urls import path
from club.views import customers_list, customers_details

urlpatterns = [
    path('list/', customers_list, name='customers-list'),
    path('<int:pk>', customers_details, name='customers-details')
]