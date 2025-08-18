from django.urls import path
from .views import home,get_reports

urlpatterns = [
    path('', home, name="home"),
    path('reports/', get_reports),
]