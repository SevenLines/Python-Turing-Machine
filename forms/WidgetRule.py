import re
import symbol
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QWidget, QPalette, QInputContext
from PyQt4.QtGui import QColor
from forms.ui.WidgetRule_ui import Ui_WidgetRule
from turing.turing import Rule


class Widget_Rule(QWidget, Ui_WidgetRule):
    _valid = True
    _rule = None

    def showEvent(self, QShowEvent):
        QWidget.showEvent(self, QShowEvent)
        self.edtRule.setSelection(len(self.edtRule.text()),0)
        # self.edtRule.setSelection(len(self.edtRule.text()),0)

    def __init__(self, QWidget_parent=None):
        QWidget.__init__(self, QWidget_parent)
        self.setupUi(self)

        self.edtRule.textChanged.connect(self.regen_rule)
        self.setAutoFillBackground(True)
        self.setFocusProxy(self.edtRule)


    def regen_rule(self):
        text = self.edtRule.text()
        m = re.search('\\b(.)([<>=])(\d+)\\b', text)

        self._valid = False
        if m:
            shear = 1 if m.group(2) == '>' else -1 if m.group(2) == '<' else 0
            self._rule.new_symbol = str(m.group(1))
            self._rule.shear = shear
            self._rule.next_state = int(m.group(3))
            self._valid = True

        palette = self.edtRule.palette()
        assert (isinstance(palette, QPalette))
        clr = Qt.green if self._valid else Qt.red
        palette.setColor(self.backgroundRole(), clr)
        self.setPalette(palette)

    def gen_rule(self):
        if not self._rule:
            return

        self.edtRule.setText('{0}{1}{2}'.format(
            self._rule.new_symbol,
            '<' if self._rule.shear == -1 else '>' if self._rule.shear == 1 else '=',
            self._rule.next_state)
        )
        self._valid = True


    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self, value):
        self._rule = value
        self.gen_rule()


    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
        self.gen_rule()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.gen_rule()


    @property
    def shear(self):
        return self._shear

    @shear.setter
    def shear(self, value):
        self._shear = value
        self.gen_rule()