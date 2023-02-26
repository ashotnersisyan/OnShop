from django.contrib import admin
from .models import StoreCategory
from .models import ItemCategory
from .models import Customer
from .models import StoreOwner
from .models import Store
from .models import Item
from .models import MyBag
from .models import Purchase


admin.site.register(StoreCategory)
admin.site.register(ItemCategory)
admin.site.register(Customer)
admin.site.register(StoreOwner)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(MyBag)
admin.site.register(Purchase)
