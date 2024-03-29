from django.urls import path
from .views import FooterComponents, HeaderComponenets, contactUsView, FeedbackView, AboutUsView, BucketView

app_name = 'sites'
urlpatterns = [
    path('hrader_components', HeaderComponenets.as_view(), name='hrader_components'),
    path('footer_components', FooterComponents.as_view(), name='footer_components'),
    path('contact_us/', contactUsView.as_view(), name='contact_us'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('buckets/', BucketView.as_view(), name='buckets'),
]
