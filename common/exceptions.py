from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.fields import get_error_detail

from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    """
        Sometimes in your Django model you want to raise a ``ValidationError`` in the ``save`` method, for
        some reason.
        This exception is not managed by Django Rest Framework because it occurs after its validation
        process. So at the end, you'll have a 500.
        Correcting this is as simple as overriding the exception handler, by converting the Django
        ``ValidationError`` to a DRF one.
    """
    if isinstance(exc, DjangoValidationError):
        exc = DRFValidationError(detail=get_error_detail(exc))

    return drf_exception_handler(exc, context)
