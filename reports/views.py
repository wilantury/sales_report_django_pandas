# Django
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
# libraries
from xhtml2pdf import pisa
# Models
from profiles.models import Profile
from .models import Report
# Forms
from .forms import ReportForm
# utils
from .utils import get_report_image

class ReportListView(ListView):
    model = Report
    template_name = 'reports/main.html'

class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/detail.html'

def create_report_view(request):
    if request.is_ajax():
        """a way to save the data into database, using the Models object"""
        # name = request.POST.get('name')
        # remarks = request.POST.get('remarks')
        # image = request.POST.get('image')
        # img = get_report_image(image)
        # author = Profile.objects.get(user=request.user)
        # Report.objects.create(name=name, remarks=remarks, image=img, author=author)
        
        """another way to save the data into database, using Forms Models object"""
        form = ReportForm(request.POST or None)
        image = request.POST.get('image')
        img = get_report_image(image)        
        author = Profile.objects.get(user=request.user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = img
            instance.author = author
            instance.save()

        return JsonResponse({'data':'send'})
    return JsonResponse({'res':'No ajax request'})

def render_pdf_view(request, pk):
    template_path = 'reports/pdf.html'
    obj = get_object_or_404(Report, pk=pk)
    context = {'obj': obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # Download file
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Display into browser
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response