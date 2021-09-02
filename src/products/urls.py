
from django.urls import path
from products.views import render_initial_data, product_detail_view, product_delete_view, product_list_view

app_name = 'products'
urlpatterns = [
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),
    path('create', render_initial_data, name='product-initial'),
    path('list', product_list_view, name='product-list'),
]