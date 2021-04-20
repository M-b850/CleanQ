from django.urls import path

from reservation import views


app_name = 'reservation'

urlpatterns = [
    path('create/', views.CreateReservationView.as_view(), name='create'),
    path('mine/', views.ListReservationView.as_view(), name='list'),
    path('clinics/', views.ListClinicsView.as_view(), name='clinics')
]
