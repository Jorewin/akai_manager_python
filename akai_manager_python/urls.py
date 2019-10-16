"""akai_manager_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from meetings import views as meeting_views
from members import views as member_views
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from qr_code import urls as qr_code_urls



urlpatterns = [
    path('admin/', admin.site.urls),

    path('meetings/create/', meeting_views.create, name="meeting_create"),
    path('meetings/<int:pk>/', meeting_views.MeetingDetailView.as_view(), name="meeting_view"),
    path('meetings/register/<str:code>/', meeting_views.register, name="meeting_register_code"),
    path('meetings/register/', meeting_views.register, name="meeting_register"),
    path('meetings/register/', include(qr_code_urls, namespace='qr_code')),
    path('meetings/', meeting_views.MeetingListView.as_view(), name="meeting_list"),

    path('members/', member_views.IndexView.as_view(), name="member_list"),
    path('members/<int:pk>/', member_views.DetailView.as_view(), name="member_detail"),
    path('members/<int:pk>/edit',
         member_views.EditView.as_view(), name="member_edit"),
    path('members/<int:pk>/delete',
         member_views.DeleteView.as_view(), name="member_delete"),

    path('', member_views.login, name="login"),
    path('', include('social_django.urls', namespace="social")),
    path('logout/', auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout'),
]
