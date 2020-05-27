# -*- coding: utf-8 -*-
import asyncio
from controllers import commonCtrl

base_url = 'http://127.0.0.1:3000/event/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_name(event_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + event_id + '/name'))


def get_all_names():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all/names'))


def get_data(event_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + event_id))


def get_volunteers(event_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + event_id + '/volunteers'))


def get_counted_volunteers(event_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + event_id + '/volunteers/counted'))


def insert(event_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, event_data))


def update(event_id, event_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + event_id, event_data))


def delete(event_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + event_id))
