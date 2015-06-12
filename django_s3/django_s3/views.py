from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_s3.django_s3.forms import UploadFileForm
from django_s3.django_s3.utils import s3_connect
from django_s3.settings import AWS_S3_BUCKET_ID


def home(request):
    form = UploadFileForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadFileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            # upload to s3
            from boto.s3.key import Key
            conn = s3_connect()
            bucket = conn.get_bucket(AWS_S3_BUCKET_ID)
            key = Key(bucket)
            upload_file = request.FILES['upload_file']
            key.key = upload_file.name
            key.set_contents_from_file(upload_file)

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadFileForm()


    context = {
        'form': form,
    }

    return render(request, 'home.html', context)
