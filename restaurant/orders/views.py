from django.shortcuts import render, redirect
from .models import Order, OrderComposition
from dishes.models import Dish
from django.db.models import Count
from django.views.generic import ListView, DetailView

# Create your views here.
class OrdersListView(ListView):
    queryset = Order.objects.order_by('-date')
    template_name = 'orders/index.html'
    context_object_name = 'orders'

def add(request):
    error = ''
    if request.method == 'POST':
        dishes = [x for x in Dish.objects.all()]
        dishes_counts = {}

        for dish in dishes:
            if request.POST.get(dish.name):
                dishes_counts[dish] = int(request.POST.get(dish.name))
        
        order = Order()
        
        for dish, count in dishes_counts.items():
            for ing in dish.ingridients.all():
                ing.count -= count
                if ing.count < 0:
                    error = f'На складе нет такого кол-ва следующего ингредиента: {ing.name}'
                    data = {
                        'error': error,
                        'dishes': Dish.objects.all()
                    }

                    return render(request, 'orders/add.html', data)

        for dish, count in dishes_counts.items():
            for ing in dish.ingridients.all():
                ing.save()
            if count > 0:
                orderComposition = OrderComposition()
                orderComposition.order = order
                orderComposition.dish = dish
                orderComposition.dish_count = count
                order.cost += dish.default_price * count
                order.save()
                orderComposition.save()

        order.save()
        
        return redirect('index_order')

    order = Order()
    data = {
        'error': error,
        'order': order,
        'dishes': Dish.objects.all()
    }

    return render(request, 'orders/add.html', data)

def delete(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
        return redirect('index_order')
    except Order.DoesNotExist:
        return redirect('index_order')