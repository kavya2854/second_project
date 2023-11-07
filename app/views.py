from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def silk(request):
    return HttpResponse('<h1 style="color:red;"><marquee>Iam not talking about the Dairy Milk Silk</h1></marquee>')