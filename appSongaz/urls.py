from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='index'),
    path('', views.login, name='all_files'),
    path('all_files/', views.all_files, name='all_files'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('delete_file/<int:id>/', views.delete_file, name='delete'),
    path('download_file/<int:pk>/', views.download_file, name='download_file'),
    path('update/<int:pk>/', login_required(views.UpdateFileView.as_view()), name='update'),



    # path('register', views.register, name='register'),
    # path('document', views.document, name='document'),
    # path('documents', views.documents, name='documents'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('editprofile', views.editprofile, name='editprofile'),
    # # path('editprofile', views.logout_view, name='editprofile'),
    #
    # path('delete_file/<int:id>/', views.delete_file, name='delete_file'),
    # path('download_file/<int:pk>/', views.download_file, name='download_file'),
    # path('update/<int:pk>/', views.UpdateFileView.as_view(), name='update'),
]
