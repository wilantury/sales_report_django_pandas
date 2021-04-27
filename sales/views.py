from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale

def home_view(request):
    hello = 'Hello world from view'
    return render(request, 'sales/home.html', {'hello': hello})

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    #context_object_name = 'another_name_object_as_param'
