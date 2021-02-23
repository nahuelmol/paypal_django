from django.contrib import admin
from django.urls import path,include

import base.urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baseapp/',include('base.urls'))
]
