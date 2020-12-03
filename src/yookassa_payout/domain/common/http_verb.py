# -*- coding: utf-8 -*-


class HttpVerb(object):
    """
    Constants representing http method verbs. Available values are:

    * yookassa_payout.domain.common.HttpVerb.GET
    * yookassa_payout.domain.common.HttpVerb.POST
    * yookassa_payout.domain.common.HttpVerb.PUT
    * yookassa_payout.domain.common.HttpVerb.PATCH
    * yookassa_payout.domain.common.HttpVerb.HEAD
    * yookassa_payout.domain.common.HttpVerb.OPTIONS
    * yookassa_payout.domain.common.HttpVerb.DELETE
    """
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    HEAD = 'head'
    OPTIONS = 'options'
    DELETE = 'delete'
