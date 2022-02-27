from django.contrib import admin
from .models import Product, WishList_Cart, Comments, Delivery

# Register your models here.
admin.site.register(Product)
admin.site.register(WishList_Cart)
admin.site.register(Comments)
admin.site.register(Delivery)