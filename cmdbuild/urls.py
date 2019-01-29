#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: urls.py
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/13 下午3:28
"""

from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.test_httpresponse),
    url(r'^token/', views.response_cmdbuild_token),
    url(r'^classes/', views.response_cmdbuild_classes),
    url(r'^env/', views.response_cmdbuild_env),
    url(r'^business/', views.response_cmdbuild_business),
    url(r'^server/', views.response_cmdbuild_server),
]
