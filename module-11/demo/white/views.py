#Mark White
#CSD325
#11.2


from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Mark White says Hello!')
