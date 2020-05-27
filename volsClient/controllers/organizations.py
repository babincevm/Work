# -*- coding: utf-8 -*-
from controllers import commonCtrl
import asyncio


base_url = 'http://127.0.0.1:3000/organization/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_data(org_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + org_id))


def get_names():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'names/all'))


def get_name(org_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + org_id + '/name'))


def get_all_events(org_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + org_id + '/events'))


def insert(organization_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, organization_data))


def update(org_id, organization_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + org_id, organization_data))


def delete(org_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + org_id))


def get_counted_events(org_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + org_id + '/events/counted'))
