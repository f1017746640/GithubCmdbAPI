#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: get_cmdbuild_os.py
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/14 下午2:56
"""
import requests
from cmdbuild.config import *
from .get_cmdbuild_token import cmdbuild_token
from cmdbuild.CmdbClassAPI import cmdb_class_api

CLASS = cmdb_class_api('CLASS')['cls']


def cmdbuild_class():
    token = cmdbuild_token()
    if token:
        url = URI_CLASS

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


