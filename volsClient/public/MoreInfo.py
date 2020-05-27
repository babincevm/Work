# -*- coding: utf-8 -*-
import traceback
from views import info
from public import AddVolInEvent
from PyQt5 import QtCore, QtGui, QtWidgets


class more_info(QtWidgets.QDialog):
    def __init__(self, parent, about, about_id, is_manager=True):
        super(more_info, self).__init__(parent)
        self.setupUi(self)
        info.fill(self, about, about_id)
        if is_manager and (about == 0 or about == 2):
            self.add_buttons(self)
            self.about_id = about_id
            self.about = about
            if about == 2:
                self.table_for_info.horizontalHeaderItem(1).setText("ФИО")



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(539, 459)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_of_info_requester = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.name_of_info_requester.setFont(font)
        self.name_of_info_requester.setAlignment(QtCore.Qt.AlignCenter)
        self.name_of_info_requester.setObjectName("name_of_info_requester")
        self.verticalLayout_2.addWidget(self.name_of_info_requester)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.label_for_table = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_for_table.setFont(font)
        self.label_for_table.setAlignment(QtCore.Qt.AlignCenter)
        self.label_for_table.setObjectName("label_for_table")
        self.verticalLayout_3.addWidget(self.label_for_table)
        self.count_label = QtWidgets.QLabel(Form)
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.count_label.setObjectName("count_label")
        self.verticalLayout_3.addWidget(self.count_label)
        self.count_label.setFont(font)
        self.table_for_info = QtWidgets.QTableWidget(Form)
        self.table_for_info.setObjectName("table_for_info")
        self.table_for_info.setColumnCount(2)
        self.table_for_info.setRowCount(0)
        self.table_for_info.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem())
        self.table_for_info.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem())
        self.verticalLayout_3.addWidget(self.table_for_info)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.table_for_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_of_info_requester.setText(_translate("Form", "Name"))
        self.label_for_table.setText(_translate("Form", "Table"))
        self.table_for_info.horizontalHeaderItem(0).setText(_translate("Form", "id"))
        self.table_for_info.horizontalHeaderItem(1).setText(_translate("Form", "Название"))

    def add_buttons(self, Form):
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        self.add = QtWidgets.QPushButton(Form)
        self.add.setObjectName("add")
        self.layout_buttons.addWidget(self.add)
        self.delete_vol = QtWidgets.QPushButton(Form)
        self.delete_vol.setObjectName("delete_vol")
        self.layout_buttons.addWidget(self.delete_vol)
        self.verticalLayout_3.addLayout(self.layout_buttons)
        self.delete_vol.setText("Удалить")
        self.add.setText("Добавить")

        self.add.clicked.connect(self.add_vie)
        self.delete_vol.clicked.connect(self.delete)

    def add_vie(self):
        try:
            if self.about == 0:
                if AddVolInEvent.AddVolunteerInEvent(self, vol_id=self.about_id).exec_() == QtWidgets.QDialog.Accepted:
                    info.fill(self, self.about, self.about_id)
            else:
                if AddVolInEvent.AddVolunteerInEvent(self, event_id=self.about_id).exec_() == QtWidgets.QDialog.Accepted:
                    info.fill(self, self.about, self.about_id)
        except Exception:
            print(traceback.format_exc())

    def get_id(self):
        table = self.table_for_info
        try:
            return int(table.item(table.currentRow(), 0).text())
        except AttributeError:
            return int(table.item(0, 0).text())

    def convert(self):
        if self.about == 0:
            return {
                "volunteer_id": int(self.about_id),
                "event_id": self.get_id()
            }
        return {
            "event_id": int(self.about_id),
            "volunteer_id": self.get_id()
        }

    def delete(self):
        try:
            if info.delete_vol_in_event(self.convert()):
                self.table_for_info.setRowCount(self.table_for_info.rowCount() - 1)
                info.fill(self, self.about, self.about_id)
            else:
                QtWidgets.QMessageBox.about(self, "Ошибка", "Ошибка")
        except Exception:
            print(traceback.format_exc())

