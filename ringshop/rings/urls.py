from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name="home"),
    path('about/',views.about,name="about"),
    path('student/',views.student, name="student"),
    path('insertData/', views.insertData, name="insertData"),
    path('viewdata/',views.viewdata, name="viewdata")
]
