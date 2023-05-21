from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("index/", views.homepage, name="index"),
    path("test/<int:test_id>/", views.test, name="test"),
    path("getTest/<int:test_id>/", views.getTest, name="getTest"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),

]