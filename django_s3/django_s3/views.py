from django.shortcuts import response


def home(request):
    return response(request, 'templates/home.html')
