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
from cmdbuild.CmdbClassAPI import cmdb_class_api

SESSIONS = cmdb_class_api('SESSIONS')['cls']


def cmdbuild_token():

    url = URI_TOKEN + SESSIONS

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
