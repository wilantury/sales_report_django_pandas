# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Models
from .models import Sale
# Forms
from .forms import SalesSearchForm
# Pandas
import pandas as pd

def home_view(request):
    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
    
        # qs = Sale.objects.all()
        qs = Sale.objects.filter(created__date=date_from)
        #obj = Sale.objects.get(id=1)
        # print(qs)
        # print(obj)
        # print(qs.values())
        # print(qs.values_list())
        print("#"*20)
        df1 = pd.DataFrame(qs.values())
        print(df1)
        print("#"*20)
        # df2 = pd.DataFrame(qs.values_list())
        # print(df2)
        #print("#"*20)



    context = {
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
This is a function view approach. 
def sale_list_view(request): # use it instead of ListView
    qs = Sale.objects.all()
    return render(request, 'sales/main.html',{"object_list": qs})

def sale_detail_view(request, pk): # use it instead of DetailView
    obj = Sale.objects.get(pk=pk)
    # or
    # obj = get_object_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {"object":obj})
"""