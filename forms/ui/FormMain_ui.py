# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/ui/FormMain.ui'
#
# Created: Thu May  1 03:51:27 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName(_fromUtf8("MainForm"))
        MainForm.resize(485, 429)
        self.centralwidget = QtGui.QWidget(MainForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnStep = QtGui.QPushButton(self.centralwidget)
        self.btnStep.setObjectName(_fromUtf8("btnStep"))
        self.horizontalLayout.addWidget(self.btnStep)
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnRestart = QtGui.QPushButton(self.centralwidget)
        self.btnRestart.setObjectName(_fromUtf8("btnRestart"))
        self.horizontalLayout.addWidget(self.btnRestart)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.clmnTape = QtGui.QColumnView(self.splitter)
        self.clmnTape.setObjectName(_fromUtf8("clmnTape"))
        self.tblTuring = QtGui.QTableView(self.splitter)
        self.tblTuring.setObjectName(_fromUtf8("tblTuring"))
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 485, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainForm)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainForm.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(MainForm)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainForm)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainForm)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainForm)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainForm.close)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(_translate("MainForm", "MainWindow", None))
        self.btnStep.setText(_translate("MainForm", "step", None))
        self.btnStart.setText(_translate("MainForm", "start", None))
        self.btnRestart.setText(_translate("MainForm", "restart", None))
        self.menuFile.setTitle(_translate("MainForm", "File", None))
        self.actionLoad.setText(_translate("MainForm", "Load...", None))
        self.actionLoad.setShortcut(_translate("MainForm", "Ctrl+O", None))
        self.actionSave.setText(_translate("MainForm", "Save...", None))
        self.actionSave.setShortcut(_translate("MainForm", "Ctrl+S", None))
        self.actionExit.setText(_translate("MainForm", "Exit", None))
        self.actionExit.setShortcut(_translate("MainForm", "Ctrl+Q", None))

