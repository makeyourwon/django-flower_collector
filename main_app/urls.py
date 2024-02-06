from .views import Home, FlowerList, FlowerDetails, HydrateList, HydrateDetail;
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('flowers/', FlowerList.as_view(), name='flowers-list'),
    path('flowers/<int:id>/',FlowerDetails.as_view(), name='flower-details'),
    path('flowers/<int:flower_id>/hydrates', HydrateList.as_view(), name='hydrate-list'),
    path('flowers/<int:flower_id>/hydrates/<int:id>',HydrateDetail.as_view(), name='hydrate-details')
]