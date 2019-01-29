#!/usr/bin/env python
# encoding: utf-8
"""
  > FileName: CmdbClassAPI.py
  > Author: FZH
  > Mail: fzh42353@ly.com
  > CreatedTime: 18/12/18 下午6:38
"""
import os
import yaml

curPath = os.path.dirname(os.path.realpath(__file__))
yamlPath = os.path.join(curPath, "CmdbClass.yaml")

f = open(yamlPath, 'r')
cfg = f.read()

dit = yaml.load(cfg)


def cmdb_class_api(cls):
    return dit[cls]
