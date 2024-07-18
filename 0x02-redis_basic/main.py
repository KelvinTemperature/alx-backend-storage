#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('web').get_page

page = Cache('http://slowwly.robertomurray.co.uk')

print(page.data_catcher)
