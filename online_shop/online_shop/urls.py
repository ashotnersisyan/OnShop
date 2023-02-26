"""online_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from ..parties.views import StoreCategoryView
from ..parties.views import ItemCategoryView
from ..parties.views import CustomerView
from ..parties.views import StoreOwnerView
from ..parties.views import StoreView
from ..parties.views import ItemView
from ..parties.views import MyBagView
from ..parties.views import PurchaseView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("NAME.APP.urls")),
    path("api/storecategory", StoreCategoryView.as_view()),
    path("api/itemcategory", ItemCategoryView.as_view()),
    path("api/customer", CustomerView.as_view()),
    path("api/storeowner", StoreOwnerView.as_view()),
    path("api/store", StoreView.as_view()),
    path("api/item", ItemView.as_view()),
    path("api/mybag", MyBagView.as_view()),
    path("api/purchase", PurchaseView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
