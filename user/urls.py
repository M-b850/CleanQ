from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('Patients-List/', views.UserList.as_view(), name='user-list'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]