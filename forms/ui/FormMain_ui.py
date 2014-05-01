# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/ui/FormMain.ui'
#
# Created: Fri May  2 03:44:00 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(485, 429)
        self.centralwidget = QtGui.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStep = QtGui.QPushButton(self.centralwidget)
        self.btnStep.setObjectName("btnStep")
        self.horizontalLayout.addWidget(self.btnStep)
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnRestart = QtGui.QPushButton(self.centralwidget)
        self.btnRestart.setObjectName("btnRestart")
        self.horizontalLayout.addWidget(self.btnRestart)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.clmnTape = QtGui.QColumnView(self.splitter)
        self.clmnTape.setObjectName("clmnTape")
        self.tblTuring = TableViewTuring(self.splitter)
        self.tblTuring.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.tblTuring.setObjectName("tblTuring")
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(MainForm)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtGui.QAction(MainForm)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtGui.QAction(MainForm)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainForm)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainForm.close)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStep.setText(QtGui.QApplication.translate("MainForm", "step", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStart.setText(QtGui.QApplication.translate("MainForm", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRestart.setText(QtGui.QApplication.translate("MainForm", "restart", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainForm", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainForm", "Load...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setShortcut(QtGui.QApplication.translate("MainForm", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainForm", "Save...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainForm", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainForm", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainForm", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

from forms.TableViewTuring import TableViewTuring
