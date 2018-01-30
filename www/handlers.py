# coding=utf-8

'handlers'

__author__ = 'yuyingqi'
__email__ = 'yuyingqijack@163.com'
__version__ = 1.0

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
