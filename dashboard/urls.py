from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', index, name='dashboard'),
    path('staff/', staff, name='staff'),
    path('staff/<int:id>/', staff_details, name='staff-details'),
    path('product/', product, name='product'),
    path('update/<int:id>/', update_product, name='update'),
    path('delete/<int:id>/', delete_product, name='delete'),
    path('order/', order, name='order'),
]
