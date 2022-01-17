import csv

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import InventoryItem


class IndexView(generic.ListView):
    template_name = 'tracker/index.html'
    context_object_name = 'inventory_item_list'

    def get_queryset(self):
        return InventoryItem.objects.all()

class DetailView(generic.DetailView):
    model = InventoryItem
    template_name = 'tracker/detail.html'

def create(request):
    return render(request, 'tracker/create.html')

class EditView(generic.DetailView):
    model = InventoryItem
    template_name = 'tracker/edit.html'

class DeleteView(generic.DetailView):
    model = InventoryItem
    template_name = 'tracker/delete.html'

def edit_inventory_item(request, inventory_item_id):
    inventory_item = get_object_or_404(InventoryItem, pk=inventory_item_id)
    update_item_name = request.POST['item_name']
    update_company = request.POST['company']
    update_item_description = request.POST['item_description']
    update_stock_quantity = request.POST['stock_quantity']
    update_item_location = request.POST['item_location']
    update_release_date = request.POST['release_date']

    inventory_item.item_name = update_item_name
    inventory_item.company = update_company
    inventory_item.item_description = update_item_description
    inventory_item.stock_quantity = update_stock_quantity
    inventory_item.item_location = update_item_location
    inventory_item.release_date = update_release_date

    inventory_item.save()

    return HttpResponseRedirect(reverse('tracker:detail', args=(inventory_item.id,)))

def create_inventory_item(request):
    create_item_name = request.POST['item_name']
    create_company = request.POST['company']
    create_item_description = request.POST['item_description']
    create_stock_quantity = request.POST['stock_quantity']
    create_item_location = request.POST['item_location']
    create_release_date = request.POST['release_date']

    new_inventory_item = InventoryItem(
        item_name = create_item_name,
        company = create_company,
        item_description = create_item_description,
        stock_quantity = create_stock_quantity,
        item_location = create_item_location,
        release_date = create_release_date
    )
    new_inventory_item.save()

    return HttpResponseRedirect(reverse('tracker:detail', args=(new_inventory_item.id,)))


def delete_inventory_item(request, inventory_item_id):
    inventory_item = get_object_or_404(InventoryItem, pk=inventory_item_id)
    inventory_item.delete()

    return HttpResponseRedirect(reverse('tracker:index'))



def export_inventory_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory.csv"'

    writer = csv.writer(response)
    writer.writerow(['item_name', 'company', 'item_description', 'stock_quantity', 'item_location', 'release_date'])

    inventory = InventoryItem.objects.all().values_list('item_name', 'company', 'item_description', 'stock_quantity', 'item_location', 'release_date')

    for item in inventory:
        writer.writerow(item)

    return  response
