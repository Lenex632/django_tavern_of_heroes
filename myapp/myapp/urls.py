from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tavern_of_heroes.urls', namespace='app')),
    path('api/', include('tavern_of_heroes.api.urls', namespace='api')),
    path('admin/', admin.site.urls),
]
