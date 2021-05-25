# Django
from django.shortcuts import render

# Models
from .models import Profile

# Forms
from .forms import ProfileForm

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if form.is_valid():
        form.save()
        confirm = True
    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profiles/main.html', context)
