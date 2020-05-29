# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from controllers import volunteers, organizations, events, centers, requests, levels, managers


def gender(number):
    if number == 0:
        return 'Ж'
    return 'М'


def fill_volunteers(table):
    all = volunteers.get_all()
    if all:
        rows = 0
        for volunteer in all:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(volunteer["volunteer_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(volunteer["emp_name"]))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(gender(volunteer["emp_gender"])))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(volunteer["emp_phone"]))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(volunteer["emp_email"]))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(volunteer["emp_bdate"]))
            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(volunteer["center_name"]))
            rows += 1


def delete_vol(vol_id):
    return volunteers.delete_vol(vol_id)


def fill_organizations(table):
    all = organizations.get_all()
    if all:
        rows = 0
        for organization in all:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(organization["organization_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(organization["org_name"]))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(organization["org_email"]))
            rows += 1


def delete_org(org_id):
    return organizations.delete(org_id)


def fill_events(table):
    data = events.get_all()
    if data:
        rows = 0
        for event in data:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(event["event_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(event["event_name"]))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(event["event_date"]))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(event["level_name"]))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(event["org_name"]))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(event["center_name"]))
            rows += 1


def delete_event(event_id):
    return events.delete(event_id)


def fill_centers(table):
    all = centers.get_all()
    if all:
        rows = 0
        for center in all:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(center["center_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(center["center_name"]))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(center["head_name"]))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(center["center_address"]))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(center["center_phone"]))
            rows += 1


def delete_center(center_id):
    return centers.delete(center_id)


def fill_requests(table):
    all = requests.get_all()
    if all:
        rows = 0
        for request in all:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(request["request_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(request["request_event_name"]))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(request["request_event_date"]))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(request["level_name"]))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(request["emp_name"]))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(request["org_name"]))
            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(request["center_name"]))
            rows += 1


def delete_req(req_id):
    return requests.delete(req_id)


def fill_levels(table):
    all = levels.get_all()
    if all:
        rows = 0
        for level in all:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(level["level_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(level["level_name"]))
            rows += 1


def delete_level(level_id):
    return levels.delete(level_id)


def fill_managers(table):
    all = managers.get_all()
    if all:
        rows = 0
        for manager in all:
            table.setRowCount(rows + 1)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(manager["manager_id"])))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(manager["emp_name"]))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(gender(manager["emp_gender"])))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(manager["emp_phone"]))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(manager["emp_email"]))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(manager["emp_bdate"]))
            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(manager["center_name"]))

            rows += 1


def delete_manager(manager_id):
    return managers.delete(manager_id)





