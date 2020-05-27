# -*- coding: utf-8 -*-
from controllers import commonCtrl
import asyncio


base_url = 'http://127.0.0.1:3000/request/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_data(request_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + request_id))


def insert(request_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, request_data))


def update(request_id, request_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + request_id, request_data))


def delete(request_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + request_id))

