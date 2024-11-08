from django.shortcuts import render, redirect
from .forms import AlumniRegistrationForm

# View to handle alumni registration
def register(request):
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('success')  # Redirect to a success page after saving
    else:
        form = AlumniRegistrationForm()

    return render(request, 'Alumni_App/register.html', {'form': form})

# View for success page
def success(request):
    return render(request, 'Alumni_App/success.html')
