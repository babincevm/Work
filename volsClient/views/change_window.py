# -*- coding: utf-8 -*-
from controllers import volunteers, organizations, events, centers, requests,managers,levels
import datetime
from PyQt5 import QtCore


def fill_volunteer_data(update_window):
    volunteer_data = volunteers.get_data(update_window.vol_id)[0]
    update_window.line_name.setText(volunteer_data['emp_name'])
    update_window.line_phone.setText(volunteer_data['emp_phone'])
    update_window.line_email.setText(volunteer_data['emp_email'])
    bdate = volunteer_data['emp_bdate']
    update_window.calendar.setSelectedDate(
        datetime.date(day=int(bdate[0:2]), month=int(bdate[3:5]), year=int(bdate[6:])))
    update_window.male_gender.setChecked(volunteer_data['emp_gender'])


def fill_organization_data(update_window):
    organization_data = organizations.get_data(update_window.org_id)[0]
    update_window.line_name.setText(organization_data["org_name"])
    update_window.line_email.setText(organization_data["org_email"])


def fill_event_data(update_window):
    event_data = events.get_data(update_window.event_id)[0]
    update_window.line_name.setText(event_data["event_name"])
    date = event_data["event_date"]
    update_window.calendar.setSelectedDate(datetime.date(day=int(date[0:2]), month=int(date[3:5]), year=int(date[6:])))


def fill_center_data(update_window):
    center_data = centers.get_data(update_window.center_id)[0]
    update_window.line_name.setText(center_data["center_name"])
    update_window.line_headname.setText(center_data["head_name"])
    update_window.line_phone.setText(center_data["center_phone"])
    update_window.line_adres.setText(center_data["center_address"])


def fill_request_data(update_window):
    request_data = requests.get_data(update_window.request_id)[0]
    update_window.line_name.setText(request_data["request_event_name"])
    date = request_data["request_event_date"]
    update_window.calendar.setSelectedDate(datetime.date(day=int(date[0:2]), month=int(date[3:5]), year=int(date[6:])))


def fill_manager_data(update_window):
    volunteer_data = managers.get_data(update_window.manager_id)[0]
    update_window.line_name.setText(volunteer_data['emp_name'])
    update_window.line_phone.setText(volunteer_data['emp_phone'])
    update_window.line_email.setText(volunteer_data['emp_email'])
    bdate = volunteer_data['emp_bdate']
    update_window.calendar.setSelectedDate(
        datetime.date(day=int(bdate[0:2]), month=int(bdate[3:5]), year=int(bdate[6:])))
    update_window.male_gender.setChecked(volunteer_data['emp_gender'])


def fill_level_data(update_window):
    level_data = levels.get_data(update_window.level_id)[0]
    update_window.line_name.setText(level_data['level_name'])


