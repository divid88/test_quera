from django.urls import path

from . import views


urlpatterns = [
    path('all/', views.SubjectAPIView.as_view(), name="subjects_list"),
]