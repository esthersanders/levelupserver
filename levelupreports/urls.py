from django.urls import path
from .views import usergame_list
from .views import eventuser_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', eventuser_list)
]