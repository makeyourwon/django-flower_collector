from .views import Home, FlowerList, FlowerDetails, HydrateList, HydrateDetail, CustomerList, CustomerDetail, AddFlowerToCustomer,RemoveFlowerToCustomer;
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('flowers/', FlowerList.as_view(), name='flowers-list'),
    path('flowers/<int:id>/',FlowerDetails.as_view(), name='flower-details'),
    path('flowers/<int:flower_id>/hydrates', HydrateList.as_view(), name='hydrate-list'),
    path('flowers/<int:flower_id>/hydrates/<int:id>',HydrateDetail.as_view(), name='hydrate-details'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:id>/', CustomerDetail.as_view(), name='customer-detail'),
    path('customers/<int:customer_id>/add_flower/<int:flower_id>/', AddFlowerToCustomer.as_view(), name='add-flower-to-customer'),
    path('customers/<int:customer_id>/remove_flower/<int:flower_id>/', RemoveFlowerToCustomer.as_view(), name='remove-flower-to-customer'),
    
]