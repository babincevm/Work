# -*- coding: utf-8 -*-
import asyncio
from controllers import commonCtrl

base_url = 'http://127.0.0.1:3000/manager/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_data(manager_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + manager_id + '/data'))


def get_all_names():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all/names'))


def insert(manager_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, manager_data))


def update(manager_id, manager_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + manager_id, manager_data))


def delete(manager_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + manager_id))


def VIEInsert(vie_data):
    return asyncio.run(commonCtrl.make_post_request(base_url + 'vol', vie_data))


def VIEDelete(vie_data):
    return asyncio.run(commonCtrl.make_delete_request(base_url + 'vol', vie_data))


def manager_auth(auth_data):
    return asyncio.run(commonCtrl.make_post_request(base_url + 'auth', auth_data))
