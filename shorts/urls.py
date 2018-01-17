from django.urls import path

from shorts.views import HoveView, short_url_redirect

urlpatterns = [
    path('', HoveView.as_view(), name='main_page'),
    path('<slug:slug>/', short_url_redirect, name='short_url_redirect'),
]