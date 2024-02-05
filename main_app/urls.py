from .views import Home, FlowerList, FlowerDetails;
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('flowers/', FlowerList.as_view(), name='flowers-list'),
    path('flowers/<int:id>/',FlowerDetails.as_view(), name='flower-details')
]