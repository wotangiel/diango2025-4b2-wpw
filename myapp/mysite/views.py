from django.http import HttpResponse

def landing_page(request):
    return HttpResponse("You are on landing page")