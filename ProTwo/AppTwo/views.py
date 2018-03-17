from django.shortcuts import render
from AppTwo.models import User

from AppTwo.forms import NewUserForm

def index(request):
    context_dic = {
        'heading': 'WELCOME!'
    }
    return render(request, 'AppTwo/index.html', context=context_dic)


def detail(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request, 'AppTwo/detail.html', {'form': form})