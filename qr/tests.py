from django.test import TestCase
from django.http import HttpRequest

from .views import *


class QRTestCase(TestCase):

    def test_qr_generation_L(self):
        test = generation(qrcode.constants.ERROR_CORRECT_L, HttpRequest())
        self.assertLess(int(test["status"]), time.time_ns())

    def test_qr_generation_M(self):
        test = generation(qrcode.constants.ERROR_CORRECT_M, HttpRequest())
        self.assertLess(int(test["status"]), time.time_ns())

    def test_qr_generation_H(self):
        test = generation(qrcode.constants.ERROR_CORRECT_H, HttpRequest())
        self.assertLess(int(test["status"]), time.time_ns())

    def test_qr_generation_Q(self):
        test = generation(qrcode.constants.ERROR_CORRECT_Q, HttpRequest())
        self.assertLess(int(test["status"]), time.time_ns())
