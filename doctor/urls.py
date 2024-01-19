from django.urls import path
from .views import  HomeComponents, SignUpDoctorView, All_doctor \
    ,DoctorSlider, LatesDoctor, AdvanceSearchDoctorView, AppointmentDoctorView, DetailsQuestionDoctorView

app_name = 'doctor'
urlpatterns = [
    path('', HomeComponents.as_view(), name='home'),
    path('signup_doctor/', SignUpDoctorView.as_view(), name='signup_doctor'),
    path('list_doctor/', All_doctor.as_view(), name='all_doctor'),
    # path('doctor_slider/', DoctorSlider.as_view(), name='doctor_slider'),
    path('latest_doctor', LatesDoctor.as_view(), name='latest_doctor'),
    # path('advance_search_doctor/', AdvanceSearchDoctorView.as_view(), name='advance_search_doctor'),
    path('details_doctor/<int:doctor_id>/', AppointmentDoctorView.as_view(), name='order_details_doctor'),
]
