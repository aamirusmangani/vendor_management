from django.contrib import admin
from .models import Vendor, PurchaseOrder

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_details', 'address', 'vendor_code')
    search_fields = ('name', 'vendor_code')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number', 'vendor', 'order_date', 'delivery_date', 'status')
    list_filter = ('vendor', 'status', 'order_date')
    search_fields = ('po_number', 'vendor__name')

