# -*- coding: utf-8 -*-
import datetime
from PyQt5 import QtCore, QtWidgets
from views import add_window


class AddManagerWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(AddManagerWindow, self).__init__(parent)
        self.setupUi(self)
        add_window.fill_centers_names(self.choose_center)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 400)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line_name = QtWidgets.QLineEdit(Dialog)
        self.line_name.setObjectName("line_name")
        self.horizontalLayout.addWidget(self.line_name)
        self.incorrect_name = QtWidgets.QLabel(Dialog)
        self.incorrect_name.setObjectName("incorrect_name")
        self.horizontalLayout.addWidget(self.incorrect_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_phone = QtWidgets.QLineEdit(Dialog)
        self.line_phone.setObjectName("line_phone")
        self.horizontalLayout_2.addWidget(self.line_phone)
        self.incorrect_phone = QtWidgets.QLabel(Dialog)
        self.incorrect_phone.setObjectName("incorrect_phone")
        self.horizontalLayout_2.addWidget(self.incorrect_phone)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.line_email = QtWidgets.QLineEdit(Dialog)
        self.line_email.setObjectName("line_email")
        self.horizontalLayout_3.addWidget(self.line_email)
        self.incorrect_email = QtWidgets.QLabel(Dialog)
        self.incorrect_email.setObjectName("incorrect_email")
        self.horizontalLayout_3.addWidget(self.incorrect_email)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.calendar = QtWidgets.QCalendarWidget(Dialog)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout_4.addWidget(self.calendar)
        self.incorrect_date = QtWidgets.QLabel(Dialog)
        self.incorrect_date.setObjectName("incorrect_date")
        self.horizontalLayout_4.addWidget(self.incorrect_date)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.male_gender = QtWidgets.QRadioButton(Dialog)
        self.male_gender.setObjectName("male_gender")
        self.male_gender.setChecked(True)
        self.verticalLayout.addWidget(self.male_gender)
        self.female_gender = QtWidgets.QRadioButton(Dialog)
        self.female_gender.setObjectName("female_gender")
        self.verticalLayout.addWidget(self.female_gender)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.choose_center = QtWidgets.QComboBox(Dialog)
        self.choose_center.setObjectName("choose_center")
        self.horizontalLayout_6.addWidget(self.choose_center)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.btn_submit = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_submit.setOrientation(QtCore.Qt.Horizontal)
        self.btn_submit.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btn_submit.setCenterButtons(False)
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout_2.addWidget(self.btn_submit)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.incorrect_name.setVisible(False)
        self.incorrect_phone.setVisible(False)
        self.incorrect_email.setVisible(False)
        self.incorrect_date.setVisible(False)

        self.retranslateUi(Dialog)
        self.btn_submit.accepted.connect(self.accept)
        self.btn_submit.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ФИО:"))
        self.incorrect_name.setText(_translate("Dialog", "Введено неверно"))
        self.label_2.setText(_translate("Dialog", "Номер телефона"))
        self.line_phone.setInputMask(_translate("Dialog", "0-000-000-0000"))
        self.incorrect_phone.setText(_translate("Dialog", "Введено неверно"))
        self.label_3.setText(_translate("Dialog", "Email"))
        self.incorrect_email.setText(_translate("Dialog", "Введено неверно"))
        self.label_4.setText(_translate("Dialog", "Дата рождения"))
        self.incorrect_date.setText(_translate("Dialog", "Введено неверно"))
        self.label_5.setText(_translate("Dialog", "Пол"))
        self.male_gender.setText(_translate("Dialog", "М"))
        self.female_gender.setText(_translate("Dialog", "Ж"))
        self.label_6.setText(_translate("Dialog", "Центр"))

    def age(self, date):
        today = datetime.date.today()
        this_year_birthday = datetime.date(today.year, date.month, date.day)
        if this_year_birthday < today:
            years = today.year - date.year
        else:
            years = today.year - date.year - 1
        return years

    def gender(self, is_checked):
        if is_checked:
            return 1
        return 0

    def check_data(self):
        flag = True
        self.incorrect_name.setVisible(False)
        self.incorrect_phone.setVisible(False)
        self.incorrect_email.setVisible(False)
        self.incorrect_date.setVisible(False)

        if not len(self.line_name.text()) > 10:
            self.incorrect_name.setVisible(True)
            flag = False

        if not len(self.line_phone.text()) == 14:
            flag = False
            self.incorrect_phone.setVisible(True)

        if "@" not in self.line_email.text():
            flag = False
            self.incorrect_email.setVisible(True)

        date = self.calendar.selectedDate()
        age = self.age(datetime.date(date.year(), date.month(), date.day()))
        if age < 14 or age > 100:
            flag = False
            self.incorrect_date.setVisible(True)
        return flag

    def convert(self):
        return {"manager_name": self.line_name.text(),
                "manager_phone": self.line_phone.text(),
                "manager_bdate": datetime.date.strftime(self.calendar.selectedDate().toPyDate(), '%d/%m/%Y'),
                "manager_email": self.line_email.text(),
                "manager_gender": self.gender(self.male_gender.isChecked()),
                "manager_center": self.choose_center.currentData(),
                }

    def accept(self):
        if self.check_data():
            if add_window.add_manager(self.convert()):
                return super().accept()
            QtWidgets.QMessageBox.about(self, "Ошибка", "Ошибка")
