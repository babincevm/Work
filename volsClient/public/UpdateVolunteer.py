# -*- coding: utf-8 -*-
import datetime
from PyQt5 import QtWidgets
from views import change_window
from public.InsertVolunteer import AddVolunteerWindow as base
from controllers import volunteers


class ChangeVolunteerWindow(base):
    def __init__(self, parent, vol_id):
        super().__init__(parent)
        self.vol_id = vol_id
        change_window.fill_volunteer_data(self)

    def accept(self):
        if super().check_data():
            if volunteers.update_vol(self.vol_id, super().convert()):
                QtWidgets.QDialog.accept(self)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')



