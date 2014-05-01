# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/ui/WidgetRule.ui'
#
# Created: Fri May  2 03:44:00 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_WidgetRule(object):
    def setupUi(self, WidgetRule):
        WidgetRule.setObjectName("WidgetRule")
        WidgetRule.resize(214, 25)
        WidgetRule.setStyleSheet("QComboBox::drop-down {\n"
"border-width: 1px;\n"
"width:5px;\n"
"min-width:5px;\n"
"background-color:black;\n"
"} \n"
"")
        self.gridLayout = QtGui.QGridLayout(WidgetRule)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.edtRule = RuleTextEdit(WidgetRule)
        self.edtRule.setInputMask("")
        self.edtRule.setObjectName("edtRule")
        self.gridLayout.addWidget(self.edtRule, 1, 2, 1, 1)

        self.retranslateUi(WidgetRule)
        QtCore.QMetaObject.connectSlotsByName(WidgetRule)

    def retranslateUi(self, WidgetRule):
        WidgetRule.setWindowTitle(QtGui.QApplication.translate("WidgetRule", "Form", None, QtGui.QApplication.UnicodeUTF8))

from forms.RuleTextEdit import RuleTextEdit
