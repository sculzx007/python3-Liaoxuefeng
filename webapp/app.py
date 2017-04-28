#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time

from datetime import datetime
from aiohttp import web

def index(request):
	return web.Response(body = b'<h1>Awesome</h1>')

#打印SQL语句
def log(sql, args = ()):
	logging.info('SQL: %s' %(sql))


# 创建一个全局的连接池，每个http请求都从池中获得数据库连接
@asyncio.coroutine
def create_pool(loop, **kw):
	logging.info('Create database connection pool...')

	# 全局变量 __pool用于存储整个连接池
	global __pool
	__pool = yield from aiomysql.create_pool(
		# **kw 参数可以包含所有连接需要用到的关键字参数
		# 
		# host 默认本机IP
		host = kw.get('host', 'localhost'),
		port = kw.get('port', 3306),
		user = kw['user'],
		password = kw['password'],
		db = kw['db'],
		charset = kw.get('charset', 'utf8'),
		autocommit = kw.get('autocommit', True),
		
		#默认最大连接数为10
		maxsize = kw.get('maxsize',10),
		minsize = kw.get('minsize',1),
		
		#接收一个event_loop实例
		loop = loop
		)

# 封装SQL的SELECT语句为select()函数
@asyncio.coroutine
def select(sql, args,size = None):
	log(sql, args)
	global __pool

	# yield from 将会调用一个子协程，并直接返回调用的结果
	# yield from 从 __pool 连接池中返回一个连接 conn
	with (yield from __pool) as conn:

		# DictCursor 属性是将cursor的结果返回成字典
		cur = yield from conn.cursor(aiomysql.DictCursor)

		# 执行SQL语句
		# SQL的占位符为 “？”，MySQL的占位符为 “%s”
		yield from cur.execute(sql.replace('?', '&s'), args or ())

		#根据指定的size，返回查询结果
		if size:
			rs = yield from cur.fetchmany(size)
		else:
			# 返回所有查询结果
			rs = yield from cur.fetchall()

		yield from cur.close()
		logging.info('Rows returned: %s' % len(rs))
		return rs

# 封装 INSERT，UPDATE，DELETE
# 语句操作参数一样，所有定义一个通用的执行函数 execute()
# 返回操作影响的行号
@asyncio.coroutine
def execute(sql, args):
	log(sql)

	with (yield from __pool) as conn:
		try:
			# execute类型的SQL操作返回的结果只有行号，所有不需要用DictCursor
			cur = yield from conn.cursor
			yield from cur.execute(sql.replace('?', '%s'), args)
			affected = cur.rowcount
			yield from cur.close()
		except BaseException as e:
			raise

		return affected


def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()