from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    hello = 'Hello world from view'
    context = {
        'hello': hello,
        'form': form
    }
    return render(request, 'sales/home.html', context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    #context_object_name = 'another_name_object_as_param'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
"""
This a function view approach. 
def sale_list_view(request): # use it instead of ListView
    qs = Sale.objects.all()
    return render(request, 'sales/main.html',{"object_list": qs})

def sale_detail_view(request, pk): # use it instead of DetailView
    obj = Sale.objects.get(pk=pk)
    # or
    # obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {"object":obj})
"""