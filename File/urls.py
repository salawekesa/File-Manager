from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Manager.urls")),
    # path('Users/', include("django.contrib.auth.urls")),
    path('Users/', include("Users.urls")),
]
