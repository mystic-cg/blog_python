#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by PyCharm
# @author  : mystic
# @date    : 2017/11/9 14:25
"""
    async web application.
"""
import asyncio
import logging

from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Mystic</h1>', content_type='text/html')


async def init(loop_):
    app = web.Application(loop=loop_)
    app.router.add_route('GET', '/', index)
    server = await loop_.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
