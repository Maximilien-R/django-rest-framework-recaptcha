from rest_framework import serializers

from rest_framework_recaptcha.validators import ReCaptchaValidator


class ReCaptchaField(serializers.CharField):
    """
    reCAPTCHA serializer field to use within a Django REST framework serializer
    in order to validate a reCAPTCHA response token.
    """

    def __init__(self, write_only=True, **kwargs):
        """
        Initializes the reCAPTCHA field as write only by default and append
        the ReCaptchaValidator to its validators list.
        :param write_only: determines whether or not the field is write only
        """
        super(ReCaptchaField, self).__init__(write_only=write_only, **kwargs)
        self.validators.append(
            ReCaptchaValidator(messages=self.error_messages)
        )
