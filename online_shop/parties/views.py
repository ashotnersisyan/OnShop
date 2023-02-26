from django.shortcuts import render
from .models import StoreCategory
from .models import ItemCategory
from .models import Customer
from .models import StoreOwner
from .models import Store
from .models import Item
from .models import MyBag
from .models import Purchase
import json
from django.views.generic import View
from django.http import HttpResponse


class StoreCategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = StoreCategory.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategory.get_single(request,id)
        if request.method == "DELETE":
            return StoreCategory.delete(request,id)
        if request.method == "PATCH":
            return StoreCategory.edit(request,id)

    @staticmethod
    def get_single(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return StoreCategoryView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return StoreCategoryView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return StoreCategoryView.ok_status()


class ItemCategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = ItemCategory.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = ItemCategory.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategory.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategory.delete(request, id)
        if request.method == "PATCH":
            return ItemCategory.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return ItemCategoryView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return ItemCategoryView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return ItemCategoryView.ok_status()


class CustomerView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = Customer.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = Customer.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return Customer.get_single(request, id)
        if request.method == "DELETE":
            return Customer.delete(request, id)
        if request.method == "PATCH":
            return Customer.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = Customer.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return CustomerView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = Customer.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return CustomerView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Customer.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return CustomerView.ok_status()


class StoreOwnerView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = StoreOwner.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = StoreOwner.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwner.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwner.delete(request, id)
        if request.method == "PATCH":
            return StoreOwner.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = StoreOwner.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return StoreOwnerView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = StoreOwner.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return StoreOwnerView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreOwner.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return StoreOwnerView.ok_status()


class StoreView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = Store.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = Store.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return Store.get_single(request, id)
        if request.method == "DELETE":
            return Store.delete(request, id)
        if request.method == "PATCH":
            return Store.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = Store.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return StoreView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = Store.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return StoreView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Store.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return StoreView.ok_status()


class ItemView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = Item.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = Item.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return Item.get_single(request, id)
        if request.method == "DELETE":
            return Item.delete(request, id)
        if request.method == "PATCH":
            return Item.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = Item.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return ItemView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = Item.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return ItemView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Item.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return ItemView.ok_status()


class MyBagView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = MyBag.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = MyBag.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBag.get_single(request, id)
        if request.method == "DELETE":
            return MyBag.delete(request, id)
        if request.method == "PATCH":
            return MyBag.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = MyBag.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return MyBagView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = MyBag.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return MyBagView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = MyBag.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return MyBagView.ok_status()


class PurchaseView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type="application/json"
        )

    def get(self, request):
        categories = Purchase.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})
        return self.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = Purchase.objects.create(name=data["name"])
        category.save()
        return self.ok_status

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return Purchase.get_single(request, id)
        if request.method == "DELETE":
            return Purchase.delete(request, id)
        if request.method == "PATCH":
            return Purchase.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = Purchase.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        return Purchase.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = Purchase.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        category.delete()
        return PurchaseView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Purchase.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data["name"]
        category.save()
        return PurchaseView.ok_status()
