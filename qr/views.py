from django.shortcuts import render
from django.http import HttpResponse

import qrcode
import time


def home(request):
    return render(request, "qr/index.html")


def about_us(request):
    return render(request, "qr/about-us.html")


def generate_qr_first_format(request):
    qr = qrcode.QRCode(
        box_size=10,
        border=4,
    )
    qr.make(fit=True)

    data = request.GET.get('data', '')
    print(data)

    # image_name = str(int(round(time.time() * 1000))) + "result"
    image_name = str(data)

    qr.add_data(data=data)

    img = qr.make_image()

    context = {
        "image": image_name + ".jpg",
        "status": image_name
    }

    img.save("static/results/" + image_name + ".jpg")
    # img.save(image_name + ".jpg")
    print(context["image"])
    return render(request, "qr/first-format.html", context=context)


def generate_qr_second_format(request):
    qr = qrcode.QRCode(
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr.make(fit=True)

    data = request.GET.get('data', '')
    print(data)

    # image_name = str(int(round(time.time() * 1000))) + "result"
    image_name = str(data)

    qr.add_data(data=data)

    img = qr.make_image()

    context = {
        "image": image_name + ".jpg",
        "status": image_name

    }

    img.save("static/results/" + image_name + ".jpg")
    print(context["image"])
    return render(request, "qr/second-format.html", context=context)


def generate_qr_third_format(request):
    qr = qrcode.QRCode(
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    qr.make(fit=True)

    data = request.GET.get('data', '')
    print(data)

    # image_name = str(int(round(time.time() * 1000))) + "result"
    image_name = str(data)

    qr.add_data(data=data)

    img = qr.make_image()

    context = {
        "image": image_name + ".jpg",
        "status": image_name

    }

    img.save("static/results/" + image_name + ".jpg")
    print(context["image"])
    return render(request, "qr/third-format.html", context=context)


def generate_qr_fourth_format(request):
    qr = qrcode.QRCode(
        box_size=10,
        border=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
    )
    qr.make(fit=True)

    data = request.GET.get('data', '')
    print(data)

    # image_name = str(int(round(time.time() * 1000))) + "result"
    image_name = str(data)

    qr.add_data(data=data)

    img = qr.make_image()

    context = {
        "image": image_name + ".jpg",
        "status": image_name

    }

    img.save("static/results/" + image_name + ".jpg")
    print(context["image"])
    return render(request, "qr/fourth-format.html", context=context)
