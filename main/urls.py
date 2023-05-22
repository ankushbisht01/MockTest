from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.homepage, name="homepage"),
    path("test/<int:test_id>/", views.test, name="test"),
    path("getTest/<int:test_id>/", views.getTest, name="getTest"),
    path("delete/<int:test_id>/", views.deleteTest, name="delete"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),

]