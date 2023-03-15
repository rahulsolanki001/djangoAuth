from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("",views.registerView,name="register"),
    path("login",views.loginView,name="login"),
    path('dashboard',views.dashboardView,name="dashboard"),
    path('logout',views.logoutView,name='logout')
]

urlpatterns +=staticfiles_urlpatterns()
