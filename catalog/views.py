from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.utils import timezone

class HomeView(ListView):
    model = Item
    template_name = "home.html"

class ProductDetail(DetailView):
    model = Item
    template_name = 'product.html'

 
def checkout(request):
    return render(request ,'checkout.html')

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order items is in order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"{item.title}'s quantity was updated")
            return redirect("product", slug=slug)
        else:
            order.items.add(order_item)
            messages.success(request, f"{item.title}'s was added to your cart")
            return redirect("product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, f"{item.title}'s was added to your cart")
        return redirect("product", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order items is in order
        if order.items.filter(item__slug=item.slug).exists():
            order.items.remove(order_item)
            order.save()
            messages.success(request, f"{item.title} was removed from your cart")
            return redirect("product", slug=slug)
        else:
            # add a message saying the user doesnt have an order
            messages.info(request, f"{item.title} item was not in your cart")
            return redirect("product", slug=slug)
    else:
        # add a message saying the user doesnt have an order
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)
