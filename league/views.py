from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import RegistrationForm
from .models import DriverProfile

# Registration View
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Driver Profile View with role-based access
@login_required
def driver_profile_view(request):
    profile = get_object_or_404(DriverProfile, user=request.user)

    # Role-based access handling
    if profile.role.name == 'Driver':
        return render(request, 'profile_driver.html', {'profile': profile})
    elif profile.role.name == 'FIA':
        return render(request, 'profile_fia.html', {'profile': profile})
    elif profile.role.name == 'Admin':
        return render(request, 'profile_admin.html', {'profile': profile})
    else:
        raise Http404("Invalid role assigned to the profile.")

# Home View
def home_view(request):
    return render(request, 'home.html')

def rules_view(request):
    return render(request, 'rules.html')

def information_view(request):
    return render(request, 'information.html')

# Sample event data
events_data = [
    {"name": "Grand Prix 1", "date": "2024-04-12", "location": "Monaco"},
    {"name": "Grand Prix 2", "date": "2024-04-26", "location": "Silverstone"},
    {"name": "Grand Prix 3", "date": "2024-05-10", "location": "Spa-Francorchamps"},
]

# Calendar View
def calendar_view(request):
    return render(request, 'calendar.html', {'events': events_data})

# Standings
from django.shortcuts import render

# Sample driver standings data
standings_data = [
    {"position": 1, "name": "Driver A", "team": "Team Red", "points": 150},
    {"position": 2, "name": "Driver B", "team": "Team Blue", "points": 130},
    {"position": 3, "name": "Driver C", "team": "Team Green", "points": 120},
]

# Standings View
def standings_view(request):
    return render(request, 'standings.html', {'drivers': standings_data})