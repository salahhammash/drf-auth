from django.urls import path
from .views import GameList, GameDetail

urlpatterns = [
    path('', GameList.as_view(), name= 'list'),
    path('<int:pk>/', GameDetail.as_view(), name= 'details')
]