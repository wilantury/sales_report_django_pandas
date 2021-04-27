from django.shortcuts import render

def home_view(request):
    hello = 'Hello world from view'
    return render(request, 'sales/main.html', {'hello': hello})
