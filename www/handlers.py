# coding=utf-8

'handlers'

__author__ = 'yuyingqi'
__email__ = 'yuyingqijack@163.com'
__version__ = 1.0

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get,post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
