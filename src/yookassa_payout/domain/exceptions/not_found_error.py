# -*- coding: utf-8 -*-
from yookassa_payout.domain.exceptions.api_error import ApiError


class NotFoundError(ApiError):
    HTTP_CODE = 404
