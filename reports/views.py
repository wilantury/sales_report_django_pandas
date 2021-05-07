# Django
from django.shortcuts import render
from django.http import JsonResponse
# Models
from profiles.models import Profile
from .models import Report
# Forms
from .forms import ReportForm
# utils
from .utils import get_report_image

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
