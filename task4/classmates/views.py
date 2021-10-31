from django.http.response import HttpResponse
from django.http import HttpResponse    

def index(request):
    return HttpResponse('Hello, World. You''re at the classmates index')
