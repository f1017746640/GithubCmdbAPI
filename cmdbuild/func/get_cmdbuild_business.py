#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: get_cmdbuild_business.py
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/14 下午5:57
"""
import requests
from .get_cmdbuild_token import cmdbuild_token
from cmdbuild.config import *
from cmdbuild.CmdbClassAPI import cmdb_class_api

BUSINESS = cmdb_class_api('BUSINESS')['cls']


def cmdbuild_business():
    token = cmdbuild_token()
    if token:
        url = URI_CLASS + BUSINESS + "/cards"

        headers = {
          'Content-Type': "application/json",
          'CMDBuild-Authorization': token
        }

        response = requests.request("GET",
                                    url,
                                    headers=headers)

        print(response.text)
        return response.text
    else:
        return
