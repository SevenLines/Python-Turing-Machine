# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/ui/WidgetRule.ui'
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

class Ui_WidgetRule(object):
    def setupUi(self, WidgetRule):
        WidgetRule.setObjectName(_fromUtf8("WidgetRule"))
        WidgetRule.resize(214, 25)
        WidgetRule.setStyleSheet(_fromUtf8("QComboBox::drop-down {\n"
"border-width: 1px;\n"
"width:5px;\n"
"min-width:5px;\n"
"background-color:black;\n"
"} \n"
""))
        self.gridLayout = QtGui.QGridLayout(WidgetRule)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edtRule = QtGui.QLineEdit(WidgetRule)
        self.edtRule.setInputMask(_fromUtf8(""))
        self.edtRule.setObjectName(_fromUtf8("edtRule"))
        self.gridLayout.addWidget(self.edtRule, 1, 2, 1, 1)

        self.retranslateUi(WidgetRule)
        QtCore.QMetaObject.connectSlotsByName(WidgetRule)

    def retranslateUi(self, WidgetRule):
        WidgetRule.setWindowTitle(_translate("WidgetRule", "Form", None))

