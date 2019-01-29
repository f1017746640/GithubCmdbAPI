#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: get_cmdbuild_os.py
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/14 下午5:42
"""
from cmdbuild.config import *
from .get_cmdbuild_token import cmdbuild_token
from cmdbuild.CmdbClassAPI import cmdb_class_api
import requests

ENV = cmdb_class_api('ENV')['cls']


def cmdbuild_env():
    token = cmdbuild_token()
    if token:
        url = URI_CLASS + ENV + "/cards"

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
