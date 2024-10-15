from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm

@login_required(login_url='login')
def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inputbook')
    else:
        form = BookForm()
    return render(request, 'book/inputbook.html', {'form': form})