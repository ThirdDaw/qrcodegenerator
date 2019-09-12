from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="home_url"),
    path('gff', generate_qr_first_format, name="generate_qr_first_format_url"),
    path('gsf', generate_qr_second_format, name="generate_qr_second_format_url"),
    path('gtf', generate_qr_third_format, name="generate_qr_third_format_url"),
    path('gfff', generate_qr_fourth_format, name="generate_qr_fourth_format_url"),
    path('about', about_us, name="about_us_url"),
]