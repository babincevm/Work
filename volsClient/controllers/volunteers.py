# -*- coding: utf-8 -*-
import asyncio
from controllers import commonCtrl


base_url = 'http://127.0.0.1:3000/volunteer/'


def get_all():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all'))


def get_name(vol_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + vol_id + '/name'))


def get_all_names():
    return asyncio.run(commonCtrl.make_get_request(base_url + 'all/names'))


def get_data(vol_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + vol_id))


def insert_vol(vol_data):
    return asyncio.run(commonCtrl.make_post_request(base_url, vol_data))


def update_vol(vol_id, vol_data):
    return asyncio.run(commonCtrl.make_put_request(base_url + vol_id, vol_data))


def delete_vol(vol_id):
    return asyncio.run(commonCtrl.make_delete_request(base_url + vol_id))


def get_all_events(vol_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + vol_id + '/events'))


def get_counted_events(vol_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + vol_id + '/events/count'))


def get_avg_lvl(vol_id):
    return asyncio.run(commonCtrl.make_get_request(base_url + vol_id + '/levels/avg'))
