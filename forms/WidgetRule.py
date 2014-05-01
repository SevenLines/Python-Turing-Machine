import re
import symbol
from PySide.QtCore import Qt
from PySide.QtGui import QWidget, QPalette, QInputContext
from PySide.QtGui import QColor
from forms.ui.WidgetRule_ui import Ui_WidgetRule
from turing.turing import Rule


class Widget_Rule(QWidget, Ui_WidgetRule):


    def showEvent(self, QShowEvent):
        QWidget.showEvent(self, QShowEvent)
        self.edtRule.setSelection(len(self.edtRule.text()),0)
        # self.edtRule.setSelection(len(self.edtRule.text()),0)

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0):
        QWidget.__init__(self, QWidget_parent, Qt_WindowFlags_flags)
        self.setupUi(self)
        self.setFocusProxy(self.edtRule)


    # def __init__(self, QWidget_parent=None):



    @property
    def rule(self):
        return self.edtRule._rule

    @rule.setter
    def rule(self, value):
        self.edtRule.rule = value