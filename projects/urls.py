
from django.urls import path
from .views import project



urlpatterns = [
   path('works/', project, name='works'),
]














