from django.urls import path

from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('edit_inventory_item/<int:inventory_item_id>', views.edit_inventory_item, name='edit_inventory_item'),
    path('create_inventory_item/', views.create_inventory_item, name='create_inventory_item'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('delete_inventory_item/<int:inventory_item_id>', views.delete_inventory_item, name='delete_inventory_item'),
    path('export_inventory_to_csv/', views.export_inventory_to_csv, name='export_inventory_to_csv'),
]
