from django.contrib import admin
from django.urls import path, include
from . import views


"""admin.site.site_header = "Login to EAD Registry"
admin.site.site_title = "EAD Registry - Federal Ministry of Environment"
admin.site.index_title = "EAD Registry"
"""

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
]
