# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from views import change_window
from public.InsertLevel import AddLevelWindow as base


class ChangeLevelWindow(base):
    def __init__(self, parent, level_id):
        super().__init__(parent)
        self.level_id = level_id
        change_window.fill_level_data(self)

    def accept(self):
        if change_window.update_level(self.level_id, super().convert()):
            return QtWidgets.QDialog.accept(self)
        QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')



