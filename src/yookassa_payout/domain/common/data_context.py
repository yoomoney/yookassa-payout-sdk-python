# -*- coding: utf-8 -*-
from yookassa_payout.domain.common.context import Context


class DataContext(Context):
    """
    Constants representing context data types. Available values are:

    * yookassa_payout.domain.common.DataContext.REQUEST
    * yookassa_payout.domain.common.DataContext.RESPONSE
    """
    REQUEST = 'request'
    RESPONSE = 'response'
