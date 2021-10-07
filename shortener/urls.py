from django.urls import path
from .views import home_view, redirect_urls_views

app_name = "shortener"

urlpatterns = [
    path("", home_view, name="home"),
    path('<str:shortened_part>', redirect_urls_views, name='redirect'),
]
