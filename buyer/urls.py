from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'buyer'

urlpatterns = [
    path('search_result/',auth_views.LoginView.as_view(template_name = 'buyer/search_result.html'),name = 'Search-Result'),
]