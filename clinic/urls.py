from django.urls import path

from clinic import views


app_name = 'clinic'

urlpatterns = [
    path('create/', views.CreateClinicView.as_view(), name='create'),
    path('me/', views.WatchClinicView.as_view(), name='me')
]
