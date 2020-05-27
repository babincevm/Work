# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from views import change_window
from public.InsertRequest import InsertRequest as base
from controllers import requests


class ChangeRequestWindow(base):
    def __init__(self, parent, request_id):
        super().__init__(parent)
        self.request_id = request_id
        change_window.fill_request_data(self)

    def accept(self):
        if super().check_data():
            if requests.update(self.request_id, super().convert()):
                QtWidgets.QDialog.accept(self)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')
