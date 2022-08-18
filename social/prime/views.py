from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json

def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    context = {}
    user_data = request.user.socialaccount_set.all()[0].extra_data
    context['qr'] = json.dumps(user_data['name'])
    return render(request, 'home.html', context=context)
