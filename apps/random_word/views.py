from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    print('*'*50)
    print('the random word function is running!')
    generate_str = {'random_str': get_random_string(length=14)}
    request.session['counter'] += 1
    return render(request, 'random_word/index.html', generate_str)

def reset(request):
    print('*'*50)
    print('the reset function is running')
    request.session['counter'] = 0
    return redirect('/random_word')