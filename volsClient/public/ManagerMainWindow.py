# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from views import main_window
from public import UpdateCenter, InsertOrganization, InsertCenter, UpdateOrganization, \
    UpdateVolunteer, InsertVolunteer, UpdateEvent, InsertEvent, MoreInfoCenter, MoreInfo, \
    InsertRequest, UpdateRequest, UpdateManager, InsertManager, InsertLevel, UpdateLevel, CenterReport
import traceback


class ManagerMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ManagerMainWindow, self).__init__()
        self.setupUi(self)
        self.tabChanged()

    def setupUi(self, ManagerMainWindow):
        ManagerMainWindow.setObjectName("ManagerMainWindow")
        ManagerMainWindow.resize(568, 466)
        self.centralwidget = QtWidgets.QWidget(ManagerMainWindow)
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
        self.layout_buttons_vols = QtWidgets.QHBoxLayout()
        self.layout_buttons_vols.setObjectName("layout_buttons_vols")
        self.more_info_vol = QtWidgets.QPushButton(self.volunteers)
        self.more_info_vol.setObjectName("more_info_vol")
        self.layout_buttons_vols.addWidget(self.more_info_vol)
        self.add_vol = QtWidgets.QPushButton(self.volunteers)
        self.add_vol.setObjectName("add_vol")
        self.layout_buttons_vols.addWidget(self.add_vol)
        self.update_vol = QtWidgets.QPushButton(self.volunteers)
        self.update_vol.setObjectName("update_vol")
        self.layout_buttons_vols.addWidget(self.update_vol)
        self.delete_vol = QtWidgets.QPushButton(self.volunteers)
        self.delete_vol.setObjectName("delete_vol")
        self.layout_buttons_vols.addWidget(self.delete_vol)
        self.main_vol_layout.addLayout(self.layout_buttons_vols)
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
        self.layout_buttons_org = QtWidgets.QHBoxLayout()
        self.layout_buttons_org.setObjectName("layout_buttons_org")
        self.more_info_org = QtWidgets.QPushButton(self.organizations)
        self.more_info_org.setObjectName("more_info_org")
        self.layout_buttons_org.addWidget(self.more_info_org)
        self.add_org = QtWidgets.QPushButton(self.organizations)
        self.add_org.setObjectName("add_org")
        self.layout_buttons_org.addWidget(self.add_org)
        self.update_org = QtWidgets.QPushButton(self.organizations)
        self.update_org.setObjectName("update_org")
        self.layout_buttons_org.addWidget(self.update_org)
        self.delete_org = QtWidgets.QPushButton(self.organizations)
        self.delete_org.setObjectName("delete_org")
        self.layout_buttons_org.addWidget(self.delete_org)
        self.main_org_layout.addLayout(self.layout_buttons_org)
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
        self.layout_buttons_event = QtWidgets.QHBoxLayout()
        self.layout_buttons_event.setObjectName("layout_buttons_event")
        self.more_info_event = QtWidgets.QPushButton(self.events)
        self.more_info_event.setObjectName("more_info_event")
        self.layout_buttons_event.addWidget(self.more_info_event)
        self.add_event = QtWidgets.QPushButton(self.events)
        self.add_event.setObjectName("add_event")
        self.layout_buttons_event.addWidget(self.add_event)
        self.update_event = QtWidgets.QPushButton(self.events)
        self.update_event.setObjectName("update_event")
        self.layout_buttons_event.addWidget(self.update_event)
        self.delete_event = QtWidgets.QPushButton(self.events)
        self.delete_event.setObjectName("delete_event")
        self.layout_buttons_event.addWidget(self.delete_event)
        self.main_event_layout.addLayout(self.layout_buttons_event)
        self.event_table = QtWidgets.QTableWidget(self.events)
        self.event_table.setObjectName("event_table")
        self.event_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.event_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.event_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.event_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.event_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.event_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.event_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.main_event_layout.addWidget(self.event_table)
        self.verticalLayout_4.addLayout(self.main_event_layout)
        self.event_table.setRowCount(0)
        self.event_table.setColumnCount(6)
        self.event_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem())
        self.event_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem())
        self.event_table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem())
        self.event_table.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem())
        self.event_table.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem())
        self.event_table.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem())
        self.event_table.horizontalHeader().setCascadingSectionResizes(True)
        self.event_table.horizontalHeader().setStretchLastSection(False)
        self.event_table.verticalHeader().setVisible(False)
        self.event_table.verticalHeader().setCascadingSectionResizes(True)
        self.event_table.verticalHeader().setSortIndicatorShown(True)
        self.event_table.verticalHeader().setStretchLastSection(False)
        self.event_table.horizontalHeaderItem(0).setText("id")
        self.event_table.horizontalHeaderItem(1).setText("Название")
        self.event_table.horizontalHeaderItem(2).setText("Дата")
        self.event_table.horizontalHeaderItem(3).setText("Уровень")
        self.event_table.horizontalHeaderItem(4).setText("Организация")
        self.event_table.horizontalHeaderItem(5).setText("Центр")
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
        self.layout_buttons_center = QtWidgets.QHBoxLayout()
        self.layout_buttons_center.setObjectName("layout_buttons_center")
        self.report_center = QtWidgets.QPushButton(self.centers)
        self.report_center.setObjectName("report_center")
        self.layout_buttons_center.addWidget(self.report_center)
        self.more_info_center = QtWidgets.QPushButton(self.centers)
        self.more_info_center.setObjectName("more_info_center")
        self.layout_buttons_center.addWidget(self.more_info_center)
        self.add_center = QtWidgets.QPushButton(self.centers)
        self.add_center.setObjectName("add_center")
        self.layout_buttons_center.addWidget(self.add_center)
        self.update_center = QtWidgets.QPushButton(self.centers)
        self.update_center.setObjectName("update_center")
        self.layout_buttons_center.addWidget(self.update_center)
        self.delete_center = QtWidgets.QPushButton(self.centers)
        self.delete_center.setObjectName("delete_center")
        self.layout_buttons_center.addWidget(self.delete_center)
        self.main_center_layout.addLayout(self.layout_buttons_center)
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
        #
        # requests
        #
        self.requests = QtWidgets.QWidget()
        self.requests.setObjectName("requests")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.requests)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.main_request_layout = QtWidgets.QVBoxLayout()
        self.main_request_layout.setObjectName("main_request_layout")
        self.layout_buttons_request = QtWidgets.QHBoxLayout()
        self.layout_buttons_request.setObjectName("layout_buttons_request")
        self.add_request = QtWidgets.QPushButton(self.requests)
        self.add_request.setObjectName("add_request")
        self.layout_buttons_request.addWidget(self.add_request)
        self.update_request = QtWidgets.QPushButton(self.requests)
        self.update_request.setObjectName("update_request")
        self.layout_buttons_request.addWidget(self.update_request)
        self.delete_request = QtWidgets.QPushButton(self.requests)
        self.delete_request.setObjectName("delete_request")
        self.layout_buttons_request.addWidget(self.delete_request)
        self.main_request_layout.addLayout(self.layout_buttons_request)
        self.request_table = QtWidgets.QTableWidget(self.requests)
        self.request_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.request_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.request_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.request_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.request_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.request_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.request_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.request_table.setRowCount(0)
        self.request_table.setColumnCount(7)
        self.request_table.setObjectName("request_table")
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(6, item)
        self.request_table.horizontalHeader().setCascadingSectionResizes(True)
        self.request_table.horizontalHeader().setStretchLastSection(False)
        self.request_table.verticalHeader().setVisible(False)
        self.request_table.verticalHeader().setCascadingSectionResizes(True)
        self.request_table.verticalHeader().setSortIndicatorShown(True)
        self.request_table.verticalHeader().setStretchLastSection(False)
        self.main_request_layout.addWidget(self.request_table)
        self.verticalLayout_6.addLayout(self.main_request_layout)
        self.tabWidget.addTab(self.requests, "")
        self.verticalLayout.addWidget(self.tabWidget)
        ManagerMainWindow.setCentralWidget(self.centralwidget)
        self.request_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #
        # levels
        #
        self.levels = QtWidgets.QWidget()
        self.levels.setObjectName("levels")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.levels)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.main_levels_layout = QtWidgets.QVBoxLayout()
        self.main_levels_layout.setObjectName("main_levels_layout")
        self.layout_buttons_level = QtWidgets.QHBoxLayout()
        self.layout_buttons_level.setObjectName("layout_buttons_level")
        self.add_level = QtWidgets.QPushButton(self.levels)
        self.add_level.setObjectName("add_level")
        self.layout_buttons_level.addWidget(self.add_level)
        self.update_level = QtWidgets.QPushButton(self.levels)
        self.update_level.setObjectName("update_level")
        self.layout_buttons_level.addWidget(self.update_level)
        self.delete_level = QtWidgets.QPushButton(self.levels)
        self.delete_level.setObjectName("delete_level")
        self.layout_buttons_level.addWidget(self.delete_level)
        self.main_levels_layout.addLayout(self.layout_buttons_level)
        self.levels_table = QtWidgets.QTableWidget(self.levels)
        self.levels_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.levels_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.levels_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.levels_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.levels_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.levels_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.levels_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.levels_table.setRowCount(0)
        self.levels_table.setColumnCount(2)
        self.levels_table.setObjectName("levels_table")
        item = QtWidgets.QTableWidgetItem()
        self.levels_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.levels_table.setHorizontalHeaderItem(1, item)
        self.levels_table.horizontalHeader().setCascadingSectionResizes(True)
        self.levels_table.horizontalHeader().setStretchLastSection(False)
        self.levels_table.verticalHeader().setVisible(False)
        self.levels_table.verticalHeader().setCascadingSectionResizes(True)
        self.levels_table.verticalHeader().setSortIndicatorShown(True)
        self.levels_table.verticalHeader().setStretchLastSection(False)
        self.main_levels_layout.addWidget(self.levels_table)
        self.verticalLayout_7.addLayout(self.main_levels_layout)
        self.tabWidget.addTab(self.levels, "")
        self.verticalLayout.addWidget(self.tabWidget)
        ManagerMainWindow.setCentralWidget(self.centralwidget)
        self.levels_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #
        # managers
        #
        self.managers = QtWidgets.QWidget()
        self.managers.setObjectName("managers")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.managers)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.main_manager_layout = QtWidgets.QVBoxLayout()
        self.main_manager_layout.setObjectName("main_manager_layout")
        self.layout_buttons_manager = QtWidgets.QHBoxLayout()
        self.layout_buttons_manager.setObjectName("layout_buttons_manager")
        self.add_manager = QtWidgets.QPushButton(self.managers)
        self.add_manager.setObjectName("add_manager")
        self.layout_buttons_manager.addWidget(self.add_manager)
        self.update_manager = QtWidgets.QPushButton(self.managers)
        self.update_manager.setObjectName("update_vol")
        self.layout_buttons_manager.addWidget(self.update_manager)
        self.delete_manager = QtWidgets.QPushButton(self.managers)
        self.delete_manager.setObjectName("delete_manager")
        self.layout_buttons_manager.addWidget(self.delete_manager)
        self.main_manager_layout.addLayout(self.layout_buttons_manager)
        self.manager_table = QtWidgets.QTableWidget(self.managers)
        self.manager_table.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.manager_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manager_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.manager_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.manager_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.manager_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.manager_table.setTextElideMode(QtCore.Qt.ElideRight)
        self.manager_table.setRowCount(0)
        self.manager_table.setColumnCount(7)
        self.manager_table.setObjectName("manager_table")
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.manager_table.setHorizontalHeaderItem(6, item)
        self.manager_table.horizontalHeader().setCascadingSectionResizes(True)
        self.manager_table.horizontalHeader().setStretchLastSection(False)
        self.manager_table.verticalHeader().setVisible(False)
        self.manager_table.verticalHeader().setCascadingSectionResizes(True)
        self.manager_table.verticalHeader().setSortIndicatorShown(True)
        self.manager_table.verticalHeader().setStretchLastSection(False)
        self.main_manager_layout.addWidget(self.manager_table)
        self.verticalLayout_8.addLayout(self.main_manager_layout)
        self.tabWidget.addTab(self.managers, "")
        self.manager_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #
        #
        #

        self.retranslateUi(ManagerMainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.currentChanged.connect(self.tabChanged)
        QtCore.QMetaObject.connectSlotsByName(ManagerMainWindow)

        #
        # volunteer buttons
        #
        self.add_vol.clicked.connect(self.insert_volunteer)
        self.delete_vol.clicked.connect(self.del_volunteer)
        self.update_vol.clicked.connect(self.upd_volunteer)
        self.more_info_vol.clicked.connect(self.info_volunteer)
        #
        # organization buttons
        #
        self.add_org.clicked.connect(self.insert_organization)
        self.delete_org.clicked.connect(self.del_organization)
        self.update_org.clicked.connect(self.upd_organization)
        self.more_info_org.clicked.connect(self.info_organization)
        #
        # event buttons
        #
        self.add_event.clicked.connect(self.insert_event)
        self.more_info_event.clicked.connect(self.info_event)
        self.delete_event.clicked.connect(self.del_event)
        self.update_event.clicked.connect(self.upd_event)
        #
        # center buttons
        #
        self.more_info_center.clicked.connect(self.center_info)
        self.add_center.clicked.connect(self.insert_center)
        self.update_center.clicked.connect(self.upd_center)
        self.delete_center.clicked.connect(self.del_center)
        self.report_center.clicked.connect(self.center_report)
        #
        # request buttons
        #
        self.add_request.clicked.connect(self.insert_request)
        self.delete_request.clicked.connect(self.del_request)
        self.update_request.clicked.connect(self.upd_request)
        #
        # level buttons
        #
        self.add_level.clicked.connect(self.insert_level)
        self.delete_level.clicked.connect(self.del_level)
        self.update_level.clicked.connect(self.upd_level)
        #
        # manager buttons
        #
        self.add_manager.clicked.connect(self.insert_manager)
        self.delete_manager.clicked.connect(self.del_manager)
        self.update_manager.clicked.connect(self.upd_manager)

    def retranslateUi(self, ManagerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ManagerMainWindow.setWindowTitle(_translate("ManagerMainWindow", "Управляющий"))
        #
        # volunteers
        #
        self.more_info_vol.setText(_translate("ManagerMainWindow", "Доп. инфо"))
        self.add_vol.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_vol.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_vol.setText(_translate("ManagerMainWindow", "Удалить"))
        self.vol_table.setSortingEnabled(True)
        item = self.vol_table.horizontalHeaderItem(0)
        item.setText(_translate("ManagerMainWindow", "id"))
        item = self.vol_table.horizontalHeaderItem(1)
        item.setText(_translate("ManagerMainWindow", "ФИО"))
        item = self.vol_table.horizontalHeaderItem(2)
        item.setText(_translate("ManagerMainWindow", "Пол"))
        item = self.vol_table.horizontalHeaderItem(3)
        item.setText(_translate("ManagerMainWindow", "Телефон"))
        item = self.vol_table.horizontalHeaderItem(4)
        item.setText(_translate("ManagerMainWindow", "email"))
        item = self.vol_table.horizontalHeaderItem(5)
        item.setText(_translate("ManagerMainWindow", "Дата рождения"))
        item = self.vol_table.horizontalHeaderItem(6)
        item.setText(_translate("ManagerMainWindow", "Центр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.volunteers), _translate("ManagerMainWindow", "Волонтеры"))
        #
        # organizations
        #
        self.more_info_org.setText(_translate("ManagerMainWindow", "Доп. инфо"))
        self.add_org.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_org.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_org.setText(_translate("ManagerMainWindow", "Удалить"))
        self.org_table.setSortingEnabled(True)
        item = self.org_table.horizontalHeaderItem(0)
        item.setText(_translate("ManagerMainWindow", "id"))
        item = self.org_table.horizontalHeaderItem(1)
        item.setText(_translate("ManagerMainWindow", "Название"))
        item = self.org_table.horizontalHeaderItem(2)
        item.setText(_translate("ManagerMainWindow", "email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.organizations),
                                  _translate("ManagerMainWindow", "Организации"))
        #
        # events
        #
        self.more_info_event.setText(_translate("ManagerMainWindow", "Доп. инфо"))
        self.add_event.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_event.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_event.setText(_translate("ManagerMainWindow", "Удалить"))
        self.event_table.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.events), _translate("ManagerMainWindow", "Мероприятия"))
        #
        # centers
        #
        self.report_center.setText(_translate("ManagerMainWindow", "Отчет"))
        self.more_info_center.setText(_translate("ManagerMainWindow", "Доп. инфо"))
        self.add_center.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_center.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_center.setText(_translate("ManagerMainWindow", "Удалить"))
        self.center_table.setSortingEnabled(True)
        item = self.center_table.horizontalHeaderItem(0)
        item.setText(_translate("ManagerMainWindow", "id"))
        item = self.center_table.horizontalHeaderItem(1)
        item.setText(_translate("ManagerMainWindow", "Название"))
        item = self.center_table.horizontalHeaderItem(2)
        item.setText(_translate("ManagerMainWindow", "ФИО директора"))
        item = self.center_table.horizontalHeaderItem(3)
        item.setText(_translate("ManagerMainWindow", "Адрес"))
        item = self.center_table.horizontalHeaderItem(4)
        item.setText(_translate("ManagerMainWindow", "Телефон"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.centers), _translate("ManagerMainWindow", "Центр"))
        #
        # requests
        #
        self.add_request.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_request.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_request.setText(_translate("ManagerMainWindow", "Удалить"))
        self.request_table.setSortingEnabled(True)
        item = self.request_table.horizontalHeaderItem(0)
        item.setText(_translate("ManagerMainWindow", "id"))
        item = self.request_table.horizontalHeaderItem(1)
        item.setText(_translate("ManagerMainWindow", "Название"))
        item = self.request_table.horizontalHeaderItem(2)
        item.setText(_translate("ManagerMainWindow", "Дата"))
        item = self.request_table.horizontalHeaderItem(3)
        item.setText(_translate("ManagerMainWindow", "Уровень"))
        item = self.request_table.horizontalHeaderItem(4)
        item.setText(_translate("ManagerMainWindow", "Управляющий"))
        item = self.request_table.horizontalHeaderItem(5)
        item.setText(_translate("ManagerMainWindow", "Организация"))
        item = self.request_table.horizontalHeaderItem(6)
        item.setText(_translate("ManagerMainWindow", "Центр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.requests), _translate("ManagerMainWindow", "Заявки"))
        #
        # levels
        #
        self.add_level.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_level.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_level.setText(_translate("ManagerMainWindow", "Удалить"))
        self.levels_table.setSortingEnabled(True)
        item = self.levels_table.horizontalHeaderItem(0)
        item.setText(_translate("ManagerMainWindow", "id"))
        item = self.levels_table.horizontalHeaderItem(1)
        item.setText(_translate("ManagerMainWindow", "Название"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.levels), _translate("ManagerMainWindow", "Уровни"))
        #
        # managers
        #
        self.add_manager.setText(_translate("ManagerMainWindow", "Добавить"))
        self.update_manager.setText(_translate("ManagerMainWindow", "Изменить"))
        self.delete_manager.setText(_translate("ManagerMainWindow", "Удалить"))
        self.manager_table.setSortingEnabled(True)
        item = self.manager_table.horizontalHeaderItem(0)
        item.setText(_translate("ManagerMainWindow", "id"))
        item = self.manager_table.horizontalHeaderItem(1)
        item.setText(_translate("ManagerMainWindow", "ФИО"))
        item = self.manager_table.horizontalHeaderItem(2)
        item.setText(_translate("ManagerMainWindow", "Пол"))
        item = self.manager_table.horizontalHeaderItem(3)
        item.setText(_translate("ManagerMainWindow", "Телефон"))
        item = self.manager_table.horizontalHeaderItem(4)
        item.setText(_translate("ManagerMainWindow", "email"))
        item = self.manager_table.horizontalHeaderItem(5)
        item.setText(_translate("ManagerMainWindow", "Дата рождения"))
        item = self.manager_table.horizontalHeaderItem(6)
        item.setText(_translate("ManagerMainWindow", "Центр"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.managers), _translate("ManagerMainWindow", "Управляющие"))

    def tabChanged(self):

        if self.tabWidget.currentIndex() == 0:
            main_window.fill_volunteers(self.vol_table)
        elif self.tabWidget.currentIndex() == 1:
            main_window.fill_organizations(self.org_table)
        elif self.tabWidget.currentIndex() == 2:
            main_window.fill_events(self.event_table)
        elif self.tabWidget.currentIndex() == 3:
            main_window.fill_centers(self.center_table)
        elif self.tabWidget.currentIndex() == 4:
            main_window.fill_requests(self.request_table)
        elif self.tabWidget.currentIndex() == 5:
            main_window.fill_levels(self.levels_table)
        elif self.tabWidget.currentIndex() == 6:
            main_window.fill_managers(self.manager_table)

    def get_id(self, table):
        try:
            table = getattr(self, table + "_table")
            return table.item(table.currentRow(), 0).text()
        except AttributeError:
            return table.item(0, 0).text()

    #
    # volunteers event handlers
    #
    def info_volunteer(self):
        try:
            MoreInfo.more_info(self, 0, self.get_id('vol')).exec_()
        except Exception:
            print(traceback.format_exc())

    def insert_volunteer(self):
        try:
            if InsertVolunteer.AddVolunteerWindow(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_volunteer(self):
        try:
            if main_window.delete_vol(self.get_id('vol')):
                self.vol_table.setRowCount(self.vol_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def upd_volunteer(self):
        try:
            if UpdateVolunteer.ChangeVolunteerWindow(self, self.get_id('vol')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    #
    # organization event handlers
    #
    def info_organization(self):
        try:
            MoreInfo.more_info(self, 1, self.get_id('org')).exec_()
        except Exception:
            print(traceback.format_exc())

    def insert_organization(self):
        try:
            if InsertOrganization.AddOrgWindow(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_organization(self):
        try:
            if main_window.delete_org(self.get_id('org')):
                self.org_table.setRowCount(self.org_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def upd_organization(self):
        try:
            if UpdateOrganization.ChangeOrganizationWindow(self,
                                                           self.get_id('org')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    #
    # event event handlers
    #
    def info_event(self):
        try:
            MoreInfo.more_info(self, 2, self.get_id('event')).exec_()
        except Exception:
            print(traceback.format_exc())

    def insert_event(self):
        try:
            if InsertEvent.addEvent(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_event(self):
        try:
            if main_window.delete_event(self.get_id('event')):
                self.event_table.setRowCount(self.event_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def upd_event(self):
        try:
            if UpdateEvent.ChangeEventWindow(self, self.get_id('event')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    #
    # center event handlers
    #
    def center_info(self):
        try:
            MoreInfoCenter.centerInfo(self, self.get_id('center')).exec_()
        except Exception:
            print(traceback.format_exc())

    def insert_center(self):
        try:
            if InsertCenter.addCenter(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def upd_center(self):
        try:
            if UpdateCenter.ChangeCenterWindow(self, self.get_id('center')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_center(self):
        try:
            if main_window.delete_center(self.get_id('center')):
                self.center_table.setRowCount(self.center_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def center_report(self):
        try:
            CenterReport.ReportCenter(self, self.get_id('center')).exec_()
        except Exception:
            print(traceback.format_exc())

    #
    # request event handlers
    #
    def insert_request(self):
        try:
            if InsertRequest.InsertRequest(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_request(self):
        try:
            if main_window.delete_req(self.get_id('request')):
                self.request_table.setRowCount(self.request_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def upd_request(self):
        try:
            if UpdateRequest.ChangeRequestWindow(self, self.get_id('request')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()

        except Exception:
            print(traceback.format_exc())

    #
    # level event handlers
    #
    def insert_level(self):
        try:
            if InsertLevel.AddLevelWindow(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_level(self):
        try:
            if main_window.delete_level(self.get_id('levels')):
                self.levels_table.setRowCount(self.levels_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def upd_level(self):
        try:
            if UpdateLevel.ChangeLevelWindow(self, self.get_id('levels')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    #
    # manager event handlers
    #
    def insert_manager(self):
        try:
            if InsertManager.AddManagerWindow(self).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())

    def del_manager(self):
        try:
            if main_window.delete_manager(self.get_id('manager')):
                self.manager_table.setRowCount(self.manager_table.rowCount() - 1)
                self.tabChanged()
        except AttributeError:
            print(traceback.format_exc())

    def upd_manager(self):
        try:
            if UpdateManager.ChangeManagerWindow(self, self.get_id('manager')).exec_() == QtWidgets.QDialog.Accepted:
                self.tabChanged()
        except Exception:
            print(traceback.format_exc())
