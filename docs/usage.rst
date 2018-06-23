Usage
=====

To use DRF reCAPTCHA field within your project you'll need to import and add
the ``ReCaptchaField`` serializer field into the wanted serializer. For example:

.. code-block:: python

    from rest_framework import serializers
    from drf_recaptcha_field import ReCaptchaField


    class MySerializer(serializers.Serializer):
        recaptcha = ReCaptchaField()

For you information, ``ReCaptchaField`` fields are defined as
``write_only=True`` by default.

Once your serializer is configured with your ``ReCaptchaField`` you'll be able to
send the client side generated reCAPTCHA response token and validate it
server side (cf. `reCAPTCHA documentation <https://developers.google.com/recaptcha/docs/verify>`_).
