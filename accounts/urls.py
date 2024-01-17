from django.urls import path
from .views import (UserSignupView, LoginViews, AcceptCodeView, ProfileView, LogOutView \
    ,UserPasswordResetView, UserPasswordResetCompleteView, UserPasswordResetConfirmView, UserPasswordResetDoneView,
                    EditProfileView)
app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', LoginViews.as_view(), name='login'),
    path('accept_code/', AcceptCodeView.as_view(), name='accept_code'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/logout/', LogOutView.as_view(), name='logout'),
    path('reset/', UserPasswordResetView.as_view(), name='reset_password'),
	path('reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
	path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('confirm/complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
