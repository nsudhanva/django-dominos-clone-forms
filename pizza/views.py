from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)

        if filled_form.is_valid():
            note = 'Thanks for ordering! Your %s %s and %s is on its way' % (filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': new_form, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form})