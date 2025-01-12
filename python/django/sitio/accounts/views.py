from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Profile
from django.http import HttpResponse

# Create your views here.

@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/profile_list.html', {'profiles': profiles})

@login_required
def profile_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            Profile.objects.create(name=name, email=email)
            return redirect('profile_list')  # Redirige a la lista de perfiles
        else:
            return HttpResponse("Name and Email are required", status=400)
    return render(request, 'accounts/profile_create.html')

@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')
        if profile.name and profile.email:
            profile.save()
            return redirect('profile_list')  # Redirige a la lista de perfiles
        else:
            return HttpResponse("Name and Email are required", status=400)

    return render(request, 'accounts/profile_edit.html', {'profile': profile})

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')  # Redirige a la lista de perfiles

    return render(request, 'accounts/profile_delete.html', {'profile': profile})