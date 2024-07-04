from django.contrib import admin
from .models import (Book, Author, Publisher, BookPrice, Inventory, Order, Customer, Product, Warehouse, Category,
                     Supplier)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'email')
    search_fields = ('name', 'birthdate', 'email')
    list_filter = ('name', 'birthdate', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'genre', 'author')
    search_fields = ('title', 'pub_date', 'genre')
    list_filter = ('title', 'pub_date', 'genre')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')


@admin.register(BookPrice)
class BookPriceAdmin(admin.ModelAdmin):
    list_display = ('book', 'publisher', 'price_book')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'quantity')
    search_fields = ('product', 'warehouse', 'quantity')
    list_filter = ('product', 'warehouse', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'total_amount')
    search_fields = ('customer', 'order_date', 'total_amount')
    list_filter = ('customer', 'order_date', 'total_amount')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'address')
    list_filter = ('name', 'address')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'price')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'phone', 'address')
