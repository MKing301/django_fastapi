from django.urls import path
from .views import login_view, logout_view, home
from .views import fastapi_proxy

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('fastapi-proxy/', fastapi_proxy, name='fastapi-proxy'),
]
