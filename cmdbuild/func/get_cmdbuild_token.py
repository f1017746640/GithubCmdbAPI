#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: get_cdmbuild_token
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/13 下午8:01
"""
import json
import requests
from cmdbuild.config import *


def cmdbuild_token():
    url = PRE_CMDB + MID_CMDB + PRO_SESSION

    payload = {
        "username": USER_NAME,
        "password": PASSWORD
    }

    headers = {
        'Content-Type': "application/json"
    }

    try:
        response = requests.request("POST",
                                    url,
                                    data=json.dumps(payload),
                                    headers=headers)

        # print(response.text)
        token = response.json()['data']['_id']
        return token
    except Exception as e:
        print(e)
        return
