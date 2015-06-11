from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_s3.django_s3.forms import UploadFileForm
from django_s3.django_s3.utils import s3_connect


def home(request):
    form = UploadFileForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            conn = s3_connect()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadFileForm()


    context = {
        'form': form,
    }

    return render(request, 'home.html', context)
