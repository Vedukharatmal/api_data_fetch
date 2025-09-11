# from django.urls import path
# from .views import home,reports
# from . import views

# urlpatterns = [
#     path('', home, name="home"),
#     path('api/reports/', views.reports_api, name="reports_api"),
# ]


from django.urls import path
from .views import home, reports, reports_api, get_api_endpoint
from . import views

# urlpatterns = [
#     path('', home, name="home"),
#     path('api/reports/', views.reports, name="reports"),        # DB endpoint
#     path('api/reports_api/', views.reports_api, name="reports_api"),  # external API caller
# ]

urlpatterns = [
    path('', views.home, name="home"),
    path('api/reports/', views.reports, name="reports"),
    path('api/reports_api/', views.reports_api, name="reports_api"),
    path('api/get-endpoint/', views.get_api_endpoint, name="get_api_endpoint"),  # new
]