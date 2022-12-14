from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="index"),
    path('Shireen/',views.Shireen),
    path('Shireen/psid',views.ShireenPsid),
    path('search',views.search),
    path('search-action',views.search_action,name="search_action"),
    path('signup',views.signup),
    path('signup-action',views.signup_action,name="signup_action"),
    path('signin',views.signin),
    path('signin-action',views.signin_action,name="signin_action"),
    path('courseid',views.courseid)
    
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)