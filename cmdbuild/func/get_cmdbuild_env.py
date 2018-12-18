#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: get_cmdbuild_os.py
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/14 下午5:42
"""

from .get_cmdbuild_token import cmdbuild_token
import requests


def cmdbuild_env():
    token = cmdbuild_token()
    if token:
        url = "http://10.100.172.112:8080/services/rest/v2/classes/env/cards"

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
