from django.contrib import admin
from django.urls import path, include
from CV import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('new/cv_entry', views.newCV, name="cv_new"),
    path('edit/personalDetails', views.personDet_edit, name='edit_personal_details'),
    path('edit/<pk>/cv_entry', views.CV_Entry_edit, name="cv_edit"),
    path('remove/<pk>/cv_entry', views.CV_Entry_remove, name="cv_remove"),
    path('new/education', views.Education_new, name="new_educ"),
    path('edit/<pk>/education', views.Education_edit, name="education_edit"),
    path('remove/<pk>/education', views.Education_remove, name="education_remove"),
]
