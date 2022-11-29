from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_appointments),
    path('add/', views.add_appointment),
    path('<int:id>/', views.get_appointment),
    path('update/<int:id>/', views.update_appointment),
    path('delete/<int:id>/', views.delete_appointment)
]
