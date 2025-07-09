from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home-view"),
    path('create', student_create_view, name="create-student"),
    path('<int:pk>', student_detail_view, name="student-detail"),
    path('update/<int:pk>', student_edit_view, name="edit-student"),
    path('delete/<int:pk>', student_destroy_view, name="delete-student"),
]
