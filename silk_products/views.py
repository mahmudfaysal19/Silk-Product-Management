from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from types import SimpleNamespace
from bson import ObjectId
from .db import get_products
from .forms import SilkProductForm

def product_list(request):
    if getattr(settings, 'DEMO_MODE', False):
        type_map = {'saree': 'Saree', 'fabric': 'Fabric', 'scarf': 'Scarf'}
        sample = [
            SimpleNamespace(
                pk=1, name='Classic Rajshahi Saree', type='saree', price=2999.99, availability=True,
                get_type_display=lambda: type_map['saree']
            ),
            SimpleNamespace(
                pk=2, name='Premium Silk Fabric', type='fabric', price=1499.50, availability=True,
                get_type_display=lambda: type_map['fabric']
            ),
            SimpleNamespace(
                pk=3, name='Elegant Silk Scarf', type='scarf', price=499.00, availability=False,
                get_type_display=lambda: type_map['scarf']
            ),
        ]
        query = request.GET.get('q')
        if query:
            q = query.lower()
            products = [p for p in sample if q in p.name.lower() or q in p.type.lower()]
        else:
            products = sample
    else:
        col = get_products()
        query = request.GET.get('q')
        if query:
            regex = {'$regex': query, '$options': 'i'}
            cursor = col.find({'$or': [{'name': regex}, {'type': regex}]}, sort=[('_id', -1)])
        else:
            cursor = col.find({}, sort=[('_id', -1)])
        type_map = {'saree': 'Saree', 'fabric': 'Fabric', 'scarf': 'Scarf'}
        products = [
            SimpleNamespace(
                pk=str(doc['_id']),
                name=doc.get('name'),
                type=doc.get('type'),
                price=doc.get('price'),
                availability=bool(doc.get('availability')),
                get_type_display=lambda t=doc.get('type'): type_map.get(t, t)
            )
            for doc in cursor
        ]
    return render(request, 'silk_products/product_list.html', {'products': products})

def product_create(request):
    if getattr(settings, 'DEMO_MODE', False):
        messages.info(request, 'Demo mode: create disabled.')
        return redirect('product_list')
    if request.method == 'POST':
        form = SilkProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            doc = {
                'name': data['name'],
                'type': data['type'],
                'price': float(data['price']),
                'availability': bool(data['availability']),
            }
            get_products().insert_one(doc)
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = SilkProductForm()
    return render(request, 'silk_products/product_form.html', {'form': form, 'action': 'Create'})

def product_update(request, pk):
    if getattr(settings, 'DEMO_MODE', False):
        messages.info(request, 'Demo mode: update disabled.')
        return redirect('product_list')
    col = get_products()
    try:
        oid = ObjectId(pk)
    except Exception:
        messages.error(request, 'Invalid product ID')
        return redirect('product_list')
    doc = col.find_one({'_id': oid})
    if not doc:
        messages.error(request, 'Product not found')
        return redirect('product_list')
    if request.method == 'POST':
        form = SilkProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            update = {
                'name': data['name'],
                'type': data['type'],
                'price': float(data['price']),
                'availability': bool(data['availability']),
            }
            col.update_one({'_id': oid}, {'$set': update})
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = SilkProductForm(initial={
            'name': doc.get('name', ''),
            'type': doc.get('type', 'saree'),
            'price': doc.get('price', 0),
            'availability': bool(doc.get('availability', True)),
        })
    return render(request, 'silk_products/product_form.html', {'form': form, 'action': 'Update'})

def product_delete(request, pk):
    if getattr(settings, 'DEMO_MODE', False):
        messages.info(request, 'Demo mode: delete disabled.')
        return redirect('product_list')
    col = get_products()
    try:
        oid = ObjectId(pk)
    except Exception:
        messages.error(request, 'Invalid product ID')
        return redirect('product_list')
    doc = col.find_one({'_id': oid})
    if not doc:
        messages.error(request, 'Product not found')
        return redirect('product_list')
    if request.method == 'POST':
        col.delete_one({'_id': oid})
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    type_map = {'saree': 'Saree', 'fabric': 'Fabric', 'scarf': 'Scarf'}
    product = SimpleNamespace(
        pk=str(doc['_id']),
        name=doc.get('name'),
        type=doc.get('type'),
        price=doc.get('price'),
        availability=bool(doc.get('availability')),
        get_type_display=lambda t=doc.get('type'): type_map.get(t, t)
    )
    return render(request, 'silk_products/product_confirm_delete.html', {'product': product})
