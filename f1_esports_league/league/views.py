from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Registration View
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can send an email notification to the admin here
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Driver Profile View with role-based access
@login_required
def driver_profile_view(request):
    profile = request.user.driverprofile  # Assuming the user has a related DriverProfile object

    if profile.role.name == 'Driver':
        # If the user is a Driver, show them limited information (e.g., FIA posts, standings, etc.)
        return render(request, 'profile_driver.html', {'profile': profile})
    elif profile.role.name == 'FIA':
        # If the user is FIA, show all information
        return render(request, 'profile_fia.html', {'profile': profile})
    elif profile.role.name == 'Admin':
        # If the user is an Admin, show all information with editing rights
        return render(request, 'profile_admin.html', {'profile': profile})
    else:
        # If none of these roles match, you can handle it accordingly
        return redirect('home')

# Home View
def home_view(request):
    return render(request, 'home.html')
