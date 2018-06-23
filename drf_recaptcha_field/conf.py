from django.conf import settings  # noqa: F401

from appconf import AppConf


class DRFReCaptchaFieldConf(AppConf):
    """
    DRF reCAPTCHA settings.
    """

    VERIFY_ENDPOINT = "https://www.google.com/recaptcha/api/siteverify"

    SECRET_KEY = None
