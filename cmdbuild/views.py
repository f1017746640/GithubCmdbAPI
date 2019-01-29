# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from func import cmdbuild_token
from func import cmdbuild_class
from func import cmdbuild_env
from func import cmdbuild_business
from func import cmdbuild_server


def test_httpresponse(request):
    return HttpResponse('test')


def response_cmdbuild_token(request):
    token = cmdbuild_token()
    if token:
        return HttpResponse(token)
    else:
        return HttpResponse('error', status=500)


def response_cmdbuild_classes(request):
    classes = cmdbuild_class()
    return HttpResponse(classes)


def response_cmdbuild_env(request):
    env = cmdbuild_env()
    return HttpResponse(env)


def response_cmdbuild_business(request):
    business = cmdbuild_business()
    return HttpResponse(business)


def response_cmdbuild_server(request):
    server = cmdbuild_server()
    return HttpResponse(server)
