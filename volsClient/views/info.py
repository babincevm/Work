# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from controllers import volunteers, organizations, events, centers, managers


def fill_volunteer(info_window, vol_id):
    name = volunteers.get_name(vol_id)
    volunteer_events = volunteers.get_all_events(vol_id)
    counted_events = volunteers.get_counted_events(vol_id)[0]['counted_events']
    info_window.label_for_table.setText("Мероприятия")
    info_window.count_label.setText("Всего мероприятий: " + str(counted_events))
    info_window.name_of_info_requester.setText(name[0]["emp_name"])
    rows = 0
    try:
        for event in volunteer_events:
            info_window.table_for_info.setRowCount(rows + 1)
            info_window.table_for_info.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(event["event_id"])))
            info_window.table_for_info.setItem(rows, 1, QtWidgets.QTableWidgetItem(event["event_name"]))
            rows += 1
    except TypeError:
        pass


def fill_organization(info_window, org_id):
    name = organizations.get_name(org_id)
    organization_events = organizations.get_all_events(org_id)
    counted_events = organizations.get_counted_events(org_id)[0]['counted_events']
    info_window.label_for_table.setText("Мероприятия")
    info_window.count_label.setText("Всего мероприятий: " + str(counted_events))
    info_window.name_of_info_requester.setText(name[0]["org_name"])
    rows = 0
    try:
        for event in organization_events:
            info_window.table_for_info.setRowCount(rows + 1)
            info_window.table_for_info.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(event["event_id"])))
            info_window.table_for_info.setItem(rows, 1, QtWidgets.QTableWidgetItem(event["event_name"]))
            rows += 1
    except TypeError:
        pass


def fill_events(info_window, event_id):
    name = events.get_name(event_id)
    volunteers_in_event = events.get_volunteers(event_id)
    counted_volunteers = events.get_counted_volunteers(event_id)[0]['counted_volunteers']
    info_window.label_for_table.setText("Волонтеры")
    info_window.count_label.setText("Всего волонтеров: " + str(counted_volunteers))
    info_window.name_of_info_requester.setText(name[0]["event_name"])
    rows = 0
    try:
        for volunteer in volunteers_in_event:
            info_window.table_for_info.setRowCount(rows + 1)
            info_window.table_for_info.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(volunteer["emp_id"])))
            info_window.table_for_info.setItem(rows, 1, QtWidgets.QTableWidgetItem(volunteer["emp_name"]))
            rows += 1
    except TypeError:
        pass


def fill_center(info_window, center_id):
    data = centers.get_name(center_id)[0]
    info_window.name_of_info_requester.setText(data["center_name"])

    data = centers.get_volunteers(center_id)
    rows = 0
    try:
        for volunteer in data:
            info_window.volunteers_table.setRowCount(rows + 1)
            info_window.volunteers_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(volunteer["emp_id"])))
            info_window.volunteers_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(volunteer["emp_name"]))
            rows += 1
    except TypeError:
        pass

    data = centers.get_events(center_id)
    rows = 0
    try:
        for event in data:
            info_window.events_table.setRowCount(rows + 1)
            info_window.events_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(event["event_id"])))
            info_window.events_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(event["event_name"]))
            rows += 1
    except TypeError:
        pass

    data = centers.get_organizations(center_id)
    rows = 0
    try:
        for organization in data:
            info_window.org_table.setRowCount(rows + 1)
            info_window.org_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(organization["organization_id"])))
            info_window.org_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(organization["org_name"]))
            rows += 1
    except TypeError:
        pass


def fill_report(report_window, center_id):
    total_volunteers = str(centers.get_total_volunteers(center_id)[0]['volunteers_total'])
    total_organizations = str(centers.get_total_organizations(center_id)[0]['organizations_total'])
    total_events = str(centers.get_total_events(center_id)[0]['events_total'])
    
    report_window.total_volunteer.setText(total_volunteers)
    report_window.total_org.setText(total_organizations)
    report_window.total_event.setText(total_events)


def fill(info_window, about, about_id):
    if about == 0:
        return fill_volunteer(info_window, about_id)
    elif about == 1:
        return fill_organization(info_window, about_id)
    elif about == 2:
        return fill_events(info_window, about_id)
    elif about == 3:
        return fill_center(info_window, about_id)


def delete_vol_in_event(vol_in_event_data):
    return managers.VIEDelete(vol_in_event_data)

