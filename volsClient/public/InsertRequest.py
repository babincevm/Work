# -*- coding: utf-8 -*-
import datetime
from PyQt5 import QtCore, QtWidgets
from views import add_window


class InsertRequest(QtWidgets.QDialog):
    def __init__(self, parent):
        super(InsertRequest, self).__init__(parent)
        self.setupUi(self)
        add_window.fill_centers_names(self.choose_center)
        add_window.fill_organizations(self.choose_organization)
        add_window.fill_levels(self.choose_level)
        add_window.fill_managers(self.choose_manager)

    def setupUi(self, InsertRequest):
        InsertRequest.setObjectName("InsertRequest")
        InsertRequest.resize(526, 412)
        self.gridLayout = QtWidgets.QGridLayout(InsertRequest)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(InsertRequest)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_name = QtWidgets.QLineEdit(InsertRequest)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout.addWidget(self.line_name)
        self.incorrect_name = QtWidgets.QLabel(InsertRequest)
        self.incorrect_name.setObjectName("incorrect_name")
        self.incorrect_name.setVisible(False)
        self.horizontalLayout.addWidget(self.incorrect_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.date_label = QtWidgets.QLabel(InsertRequest)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_2.addWidget(self.date_label)
        self.calendar = QtWidgets.QCalendarWidget(InsertRequest)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout_2.addWidget(self.calendar)
        self.incorrect_date = QtWidgets.QLabel(InsertRequest)
        self.incorrect_date.setObjectName("incorrect_date")
        self.incorrect_date.setVisible(False)
        self.horizontalLayout_2.addWidget(self.incorrect_date)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.manager_label = QtWidgets.QLabel(InsertRequest)
        self.manager_label.setObjectName("manager_label")
        self.horizontalLayout_3.addWidget(self.manager_label)
        self.choose_manager = QtWidgets.QComboBox(InsertRequest)
        self.choose_manager.setObjectName("choose_manager")
        self.horizontalLayout_3.addWidget(self.choose_manager)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.organization_label = QtWidgets.QLabel(InsertRequest)
        self.organization_label.setObjectName("organization_label")
        self.horizontalLayout_4.addWidget(self.organization_label)
        self.choose_organization = QtWidgets.QComboBox(InsertRequest)
        self.choose_organization.setObjectName("choose_organization")
        self.horizontalLayout_4.addWidget(self.choose_organization)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.center_label = QtWidgets.QLabel(InsertRequest)
        self.center_label.setObjectName("center_label")
        self.horizontalLayout_5.addWidget(self.center_label)
        self.choose_center = QtWidgets.QComboBox(InsertRequest)
        self.choose_center.setObjectName("choose_center")
        self.horizontalLayout_5.addWidget(self.choose_center)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.level_label = QtWidgets.QLabel(InsertRequest)
        self.level_label.setObjectName("level_label")
        self.horizontalLayout_6.addWidget(self.level_label)
        self.choose_level = QtWidgets.QComboBox(InsertRequest)
        self.choose_level.setObjectName("choose_level")
        self.horizontalLayout_6.addWidget(self.choose_level)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(InsertRequest)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(InsertRequest)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(InsertRequest.reject)
        QtCore.QMetaObject.connectSlotsByName(InsertRequest)

    def retranslateUi(self, InsertRequest):
        _translate = QtCore.QCoreApplication.translate
        InsertRequest.setWindowTitle(_translate("InsertRequest", "Добавить"))
        self.label.setText(_translate("InsertRequest", "Название мероприятия"))
        self.incorrect_name.setText(_translate("InsertRequest", "Введено неверно"))
        self.date_label.setText(_translate("InsertRequest", "Дата проведения"))
        self.incorrect_date.setText(_translate("InsertRequest", "Введено неверно"))
        self.manager_label.setText(_translate("InsertRequest", "Кто заполнил"))
        self.organization_label.setText(_translate("InsertRequest", "Организация"))
        self.center_label.setText(_translate("InsertRequest", "Центр"))
        self.level_label.setText(_translate("InsertRequest", "Уровень"))

    def check_data(self):
        flag = True
        self.incorrect_name.setVisible(False)
        self.incorrect_date.setVisible(False)
        if len(self.line_name.text()) < 10:
            flag = False
            self.incorrect_name.setVisible(True)
        date = self.calendar.selectedDate().toPyDate()
        if date <= datetime.date.today():
            flag = False
            self.incorrect_name.setVisible(True)
        return flag

    def convert(self):
        return {
            "request_event_name": self.line_name.text(),
            "request_event_date": datetime.date.strftime(
                self.calendar.selectedDate().toPyDate(), '%d/%m/%Y'),
            "request_manager": self.choose_manager.currentData(),
            "request_organization": self.choose_organization.currentData(),
            "request_center": self.choose_center.currentData(),
            "request_level": self.choose_level.currentData() }

    def accept(self):
        if self.check_data():
            if add_window.add_request(self.convert()):
                return super().accept()
            QtWidgets.QMessageBox.about(self, "Ошибка", "Запись уже есть")
