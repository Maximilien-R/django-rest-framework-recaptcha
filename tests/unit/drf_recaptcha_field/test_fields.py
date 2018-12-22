import pytest

from rest_framework import serializers

from rest_framework_recaptcha.fields import ReCaptchaField
from rest_framework_recaptcha.validators import ReCaptchaValidator

try:
    from unittest import mock
except ImportError:
    import mock


@pytest.mark.parametrize(
    ("params", "expected"),
    [
        ({}, True),
        (
            {"write_only": False},
            False,
        ),
        (
            {"write_only": True},
            True,
        ),
    ],
)
def test_recaptchafield_write_only(params, expected):
    field = ReCaptchaField(**params)
    assert field.write_only is expected


def test_recaptchafield_has_recaptcha_validator():
    field = ReCaptchaField()

    nb_validators = len(field.validators)
    assert nb_validators > 0
    assert isinstance(field.validators[nb_validators - 1], ReCaptchaValidator)


@pytest.mark.parametrize(
    ("messages", "recaptcha_response", "expected_error"),
    [
        (
            {"bad-request": "bad-request"},
            {"success": False, "error-codes": ["bad-request"]},
            "bad-request",
        ),
        (
            {"invalid-input-response": "invalid-input-response"},
            {"success": False, "error-codes": ["invalid-input-response"]},
            "invalid-input-response",
        ),
        (
            {"invalid-input-secret": "invalid-input-secret"},
            {"success": False, "error-codes": ["invalid-input-secret"]},
            "invalid-input-secret",
        ),
        (
            {"missing-input-response": "missing-input-response"},
            {"success": False, "error-codes": ["missing-input-response"]},
            "missing-input-response",
        ),
        (
            {"missing-input-secret": "missing-input-secret"},
            {"success": False, "error-codes": ["missing-input-secret"]},
            "missing-input-secret",
        ),
        (
            {"timeout-or-duplicate": "timeout-or-duplicate"},
            {"success": False, "error-codes": ["timeout-or-duplicate"]},
            "timeout-or-duplicate",
        ),
    ]
)
def test_recaptchafield_validation_default_error_messages_error(
    messages, recaptcha_response, expected_error
):
    class CustomReCaptchaField(ReCaptchaField):
        default_error_messages = messages

    field = CustomReCaptchaField()

    nb_validators = len(field.validators)
    assert nb_validators > 0
    assert isinstance(field.validators[nb_validators - 1], ReCaptchaValidator)

    field.validators[nb_validators - 1]._get_recaptcha_response = mock.Mock(
        return_value=recaptcha_response
    )

    with pytest.raises(serializers.ValidationError) as excinfo:
        field.run_validators("token")

    assert expected_error in str(excinfo.value)


@pytest.mark.parametrize(
    ("messages", "recaptcha_response", "expected_error"),
    [
        (
            {"bad-request": "bad-request"},
            {"success": False, "error-codes": ["bad-request"]},
            "bad-request",
        ),
        (
            {"invalid-input-response": "invalid-input-response"},
            {"success": False, "error-codes": ["invalid-input-response"]},
            "invalid-input-response",
        ),
        (
            {"invalid-input-secret": "invalid-input-secret"},
            {"success": False, "error-codes": ["invalid-input-secret"]},
            "invalid-input-secret",
        ),
        (
            {"missing-input-response": "missing-input-response"},
            {"success": False, "error-codes": ["missing-input-response"]},
            "missing-input-response",
        ),
        (
            {"missing-input-secret": "missing-input-secret"},
            {"success": False, "error-codes": ["missing-input-secret"]},
            "missing-input-secret",
        ),
        (
            {"timeout-or-duplicate": "timeout-or-duplicate"},
            {"success": False, "error-codes": ["timeout-or-duplicate"]},
            "timeout-or-duplicate",
        ),
    ]
)
def test_recaptchafield_validation_messages_error(
    messages, recaptcha_response, expected_error
):
    field = ReCaptchaField(error_messages=messages)

    nb_validators = len(field.validators)
    assert nb_validators > 0
    assert isinstance(field.validators[nb_validators - 1], ReCaptchaValidator)

    field.validators[nb_validators - 1]._get_recaptcha_response = mock.Mock(
        return_value=recaptcha_response
    )

    with pytest.raises(serializers.ValidationError) as excinfo:
        field.run_validators("token")

    assert expected_error in str(excinfo.value)
