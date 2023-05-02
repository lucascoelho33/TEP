from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.salvar()
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})

# Create your views here.
