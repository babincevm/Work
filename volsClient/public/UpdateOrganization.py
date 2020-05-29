# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from views import change_window
from public.InsertOrganization import AddOrgWindow as base


class ChangeOrganizationWindow(base):
    def __init__(self, parent, org_id):
        super().__init__(parent)
        self.org_id = org_id
        change_window.fill_organization_data(self)

    def accept(self):
        if super().check_data():
            if change_window.update_organization(self.org_id, super().convert()):
                QtWidgets.QDialog.accept(self)
            else:
                QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')
