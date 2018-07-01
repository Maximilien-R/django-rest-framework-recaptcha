from django.conf import settings  # noqa: F401

from appconf import AppConf


class DRFReCaptchaConf(AppConf):
    """
    Django REST framework reCAPTCHA settings.
    """

    VERIFY_ENDPOINT = "https://www.google.com/recaptcha/api/siteverify"

    SECRET_KEY = None
