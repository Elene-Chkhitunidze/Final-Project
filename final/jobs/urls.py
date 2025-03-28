from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_logout
from .views import add_to_favourites, favourites_list

urlpatterns = [
                  path('', views.home, name='home'),
                  path('login/', views.login_view, name='login'),
                  path('register/', views.register, name='register'),
                  path('employer-profile/', views.employer_profile, name='employer_profile'),
                  path('add-vacancy/', views.add_vacancy, name='add_vacancy'),
                  path('edit-vacancy/<int:vacancy_id>/', views.edit_vacancy, name='edit_vacancy'),
                  path('delete-vacancy/<int:vacancy_id>/', views.delete_vacancy, name='delete_vacancy'),
                  path('employer-profile/view/', views.employer_profile_view, name='employer_profile_view'),
                  path('vacancy/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
                  path('logout/', custom_logout, name='logout'),
                  path('job_seeker_profile/', views.job_seeker_profile, name='job_seeker_profile'),
                  path('vacancy/job_seeker/<int:vacancy_id>/', views.vacancy_detail_job_seeker, name='vacancy_detail_job_seeker'),
                  path('reset-password/', views.forgot_password, name='reset_password'),
                  path('resume-upload-success/', views.resume_upload_success, name='resume_upload_success'),
                  path('vacancy/<int:vacancy_id>/add_to_favourites/', add_to_favourites, name='add_to_favourites'),
                  path('favourites/', favourites_list, name='favourites_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)