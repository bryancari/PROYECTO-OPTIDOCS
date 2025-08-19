from django.urls import path
from .views import indexV

urlpatterns = [
    path("", indexV),
]
