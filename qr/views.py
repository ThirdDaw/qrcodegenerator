from django.shortcuts import render

import qrcode
import time


def home(request):
    return render(request, "qr/index.html")


def about_us(request):
    return render(request, "qr/about-us.html")


def generate_qr_first_format(request):
    context = generation(qrcode.constants.ERROR_CORRECT_L, request)
    return render(request, "qr/first-format.html", context=context)


def generate_qr_second_format(request):
    context = generation(qrcode.constants.ERROR_CORRECT_M, request)
    return render(request, "qr/first-format.html", context=context)


def generate_qr_third_format(request):
    context = generation(qrcode.constants.ERROR_CORRECT_H, request)
    return render(request, "qr/first-format.html", context=context)


def generate_qr_fourth_format(request):
    context = generation(qrcode.constants.ERROR_CORRECT_Q, request)
    return render(request, "qr/first-format.html", context=context)


# Generating QR code from given url-data. Saving image and returning context.
def generation(qr_format, request):
    qr = qrcode.QRCode(
        box_size=10,
        border=4,
        error_correction=qr_format
    )
    qr.make(fit=True)

    data = request.GET.get('data', '')

    image_name = str(time.time_ns())

    qr.add_data(data=data)

    img = qr.make_image()

    context = {
        "image": image_name + ".jpg",
        "status": image_name
    }

    img.save("static/results/" + image_name + ".jpg")

    return context
