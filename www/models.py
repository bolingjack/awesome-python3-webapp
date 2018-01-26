# coding=utf-8

'Model'

__author__ = 'yuyingqi'
__email__ = 'yuyingqijack@163.com'
__version__ = 1.0

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField


def next_id():
    '''生成id，十五位时间戳加32位uuid加000'''
    print(len(uuid.uuid4().hex))
    return "%015d%s000" % (int(time.time() * 1000), uuid.uuid4().hex)


print(next_id())
