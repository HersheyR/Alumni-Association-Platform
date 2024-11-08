from django.shortcuts import render

def register(request):
    return render(request, 'Alumni_App/register.html')

def jobs(request):
    return render(request, 'Alumni_App/jobs.html')

def events(request):
    return render(request, 'Alumni_App/events.html')

def networking(request):
    return render(request, 'Alumni_App/networking.html')
