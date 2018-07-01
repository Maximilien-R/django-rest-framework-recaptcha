Usage
=====

To use Django REST framework reCAPTCHA within your project you'll need to
import and add the ``ReCaptchaField`` serializer field into the wanted
serializer. For example:

.. code-block:: python

    from rest_framework import serializers
    from rest_framework_recaptcha import ReCaptchaField


    class MySerializer(serializers.Serializer):
        recaptcha = ReCaptchaField()

For you information, ``ReCaptchaField`` fields are defined as
``write_only=True`` by default.

Once your serializer is configured with your ``ReCaptchaField`` you'll be able to
send the client side generated reCAPTCHA response token and validate it
server side (cf. `reCAPTCHA documentation <https://developers.google.com/recaptcha/docs/verify>`_).

Validation errors
=================

During the validation process of the reCAPTCHA response token by the
verification API and according to the `documentation`_, the following errors
may be raised:

.. _documentation: https://developers.google.com/recaptcha/docs/verify#error-code-reference

======================  ==============================================================
Error code              Message
======================  ==============================================================
missing-input-secret    The secret parameter is missing.
invalid-input-secret    The secret parameter is invalid or malformed.
missing-input-response  The response parameter is missing.
invalid-input-response  The response parameter is invalid or malformed.
bad-request             The request is invalid or malformed.
timeout-or-duplicate    The response parameter has timed out or has already been used.
======================  ==============================================================

Each of these errors are handled by the ``ReCaptchaValidator``. In case of an
unknown error the ``bad-request`` error will be raised.

Each error message can be replaced if needed. For this, you have two options:

1. Create a custom ``ReCaptchaField`` that inherits from ``ReCaptchaField``
   while redefining the ``default_error_messages`` attribute with a dictionary
   which for each entry the key will match the code to override and the value
   to the new message. Example:

.. code-block:: python

    from rest_framework import serializers
    from rest_framework_recaptcha import ReCaptchaField


    class MyReCaptchaField(ReCaptchaField):
        default_error_messages = {
            "invalid-input-response": "reCAPTCHA token is invalid.",
        }


    class MySerializer(serializers.Serializer):
        recaptcha = MyReCaptchaField()

2. When adding the ``ReCaptchaField`` field to your serializer you can pass the
   optional ``error_messages`` parameter with a dictionary which for each entry
   the key will match the code to override and the value to the new message.
   Example:

.. code-block:: python

    from rest_framework import serializers
    from rest_framework_recaptcha import ReCaptchaField


    class MySerializer(serializers.Serializer):
        recaptcha = ReCaptchaField(
            error_messages={
                "invalid-input-response": "reCAPTCHA token is invalid.",
            }
        )
