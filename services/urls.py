from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_services),
    path('add/', views.add_service),
    path('<int:id>/', views.get_service),
    path('update/<int:id>/', views.update_service),
    path('delete/<int:id>/', views.delete_service)
]
