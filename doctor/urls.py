from django.urls import path
from .views import  HomeComponents, LatestComponenets, SignUpDoctorView, All_doctor

app_name = 'doctor'
urlpatterns = [
    path('', HomeComponents.as_view(), name='home'),
    path('latest_doctor/', LatestComponenets.as_view(), name='latest_doctor'),
    path('signup_doctor/', SignUpDoctorView.as_view(), name='signup_doctor'),
    path('list_doctor/', All_doctor.as_view(), name='all_doctor'),
]
