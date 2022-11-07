from django.shortcuts import render
from club.models import Customers
from django.http import JsonResponse

# Create your views here.
def customers_list(request):
    users = Customers.objects.all()
    data = {
        'user': list(users.values())
        }
    return JsonResponse(data)

def customers_details(request, pk):
    customer = Customers.objects.get(pk=pk)
    data = {
        'name': customer.c_name,
        'seat': customer.seat_no
    }
    return JsonResponse(data)
