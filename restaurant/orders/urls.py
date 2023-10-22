from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrdersListView.as_view(), name='index_order'),
    path("<int:pk>/delete", views.delete, name='delete_order'),
    path("add/", views.add, name='add_order'),
]
