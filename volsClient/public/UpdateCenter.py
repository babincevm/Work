# -*- coding: utf-8 -*-
import datetime
from PyQt5 import QtWidgets
from views import change_window
from public.InsertCenter import addCenter as base
from controllers import centers


class ChangeCenterWindow(base):
    def __init__(self, parent, center_id):
        super().__init__(parent)
        self.center_id = center_id
        change_window.fill_center_data(self)

    def accept(self):
        if super().check_data():
            if centers.update(self.center_id, super().convert()):
                QtWidgets.QDialog.accept(self)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')
