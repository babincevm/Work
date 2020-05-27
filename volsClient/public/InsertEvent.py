# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
import datetime
from views import add_window


class addEvent(QtWidgets.QDialog):
    def __init__(self, parent):
        super(addEvent, self).__init__(parent)
        self.setupUi(self)
        add_window.fill_centers_names(self.choose_center)
        add_window.fill_levels(self.choose_level)
        add_window.fill_organizations(self.choose_organization)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(366, 348)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.line_name = QtWidgets.QLineEdit(Dialog)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout_5.addWidget(self.line_name)
        self.incorrect_name = QtWidgets.QLabel(Dialog)
        self.incorrect_name.setObjectName("incorrect_name")
        self.incorrect_name.setVisible(False)
        self.horizontalLayout_5.addWidget(self.incorrect_name)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.calendar = QtWidgets.QCalendarWidget(Dialog)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout_4.addWidget(self.calendar)
        self.incorrect_date = QtWidgets.QLabel(Dialog)
        self.incorrect_date.setObjectName("incorrect_date")
        self.incorrect_date.setVisible(True)
        self.horizontalLayout_4.addWidget(self.incorrect_date)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.choose_level = QtWidgets.QComboBox(Dialog)
        self.choose_level.setObjectName("choose_level")
        self.horizontalLayout_3.addWidget(self.choose_level)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.choose_organization = QtWidgets.QComboBox(Dialog)
        self.choose_organization.setObjectName("choose_organization")
        self.horizontalLayout_2.addWidget(self.choose_organization)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.choose_center = QtWidgets.QComboBox(Dialog)
        self.choose_center.setObjectName("choose_center")
        self.horizontalLayout.addWidget(self.choose_center)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_submit = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_submit.setOrientation(QtCore.Qt.Horizontal)
        self.btn_submit.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout.addWidget(self.btn_submit)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.btn_submit.accepted.connect(self.accept)
        self.btn_submit.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название"))
        self.incorrect_name.setText(_translate("Dialog", "Введено неверно"))
        self.label_3.setText(_translate("Dialog", "Дата проведения"))
        self.label_4.setText(_translate("Dialog", "Уровень:"))
        self.label_5.setText(_translate("Dialog", "Кто заказал:"))
        self.label_6.setText(_translate("Dialog", "Кто проводил:"))

    def check_data(self):
        flag = True
        self.incorrect_name.setVisible(False)
        self.incorrect_date.setVisible(False)
        date = self.calendar.selectedDate()

        if not len(self.line_name.text()) > 10:
            self.incorrect_name.setVisible(True)
            flag = False
        if date > datetime.date.today():
            self.incorrect_date.setVisible(True)
            flag = False

        return flag

    def convert(self):

        return {"event_name": self.line_name.text(),
                "event_date": datetime.date.strftime(self.calendar.selectedDate().toPyDate(), '%d/%m/%Y'),
                "event_level": self.choose_level.currentData(),
                "event_org": self.choose_organization.currentData(),
                "event_center": self.choose_center.currentData(),
                }

    def accept(self):
        if self.check_data():
            if add_window.add_event(self.convert()):
                return super().accept()
            QtWidgets.QMessageBox.about(self, "Ошибка", "Ошибка")
