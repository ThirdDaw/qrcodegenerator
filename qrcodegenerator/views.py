from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_qr(request):
    return redirect('home_url', permanent=True)
