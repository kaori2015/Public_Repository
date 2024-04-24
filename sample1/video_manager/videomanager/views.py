# videomanager/views.py
from django.shortcuts import render
from .models import Video

# videomanager/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# videomanager/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# videomanager/views.py
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def logout_view(request):
    #logout(request)
    return render(request, 'registration/logout.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('video_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('video_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

from django.shortcuts import render
from django.http.response import HttpResponse
 
def index_template(request):
    myapp_data = {
    'app': 'Django',
    'num': range(10),
    }
    return render(request, 'index.html', myapp_data)