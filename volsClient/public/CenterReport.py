# -*- coding: utf-8 -*-
from views import info
from PyQt5 import QtCore, QtWidgets


class ReportCenter(QtWidgets.QDialog):
    def __init__(self, parent, center_id):
        super(ReportCenter, self).__init__(parent)
        self.setupUi(self)
        info.fill_report(self, center_id)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.volunteer_layout = QtWidgets.QHBoxLayout()
        self.volunteer_layout.setObjectName("volunteer_layout")
        self.text_vol = QtWidgets.QLabel(Dialog)
        self.text_vol.setObjectName("text_vol")
        self.volunteer_layout.addWidget(self.text_vol)
        self.total_volunteer = QtWidgets.QLabel(Dialog)
        self.total_volunteer.setObjectName("total_volunteer")
        self.volunteer_layout.addWidget(self.total_volunteer)
        self.verticalLayout.addLayout(self.volunteer_layout)

        self.org_layout = QtWidgets.QHBoxLayout()
        self.org_layout.setObjectName("org_layout")
        self.text_org = QtWidgets.QLabel(Dialog)
        self.text_org.setObjectName("text_org")
        self.org_layout.addWidget(self.text_org)
        self.total_org = QtWidgets.QLabel(Dialog)
        self.total_org.setObjectName("total_org")
        self.org_layout.addWidget(self.total_org)
        self.verticalLayout.addLayout(self.org_layout)

        self.event_layout = QtWidgets.QHBoxLayout()
        self.event_layout.setObjectName("event_layout")
        self.text_event = QtWidgets.QLabel(Dialog)
        self.text_event.setObjectName("text_event")
        self.event_layout.addWidget(self.text_event)
        self.total_event = QtWidgets.QLabel(Dialog)
        self.total_event.setObjectName("total_event")
        self.event_layout.addWidget(self.total_event)
        self.verticalLayout.addLayout(self.event_layout)

        self.level_layout = QtWidgets.QHBoxLayout()
        self.level_layout.setObjectName("level_layout")
        self.text_level = QtWidgets.QLabel(Dialog)
        self.text_level.setObjectName("text_level")
        self.level_layout.addWidget(self.text_level)
        self.avg_level = QtWidgets.QLabel(Dialog)
        self.avg_level.setObjectName("avg_level")
        self.level_layout.addWidget(self.avg_level)
        self.verticalLayout.addLayout(self.level_layout)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text_vol.setText(_translate("Dialog", "Всего волонтеров"))
        self.total_volunteer.setText(_translate("Dialog", " "))
        self.text_org.setText(_translate("Dialog", "Всего организаций"))
        self.total_org.setText(_translate("Dialog", " "))
        self.text_event.setText(_translate("Dialog", "Всего мероприятий"))
        self.total_event.setText(_translate("Dialog", " "))
        self.text_level.setText(_translate("Dialog", "Средний уровень"))
        self.avg_level.setText(_translate("Dialog", " "))
