# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from views import change_window
from public.InsertManager import AddManagerWindow as base


class ChangeManagerWindow(base):
    def __init__(self, parent, manager_id):
        super().__init__(parent)
        self.manager_id = manager_id
        change_window.fill_manager_data(self)

    def accept(self):
        if super().check_data():
            if change_window.update_manager(self.manager_id, super().convert()):
                QtWidgets.QDialog.accept(self)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')



