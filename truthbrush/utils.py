from datetime import timezone
from dateutil import parser as date_parse


"""Utility Functions"""


def as_datetime(date_str):
    """Datetime formatter function. Ensures timezone is UTC."""
    return date_parse.parse(date_str).replace(tzinfo=timezone.utc)
