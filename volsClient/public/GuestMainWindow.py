# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from views import main_window
from public import MoreInfoCenter, MoreInfo
import traceback


class GuestMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GuestMainWindow, self).__init__()
        try:
            self.setupUi(self)
        except Exception:
            print(traceback.format_exc())
        self.tabChanged()

    def setupUi(self, GuestMainWindow):
        GuestMainWindow.setObjectName("GuestMainWindow")
        GuestMainWindow.resize(568, 466)
        self.centralwidget = QtWidgets.QWidget(GuestMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        #
        # volunteers
        #
        self.volunteers = QtWidgets.QWidget()
        self.volunteers.setObjectName("volunteers")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.volunteers)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_vol_layout = QtWidgets.QVBoxLayout()
        self.main_vol_layout.setObjectName("main_vol_layout")
        self.vol_table = QtWidgets.QTableWidget(self.volunteers)
        self.vol_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.vol_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vol_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vol_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.vol_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.vol_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.vol_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.vol_table.setRowCount(0)
        self.vol_table.setColumnCount(7)
        self.vol_table.setObjectName("vol_table")
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.vol_table.setHorizontalHeaderItem(6, item)
        self.vol_table.horizontalHeader().setCascadingSectionResizes(True)
        self.vol_table.horizontalHeader().setStretchLastSection(False)
        self.vol_table.verticalHeader().setVisible(False)
        self.vol_table.verticalHeader().setCascadingSectionResizes(True)
        self.vol_table.verticalHeader().setSortIndicatorShown(True)
        self.vol_table.verticalHeader().setStretchLastSection(False)
        self.main_vol_layout.addWidget(self.vol_table)
        self.verticalLayout_3.addLayout(self.main_vol_layout)
        self.tabWidget.addTab(self.volunteers, "")
        self.vol_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #
        # organizations
        #
        self.organizations = QtWidgets.QWidget()
        self.organizations.setObjectName("organizations")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.organizations)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_org_layout = QtWidgets.QVBoxLayout()
        self.main_org_layout.setObjectName("main_org_layout")
        self.org_table = QtWidgets.QTableWidget(self.organizations)
        self.org_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.org_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.org_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.org_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.org_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.org_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.org_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.org_table.setRowCount(0)
        self.org_table.setColumnCount(3)
        self.org_table.setObjectName("org_table")
        item = QtWidgets.QTableWidgetItem()
        self.org_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.org_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.org_table.setHorizontalHeaderItem(2, item)
        self.org_table.horizontalHeader().setCascadingSectionResizes(True)
        self.org_table.horizontalHeader().setStretchLastSection(False)
        self.org_table.verticalHeader().setVisible(False)
        self.org_table.verticalHeader().setCascadingSectionResizes(True)
        self.org_table.verticalHeader().setSortIndicatorShown(True)
        self.org_table.verticalHeader().setStretchLastSection(False)
        self.main_org_layout.addWidget(self.org_table)
        self.verticalLayout_2.addLayout(self.main_org_layout)
        self.tabWidget.addTab(self.organizations, "")
        self.org_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #
        # events
        #
        self.events = QtWidgets.QWidget()
        self.events.setObjectName("events")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.events)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_event_layout = QtWidgets.QVBoxLayout()
        self.main_event_layout.setObjectName("main_event_layout")
        self.event_table = QtWidgets.QTableWidget(self.events)
        self.event_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.event_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.event_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.event_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.event_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.event_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.event_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.event_table.setRowCount(0)
        self.event_table.setColumnCount(6)
        self.event_table.setObjectName("event_table")
        item = QtWidgets.QTableWidgetItem()
        self.event_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.event_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.event_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.event_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.event_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.event_table.setHorizontalHeaderItem(5, item)
        self.event_table.horizontalHeader().setCascadingSectionResizes(True)
        self.event_table.horizontalHeader().setStretchLastSection(False)
        self.event_table.verticalHeader().setVisible(False)
        self.event_table.verticalHeader().setCascadingSectionResizes(True)
        self.event_table.verticalHeader().setSortIndicatorShown(True)
        self.event_table.verticalHeader().setStretchLastSection(False)
        self.main_event_layout.addWidget(self.event_table)
        self.verticalLayout_4.addLayout(self.main_event_layout)
        self.tabWidget.addTab(self.events, "")
        self.event_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #
        # centers
        #
        self.centers = QtWidgets.QWidget()
        self.centers.setObjectName("centers")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centers)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.main_center_layout = QtWidgets.QVBoxLayout()
        self.main_center_layout.setObjectName("main_center_layout")
        self.center_table = QtWidgets.QTableWidget(self.centers)
        self.center_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.center_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.center_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.center_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.center_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.center_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.center_table.setRowCount(0)
        self.center_table.setColumnCount(5)
        self.center_table.setObjectName("center_table")
        item = QtWidgets.QTableWidgetItem()
        self.center_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.center_table.setHorizontalHeaderItem(4, item)
        self.center_table.horizontalHeader().setCascadingSectionResizes(True)
        self.center_table.horizontalHeader().setStretchLastSection(False)
        self.center_table.verticalHeader().setVisible(False)
        self.center_table.verticalHeader().setCascadingSectionResizes(True)
        self.center_table.verticalHeader().setSortIndicatorShown(True)
        self.center_table.verticalHeader().setStretchLastSection(False)
        self.main_center_layout.addWidget(self.center_table)
        self.verticalLayout_5.addLayout(self.main_center_layout)
        self.tabWidget.addTab(self.centers, "")
        self.center_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        GuestMainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.tabWidget)
        self.retranslateUi(GuestMainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        QtCore.QMetaObject.connectSlotsByName(GuestMainWindow)

        #
        # more info emitters
        #
        self.vol_table.cellDoubleClicked.connect(self.info_volunteer)
        self.org_table.cellDoubleClicked.connect(self.info_organization)
        self.event_table.cellDoubleClicked.connect(self.info_event)
        self.center_table.cellDoubleClicked.connect(self.center_info)

    def retranslateUi(self, GuestMainWindow):
        _translate = QtCore.QCoreApplication.translate
        GuestMainWindow.setWindowTitle(_translate("GuestMainWindow", "Управляющий"))
        #
        # volunteers
        #
        self.vol_table.setSortingEnabled(True)
        item = self.vol_table.horizontalHeaderItem(0)
        item.setText(_translate("GuestMainWindow", "id"))
        item = self.vol_table.horizontalHeaderItem(1)
        item.setText(_translate("GuestMainWindow", "ФИО"))
        item = self.vol_table.horizontalHeaderItem(2)
        item.setText(_translate("GuestMainWindow", "Пол"))
        item = self.vol_table.horizontalHeaderItem(3)
        item.setText(_translate("GuestMainWindow", "Телефон"))
        item = self.vol_table.horizontalHeaderItem(4)
        item.setText(_translate("GuestMainWindow", "email"))
        item = self.vol_table.horizontalHeaderItem(5)
        item.setText(_translate("GuestMainWindow", "Дата рождения"))
        item = self.vol_table.horizontalHeaderItem(6)
        item.setText(_translate("GuestMainWindow", "Центр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.volunteers), _translate("GuestMainWindow", "Волонтеры"))
        #
        # organizations
        #
        self.org_table.setSortingEnabled(True)
        item = self.org_table.horizontalHeaderItem(0)
        item.setText(_translate("GuestMainWindow", "id"))
        item = self.org_table.horizontalHeaderItem(1)
        item.setText(_translate("GuestMainWindow", "Название"))
        item = self.org_table.horizontalHeaderItem(2)
        item.setText(_translate("GuestMainWindow", "email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.organizations),
                                  _translate("GuestMainWindow", "Организации"))
        #
        # events
        #
        self.event_table.setSortingEnabled(True)
        item = self.event_table.horizontalHeaderItem(0)
        item.setText(_translate("GuestMainWindow", "id"))
        item = self.event_table.horizontalHeaderItem(1)
        item.setText(_translate("GuestMainWindow", "Название"))
        item = self.event_table.horizontalHeaderItem(2)
        item.setText(_translate("GuestMainWindow", "Дата"))
        item = self.event_table.horizontalHeaderItem(3)
        item.setText(_translate("GuestMainWindow", "Уровень"))
        item = self.event_table.horizontalHeaderItem(4)
        item.setText(_translate("GuestMainWindow", "Организация"))
        item = self.event_table.horizontalHeaderItem(5)
        item.setText(_translate("GuestMainWindow", "Центр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.events), _translate("GuestMainWindow", "Мероприятия"))
        #
        # centers
        #
        self.center_table.setSortingEnabled(True)
        item = self.center_table.horizontalHeaderItem(0)
        item.setText(_translate("GuestMainWindow", "id"))
        item = self.center_table.horizontalHeaderItem(1)
        item.setText(_translate("GuestMainWindow", "Название"))
        item = self.center_table.horizontalHeaderItem(2)
        item.setText(_translate("GuestMainWindow", "ФИО директора"))
        item = self.center_table.horizontalHeaderItem(3)
        item.setText(_translate("GuestMainWindow", "Адрес"))
        item = self.center_table.horizontalHeaderItem(4)
        item.setText(_translate("GuestMainWindow", "Телефон"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.centers), _translate("GuestMainWindow", "Центр"))

    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            main_window.fill_volunteers(self.vol_table)
        elif self.tabWidget.currentIndex() == 1:
            main_window.fill_organizations(self.org_table)
        elif self.tabWidget.currentIndex() == 2:
            main_window.fill_events(self.event_table)
        elif self.tabWidget.currentIndex() == 3:
            main_window.fill_centers(self.center_table)

    def get_id(self, table):
        try:
            table = getattr(self, table + "_table")
            return table.item(table.currentRow(), 0).text()
        except AttributeError:
            return table.item(0, 0).text()

    def info_volunteer(self):
        try:
            MoreInfo.more_info(self, 0, self.get_id('vol'), False).exec_()
        except Exception:
            print(traceback.format_exc())

    def info_organization(self):
        try:
            MoreInfo.more_info(self, 1, self.get_id('org'), False).exec_()
        except Exception:
            print(traceback.format_exc())

    def info_event(self):
        try:
            MoreInfo.more_info(self, 2, self.get_id('event'), False).exec_()
        except Exception:
            print(traceback.format_exc())

    def center_info(self):
        try:
            MoreInfoCenter.centerInfo(self, self.get_id('center')).exec_()
        except Exception:
            print(traceback.format_exc())
