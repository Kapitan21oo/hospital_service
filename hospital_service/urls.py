
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include('content_app.urls')),
    path('account/', include('account_app.urls')),

]
