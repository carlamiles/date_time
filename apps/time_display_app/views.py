from django.shortcuts import render
from time import localtime, strftime

# Create your views here.
def index(request): 
    print('*'*50)
    print('the index function is running')
    context = {
        'date': strftime('%b %d, %Y', localtime()),
        'time': strftime('%I:%M %p', localtime())
    }
    return render(request, "time_display_app/index.html", context)