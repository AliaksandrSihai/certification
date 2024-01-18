from django.contrib import admin
from django.utils.html import format_html

from retail_chain.models import Contacts, Products, RetailChain

admin.site.register(Contacts)
admin.site.register(Products)


class ContactsInline(admin.TabularInline):
    model = Contacts
    extra = 1
    fields = ["email", "country", "city", "street", "house_number"]


class ProductsInline(admin.TabularInline):
    model = Products.supplier.through
    extra = 1


@admin.register(RetailChain)
class RetailChainAdmin(admin.ModelAdmin):
    """Регистрация в админ-панели модели RetailChain"""

    list_display = (
        "title",
        "supplier",
        "supplier_url",
        "supplier_debt",
        "created_at",
        "relation_level",
        "contacts",
    )
    list_filter = ("contacts__city",)
    inlines = (ContactsInline, ProductsInline)
    actions = ("clear_supplier_debt",)

    def supplier_url(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="http://127.0.0.1:8000/admin/retail_chain/retailchain/{0}">{1}</a>',
                obj.supplier.id,
                obj.supplier.title,
            )
        return "Поставщик отсутствует"

    supplier_url.short_description = "ссылка поставщика"

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_supplier_debt(self, request, queryset):
        queryset.update(supplier_debt=0)
