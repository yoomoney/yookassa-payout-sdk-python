# -*- coding: utf-8 -*-
from yookassa_payout.domain.exceptions.api_error import ApiError


class ResponseProcessingError(ApiError):
    HTTP_CODE = 202
