from django.urls import path
from .views import customer_list, customer_detail, customer_new, customer_edit, customer_delete

urlpatterns = [
    path('', customer_new, name='customer_new'),
    path('cust_list/', customer_list, name='customer_list'),
    path('<int:pk>/', customer_detail, name='customer_detail'),    
    path('<int:pk>/edit/', customer_edit, name='customer_edit'),
    path('<int:pk>/delete/', customer_delete, name='customer_delete'),
]


  #  path('', customer_new, name='customer_new'),
   # path('cust_list/', customer_list, name='customer_list'),

