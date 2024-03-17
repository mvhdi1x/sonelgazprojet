from django.urls import path
from members import views

urlpatterns = [
  path('register/', views.UserRegisterView.as_view(), name='register'),
  path('edit_profile/', views.UpdateProfileView.as_view(), name='edit_profile'),
  # path('login/', views.UserRegisterView.as_view(), name='login'),
]

