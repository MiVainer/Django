from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<center><h2>Hello!!! From Python Django!! By MiVainer</h2></center>")