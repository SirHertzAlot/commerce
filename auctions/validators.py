from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_bid(value, old_value):
    if value > old_value:
        return value
    else:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )
