import symbol
from PyQt4.QtGui import QWidget
from forms.ui.WidgetRule_ui import Ui_WidgetRule


class Widget_Rule(QWidget,  Ui_WidgetRule):
    _symbol = ''
    _state = ''
    _shear = ''

    def __init__(self, QWidget_parent=None):
        QWidget.__init__(self, QWidget_parent)
        self.setupUi(self)

    def gen_rule(self):
        self.edtRule.setText('{0}, {1}, {2}'.format(self._symbol, self._shear, self._state))

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