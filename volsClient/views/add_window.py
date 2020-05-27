# -*- coding: utf-8 -*-
from controllers import volunteers, organizations, events, centers, requests, levels, managers


def fill_centers_names(dropdown):
    all_centers = centers.get_names()
    for name in all_centers:
        dropdown.addItem(name['center_name'], name['center_id'])


def fill_levels(dropdown):
    all_levels = levels.get_all()
    for level in all_levels:
        dropdown.addItem(level['level_name'], level['level_id'])


def fill_organizations(dropdown):
    all_organizations = organizations.get_names()
    for organization in all_organizations:
        dropdown.addItem(organization['org_name'], organization['organization_id'])


def fill_managers(dropdown):
    all_managers = managers.get_all_names()
    for manager in all_managers:
        dropdown.addItem(manager['emp_name'], manager['manager_id'])


def fill_events(dropdown):
    all_events = events.get_all_names()
    for event in all_events:
        dropdown.addItem(event['event_name'], event['event_id'])


def fill_volunteers(dropdown):
    all_volunteers = volunteers.get_all_names()
    for volunteer in all_volunteers:
        dropdown.addItem(volunteer['emp_name'], volunteer['volunteer_id'])


def add_vol(vol_data):
    return volunteers.insert_vol(vol_data)


def add_org(org_data):
    return organizations.insert(org_data)


def add_event(event_data):
    return events.insert(event_data)


def add_center(center_data):
    return centers.insert(center_data)


def add_manager(manager_data):
    return managers.insert(manager_data)


def add_request(request_data):
    return requests.insert(request_data)


def add_level(level_data):
    return levels.insert(level_data)


def add_vol_in_event(vol_in_event_data):
    return managers.VIEInsert(vol_in_event_data)
