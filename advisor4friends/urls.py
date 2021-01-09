from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('city/', include('city.urls')),
]
