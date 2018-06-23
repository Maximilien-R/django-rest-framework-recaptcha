import pytest

from rest_framework import serializers

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from drf_recaptcha_field import validators

try:
    from unittest import mock
except ImportError:
    import mock


@pytest.mark.parametrize(
    ("secret_key", "api_url"),
    [
        (None, None),
        (None, "DRF_RECAPTCHA_FIELD_VERIFY_ENDPOINT"),
        ("DRF_RECAPTCHA_FIELD_SECRET_KEY", None),
    ],
)
def test_recaptchavalidator_call_improperly_configured(
    monkeypatch, api_url, secret_key
):
    monkeypatch.setattr(settings, "DRF_RECAPTCHA_FIELD_SECRET_KEY", secret_key)
    monkeypatch.setattr(
        settings, "DRF_RECAPTCHA_FIELD_VERIFY_ENDPOINT", api_url
    )

    validator = validators.ReCaptchaValidator()

    with pytest.raises(ImproperlyConfigured) as excinfo:
        validator("token")

    assert str(excinfo.value) == (
        "`DRF_RECAPTCHA_FIELD_VERIFY_ENDPOINT` and "
        "`DRF_RECAPTCHA_FIELD_SECRET_KEY` should be both defined."
    )


@pytest.mark.parametrize(
    ("recaptcha_response", "expected_error"),
    [
        (
            {},
            "The request is invalid or malformed."
        ),
        (
            {"success": False},
            "The request is invalid or malformed."
        ),
        (
            {"success": False, "error-codes": []},
            "The request is invalid or malformed.",
        ),
        (
            {"success": False, "error-codes": ["unknown"]},
            "The request is invalid or malformed.",
        ),
        (
            {
                "success": False,
                "error-codes": ["unknown", "invalid-input-response"],
            },
            "The request is invalid or malformed.",
        ),
        (
            {"success": False, "error-codes": ["bad-request"]},
            "The request is invalid or malformed.",
        ),
        (
            {"success": False, "error-codes": ["invalid-input-response"]},
            "The response parameter is invalid or malformed.",
        ),
        (
            {"success": False, "error-codes": ["invalid-input-secret"]},
            "The secret parameter is invalid or malformed.",
        ),
        (
            {"success": False, "error-codes": ["missing-input-response"]},
            "The response parameter is missing.",
        ),
        (
            {"success": False, "error-codes": ["missing-input-secret"]},
            "The secret parameter is missing.",
        ),
        (
            {
                "success": False,
                "error-codes": ["missing-input-secret", "bad-request"],
            },
            "The secret parameter is missing.",
        ),
    ],
)
def test_recaptchavalidator_call_validation_error(
    recaptcha_response, expected_error
):
    validator = validators.ReCaptchaValidator()
    validator._get_recaptcha_response = mock.Mock(
        return_value=recaptcha_response
    )

    with pytest.raises(serializers.ValidationError) as excinfo:
        validator("token")

    assert expected_error in str(excinfo.value)


def test_recaptchavalidator_call__success():
    validator = validators.ReCaptchaValidator()
    validator._get_recaptcha_response = mock.Mock(
        return_value={"success": True}
    )
    assert validator("token") == "token"


@pytest.mark.parametrize(
    "serializer_field",
    [
        None,
        {},
        mock.Mock(context={}),
        mock.Mock(context={"request": None}),
        mock.Mock(context={"request": mock.Mock(META=None)}),
    ],
)
def test_recaptchavalidator_set_context_attributeerror(serializer_field):
    validator = validators.ReCaptchaValidator()
    assert validator._client_ip is None
    validator.set_context(serializer_field)
    assert validator._client_ip is None


def test_recaptchavalidator_set_context():
    validator = validators.ReCaptchaValidator()
    assert validator._client_ip is None
    serializer_field = mock.Mock(
        context={
            "request": mock.Mock(META={"HTTP_X_FORWARDED_FOR": "172.10.20.3"})
        }
    )
    validator.set_context(serializer_field)
    assert validator._client_ip == "172.10.20.3"


def test_recaptchavalidator_get_recaptcha_response():
    validator = validators.ReCaptchaValidator()

    cm = mock.MagicMock()
    cm.decode.return_value = '{"success": true}'
    cm.read.return_value = cm
    cm.__enter__.return_value = cm

    with mock.patch.object(
        validators, "urlencode", wraps=validators.urlencode
    ) as urlencode_mock:
        with mock.patch.object(validators, "urlopen") as urlopen_mock:
            urlopen_mock.return_value = cm
            read_mock = urlopen_mock.return_value.read

            assert validator._get_recaptcha_response("token") == {
                "success": True
            }

            assert read_mock.called
            assert urlopen_mock.call_count == 1

            assert read_mock.called
            assert read_mock.call_count == 1

            read_mock.return_value.decode.assert_called_once_with("utf-8")

        urlencode_mock.assert_called_once_with(
            {"secret": "DRF_RECAPTCHA_FIELD_SECRET_KEY", "response": "token"}
        )


def test_recaptchavalidator_get_recaptcha_response_throw_exception():
    validator = validators.ReCaptchaValidator()

    with mock.patch.object(
        validators, "urlencode", return_value="encoded"
    ) as urlencode_mock:
        with mock.patch.object(
            validators, "urlopen", side_effect=[Exception()]
        ) as urlopen_mock:
            with pytest.raises(serializers.ValidationError) as excinfo:
                validator._get_recaptcha_response("token")
            urlopen_mock.assert_called_once_with(
                "DRF_RECAPTCHA_FIELD_VERIFY_ENDPOINT", b"encoded"
            )
        urlencode_mock.assert_called_once_with(
            {"secret": "DRF_RECAPTCHA_FIELD_SECRET_KEY", "response": "token"}
        )
    assert "The request is invalid or malformed" in str(excinfo.value)
