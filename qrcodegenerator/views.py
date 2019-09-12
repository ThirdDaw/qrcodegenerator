from django.http import HttpResponse


def generateQR(request):
    return HttpResponse("<h1>Hello</h1>")