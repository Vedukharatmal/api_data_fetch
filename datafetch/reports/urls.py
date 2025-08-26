from django.urls import path
from .views import home,reports

urlpatterns = [
    path('', home, name="home"),
    path('reports/', reports),
]