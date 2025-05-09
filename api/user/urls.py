from django.urls import path
from .views import FaceSignUpView, FaceLoginView

urlpatterns = [
    path('face-signup/', FaceSignUpView.as_view(), name='face_signup'),
    path('face-login/', FaceLoginView.as_view(), name='face_login'),
]
