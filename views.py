# encoding: utf8

import logging
from rest_framework.views import exception_handler as base_exception_handler

_logger = logging.getLogger('app.rest_framework')


def exception_handler(exc, context):
    _logger.warn(exc)
    return base_exception_handler(exc, context)
