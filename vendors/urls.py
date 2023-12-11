from django.urls import path
from .views import (
    register,
    login,
    logout,
    vendor_list_create,
    vendor_detail,
    vendor_performance,
    purchase_order_list_create,
    purchase_order_detail,
    acknowledge_purchase_order,
)

urlpatterns = [
    # URLs for login, register and logout
    path('api/register/', register, name='register'),
    path('api/login/', login, name='login'),
    path('api/logout/', logout, name='logout'),

    # Vendor URLs
    path('api/vendors/', vendor_list_create, name='vendor-list-create'),
    path('api/vendors/<int:vendor_id>/', vendor_detail, name='vendor-detail'),
    path('api/vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),

    # Purchase Order URLs
    path('api/purchase_orders/', purchase_order_list_create, name='purchase-order-list-create'),
    path('api/purchase_orders/<int:po_id>/', purchase_order_detail, name='purchase-order-detail'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order, name='acknowledge-purchase-order'),
]
