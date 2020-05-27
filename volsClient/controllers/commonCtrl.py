# -*- coding: utf-8 -*-
import requests_async as requests
import traceback


async def make_get_request(url):
    try:
        response = await requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception:
        print(traceback.format_exc())
        return None


async def make_post_request(url, data):
    try:
        response = await requests.post(url, json=data)
        if response.status_code == 200:
            return True
    except Exception:
        print(traceback.format_exc())
        return False


async def make_delete_request(url, data=None):
    try:
        response = await requests.delete(url, json=data)
        if response.status_code == 200:
            return True
    except Exception:
        print(traceback.format_exc())
        return False


async def make_put_request(url, data):
    try:
        response = await requests.put(url, json=data)
        if response.status_code == 200:
            return True
    except Exception:
        print(traceback.format_exc())
        return False
