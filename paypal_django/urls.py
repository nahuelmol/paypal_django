from django.contrib import admin
from django.urls import path,include

from . import views

import base.urls 
import accounts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baseapp/',include('base.urls')),
    path('account/',include('accounts.urls')),
    
]
