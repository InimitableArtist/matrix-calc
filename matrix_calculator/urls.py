from django.urls import path

from . import views

urlpatterns = [    
    path('', views.get_matrix_dimensions, name = 'home'),
    path('enternumber/<f_number>/<s_number>/', views.enter_matrix_numbers, name = 'enter_number'),
    path('calculated/', views.calculate, name = 'calculated'),

]
