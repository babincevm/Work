# -*- coding: utf-8 -*-
from controllers import commonCtrl
import asyncio

base_url = 'http://127.0.0.1:3000/center/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_data(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id))


def get_names():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all/names'))


def get_name(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/name'))


def get_volunteers(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/volunteers'))


def get_events(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/events'))


def get_organizations(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/organizations'))


def delete(center_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + center_id))


def update(center_id, update_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + center_id, update_data))


def insert(center_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, center_data))


def get_total_volunteers(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/volunteers/total'))


def get_total_organizations(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/organizations/total'))


def get_total_events(center_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + center_id + '/events/total'))
