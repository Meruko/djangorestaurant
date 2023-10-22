from django.shortcuts import render, redirect
from .models import Dish, Ingridient
from .forms import DishForm, IngridientForm
from django.views.generic import ListView, UpdateView

class DishListView(ListView):
    model = Dish
    template_name = 'dishes/index.html'
    context_object_name = 'dishes'

class DishIngridientsListView(ListView):
    model = Dish
    template_name = 'dish_ingridients/index.html'
    context_object_name = 'dishes'

class IngridientListView(ListView):
    model = Ingridient
    template_name = 'ingridients/index.html'
    context_object_name = 'ingridients'

class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'dishes/add.html'
    
    form_class = DishForm

class IngridientUpdateView(UpdateView):
    model = Ingridient
    template_name = 'ingridients/add.html'
    
    form_class = IngridientForm

def add(request):
    error = ''
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_dish')
        else:
            error = 'Форма была неверной'

    form = DishForm()

    data = {
        'error': error,
        'form': form
    }

    return render(request, 'dishes/add.html', data)

def addIngridient(request):
    error = ''
    if request.method == 'POST':
        form = IngridientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_ingridient')
        else:
            error = 'Форма была неверной'

    form = IngridientForm()

    data = {
        'error': error,
        'form': form
    }

    return render(request, 'ingridients/add.html', data)

def addComposition(request, pk):
    error = ''
    if request.method == 'POST':
        ingridients_names = [x.name for x in Ingridient.objects.all()]
        ingridients_ids = []

        for name in ingridients_names:
            if request.POST.get(name):
                ingridients_ids.append(int(request.POST.get(name)))
        
        dish = Dish.objects.get(pk=pk)
        dish.ingridients.clear()
        for id in ingridients_ids:
            dish.ingridients.add(Ingridient.objects.get(id=id))
        
        return redirect('index_dish_ingridients')

    dish = Dish.objects.get(pk=pk)
    ingridients = Ingridient.objects.all()
    ingridientsChecked = {}
    for ing in ingridients:
        if dish.ingridients.contains(ing):
            ingridientsChecked[ing] = True
        else:
            ingridientsChecked[ing] = False

    data = {
        'error': error,
        'dish': dish,
        'ingridients': ingridientsChecked
    }

    return render(request, 'dishes/add_composition.html', data)

def delete(request, pk):
    try:
        dish = Dish.objects.get(pk=pk)
        dish.delete()
        return redirect('index_dish')
    except Dish.DoesNotExist:
        return redirect('index_dish')

def deleteIngridient(request, pk):
    try:
        dish = Ingridient.objects.get(pk=pk)
        dish.delete()
        return redirect('index_ingridient')
    except Ingridient.DoesNotExist:
        return redirect('index_ingridient')