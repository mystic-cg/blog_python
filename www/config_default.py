#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by PyCharm
# @author  : mystic
# @date    : 2017/11/11 21:00
"""
    Default Configuration
"""

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'Ghost007!',
        'db': 'blog_python'
    },
    'session': {
        'secret': 'mystic'
    }
}