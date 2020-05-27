# -*- coding: utf-8 -*-
import asyncio
from controllers import commonCtrl

base_url = 'http://127.0.0.1:3000/level/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_data(level_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + level_id))


def insert(level_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, level_data))


def update(level_id, level_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + level_id, level_data))


def delete(level_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + level_id))