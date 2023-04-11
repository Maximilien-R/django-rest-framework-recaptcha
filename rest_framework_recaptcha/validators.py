import json

from ipware import get_client_ip
from rest_framework import serializers

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

from rest_framework_recaptcha.compat import urlencode, urlopen
from rest_framework_recaptcha.conf import settings

_DEFAULT_ERROR_CODE = "bad-request"

_ERROR_MESSAGES = {
    _DEFAULT_ERROR_CODE: _("The request is invalid or malformed."),
    "invalid-input-response": _(
        "The response parameter is invalid or malformed."
    ),
    "invalid-input-secret": _("The secret parameter is invalid or malformed."),
    "missing-input-response": _("The response parameter is missing."),
    "missing-input-secret": _("The secret parameter is missing."),
    "timeout-or-duplicate": _(
        "The response parameter has timed out or has already been used."
    ),
}


class ReCaptchaValidator(object):
    """
    A validator which check the reCAPTCHA response token.
    """

    def __init__(self, messages=None):
        """
        Initializes the validator with verify API endpoint and reCAPTCHA
        application's secret key.
        """
        self._api_url = getattr(
            settings, "DRF_RECAPTCHA_VERIFY_ENDPOINT", None
        )
        self._secret_key = getattr(settings, "DRF_RECAPTCHA_SECRET_KEY", None)
        self._client_ip = None

        self._error_messages = _ERROR_MESSAGES.copy()
        self._error_messages.update(messages or {})

    def __call__(self, value):
        """
        Performs the validation on the reCAPTCHA response token.
        :param value: reCAPTCHA response token
        :return: string
        """
        if not (self._api_url and self._secret_key):
            raise ImproperlyConfigured(
                "`DRF_RECAPTCHA_VERIFY_ENDPOINT` and "
                "`DRF_RECAPTCHA_SECRET_KEY` should be both defined."
            )

        response = self._get_recaptcha_response(value)
        if not response.get("success", False):
            error_codes = response.get("error-codes", [])
            if error_codes and error_codes[0] in self._error_messages:
                raise serializers.ValidationError(
                    self._error_messages[error_codes[0]]
                )
            raise serializers.ValidationError(
                self._error_messages[_DEFAULT_ERROR_CODE]
            )
        return value

    def set_context(self, serializer_field):
        """
        Try to determine the client ip address.
        :param serializer_field: reCAPTCHA field instance
        """
        try:
            self._client_ip, _ = get_client_ip(
                serializer_field.context.get("request")
            )
        except AttributeError:
            pass

    def _get_recaptcha_response(self, value):
        """
        Calls the verify API endpoint and return its response.
        :param value: reCAPTCHA response token
        :return: dict
        """
        values = {"secret": self._secret_key, "response": value}
        if self._client_ip:
            values["remoteip"] = self._client_ip

        data = urlencode(values).encode("ascii")

        try:
            with urlopen(self._api_url, data) as handler:
                return json.loads(handler.read().decode("utf-8"))
        except Exception:
            raise serializers.ValidationError(
                self._error_messages[_DEFAULT_ERROR_CODE]
            )
