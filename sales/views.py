# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Models
from .models import Sale
# Forms
from .forms import SalesSearchForm
# Pandas
import pandas as pd
# utils
from .utils import get_customer_from_id, get_salesman_from_id, get_chart

def home_view(request):
    sales_df = None
    positions_df = None
    merged_df = None
    df = None
    chart = None
    form = SalesSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
    
        # qs = Sale.objects.all()
        sale_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)

        if len(sale_qs) > 0:
            #obj = Sale.objects.get(id=1)
            # print(obj)
            # print(qs.values())
            # print(qs.values_list())
            positions_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        'sales_id': sale.id # pos.get_sales_id()
                    }
                    positions_data.append(obj)
            sales_df = pd.DataFrame(sale_qs.values())
            sales_df['customer_id'] = sales_df['customer_id'].apply(get_customer_from_id)
            sales_df['salesman_id'] = sales_df['salesman_id'].apply(get_salesman_from_id)
            sales_df.rename({'customer_id':'Customer', 'salesman_id':'Salesman', 'id':'sales_id'}, axis=1, inplace=True)
            sales_df['created'] = sales_df['created'].apply(lambda date: date.strftime('%Y/%m/%d'))
            sales_df['updated'] = sales_df['updated'].apply(lambda date: date.strftime('%Y/%m/%d'))

            # sales_df['new_col'] = sales_df['Sales_id']
            positions_df = pd.DataFrame(positions_data)

            merged_df = pd.merge(sales_df, positions_df, on='sales_id')
            df = merged_df.groupby('transaction_id', as_index=False)['price'].agg(sum)
            
            chart = get_chart(chart_type, df, labels=df['transaction_id'].values)
            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()
        

        else:
            print('no data')



    context = {
        'form': form,
        'sales_df': sales_df,
        'positions_df':positions_df,
        'merged_df':merged_df,
        'df':df,
        'chart': chart
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