from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("csrf-demo/", views.csrf_demo, name="csrf_demo"),
    path("authentication-demo/", views.authentication_demo, name="authentication_demo"),
    path("sql-demo/", views.sql_demo, name="sql_demo"),
    path("xss-demo/", views.xss_demo, name="xss_demo"),
    path("admin-patchup-demo/", views.admin_demo, name="admin_demo"),
    path("", include("django.contrib.auth.urls")),
    path("next/", views.nav_next, name="nav_next"),
]
