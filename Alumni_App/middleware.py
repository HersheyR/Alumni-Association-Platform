from django.shortcuts import redirect
from django.http import HttpResponse

class CheckAlumniMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is logged in and an alumni
        if request.path.startswith('/donate/') or request.path.startswith('/post_job/'):
            if not request.user.is_authenticated:
                return redirect('login')  # Redirect to login if not authenticated
        response = self.get_response(request)
        return response
