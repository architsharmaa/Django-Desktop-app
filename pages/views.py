# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('The server has started')