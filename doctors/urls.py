from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_doctors),
    path('add/', views.add_doctor),
    path('<int:id>/', views.get_doctor),
    path('update/<int:id>/', views.update_doctor),
    path('delete/<int:id>/', views.delete_doctor)
]
