# orders/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order

 
@login_required
def order_card_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_card.html', {'form': form})



def order_success_view(request):
    return render(request, 'order_success.html')

@login_required
def track_orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'track_orders.html', {'orders': orders})