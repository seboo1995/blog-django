
from django.http import HttpResponse

def start_screen(request):
    return HttpResponse('<h1> Welcome to the Blog API </h1> ')