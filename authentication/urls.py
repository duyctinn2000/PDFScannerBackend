from django.urls import path
from .views import ChangePasswordView, RegisterView,LoginView

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('changepassword',ChangePasswordView.as_view()),
]
