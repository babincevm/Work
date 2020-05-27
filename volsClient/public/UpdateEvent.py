# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from views import change_window
from public.InsertEvent import addEvent as base
from controllers import events


class ChangeEventWindow(base):
    def __init__(self, parent, event_id):
        super().__init__(parent)
        self.event_id = event_id
        change_window.fill_event_data(self)

    def accept(self):
        if super().check_data():
            if events.update(self.event_id, super().convert()):
                return QtWidgets.QDialog.accept(self)
            QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')
