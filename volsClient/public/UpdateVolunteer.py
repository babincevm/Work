# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from views import change_window
from public.InsertVolunteer import AddVolunteerWindow as base


class ChangeVolunteerWindow(base):
    def __init__(self, parent, vol_id):
        super().__init__(parent)
        self.vol_id = vol_id
        change_window.fill_volunteer_data(self)

    def accept(self):
        if super().check_data():
            if change_window.update_volunteer(self.vol_id, super().convert()):
                QtWidgets.QDialog.accept(self)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')



