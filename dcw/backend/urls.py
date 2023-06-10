from django.contrib import admin
from django.urls import path
from backend import views 
from backend.views import addToDb

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("addBoundingBox/", views.addBoundingBox, name="addBoundingBox"),
    path("emptyDataset/", views.emptyDataset, name="emptyDataset"),
    path('api/item/add/', addToDb.as_view(), name='addtodb'),
]
