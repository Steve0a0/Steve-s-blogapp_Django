"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('addpost/', views.addpost, name = 'addpost'),
    path('article/<int:pk>/', views.articlepage, name = 'article'),
    path('article/edit/<int:pk>/', views.updatepost, name = 'update'),
    path('article/delete/<int:pk>',views.deletepost, name= 'delete'),
    path('accounts/login/',views.loginpage, name= 'login'),
    path('signup/',views.signup, name= 'signup'),
    path('logout/',views.logoutpage, name= 'logout'),
    path('updateprofile/',views.updateprofilepage, name= 'updateprofile'),
    path('profile/',views.profilepagee, name= 'profile'),
] 

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
