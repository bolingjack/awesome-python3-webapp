# coding=utf-8

import logging
import asyncio, os, json, time
import aiomysql


@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool

    __pool = yield from aiomysql.create_pool()(
        host=kw.get('host', 'yuyingqi-develop.cszis4r93tw8.rds.cn-north-1.amazonaws.com.cn'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 1),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


@asyncio.coroutine
def select(sql,args,sizr=None):
    logging.log(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from