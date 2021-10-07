from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def home(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            meesage = form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            meesage = form.cleaned_data.get('message')
            
            messages.success(request, 'You Form was successfully uploaded ' + name)

        return redirect('home')

    context = {'form':form}
    return render(request, 'armedRDS/index.html', context)