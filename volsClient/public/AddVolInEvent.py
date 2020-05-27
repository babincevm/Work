# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from views import add_window


class AddVolunteerInEvent(QtWidgets.QDialog):
    def __init__(self, parent, vol_id=None, event_id=None):
        super(AddVolunteerInEvent, self).__init__(parent)
        self.setupUi(self)
        self.vol_id = vol_id
        self.event_id = event_id
        if vol_id:
            add_window.fill_events(self.choose_item)
        else:
            add_window.fill_volunteers(self.choose_item)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(360, 170))
        Form.setMaximumSize(QtCore.QSize(360, 170))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.choose_layout = QtWidgets.QHBoxLayout()
        self.choose_layout.setObjectName("choose_layout")
        self.choose_text = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_text.sizePolicy().hasHeightForWidth())
        self.choose_text.setSizePolicy(sizePolicy)
        self.choose_text.setObjectName("choose_text")
        self.choose_layout.addWidget(self.choose_text)
        self.choose_item = QtWidgets.QComboBox(Form)
        self.choose_item.setObjectName("choose_item")
        self.choose_layout.addWidget(self.choose_item)
        self.main_layout.addLayout(self.choose_layout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.main_layout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Form.reject)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить"))
        self.choose_text.setText(_translate("Form", "Выберите"))

    def convert(self):
        if self.vol_id:
            return {
                "volunteer_id": self.vol_id,
                "event_id": self.choose_item.currentData()
            }
        return {
                "volunteer_id": self.choose_item.currentData(),
                "event_id": self.event_id
            }

    def accept(self):
        if add_window.add_vol_in_event(self.convert()):
            return super().accept()
        QtWidgets.QMessageBox.about(self, 'Ошибка', 'Ошибка')

