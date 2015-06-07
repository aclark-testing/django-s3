from django.shortcuts import render
from .forms import UploadFileForm


def home(request):
    form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)
