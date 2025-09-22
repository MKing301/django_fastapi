import requests

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def fastapi_proxy(request):
    refresh = RefreshToken.for_user(request.user)
    access_token = str(refresh.access_token)

    headers = {"Authorization": f"Bearer {access_token}"}
    fastapi_response = requests.get("http://localhost:8001/protected", headers=headers)

    return JsonResponse(fastapi_response.json(), status=fastapi_response.status_code)

