import pytest

from drf_recaptcha_field.fields import ReCaptchaField
from drf_recaptcha_field.validators import ReCaptchaValidator


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
    assert len(field.validators) == 1
    assert isinstance(field.validators[0], ReCaptchaValidator)
