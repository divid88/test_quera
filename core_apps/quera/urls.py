from django.urls import path

from .views import SaveProgramAPIView, get_subject_test, get_test_program

urlpatterns = [
    path('save_program/', SaveProgramAPIView.as_view()),
    path('get_test_program/<int:pk>/', get_test_program),
    path('subjects/', get_subject_test, name='get_subject_test'),
]