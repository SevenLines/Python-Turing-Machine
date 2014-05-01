import re

from PySide.QtCore import Qt
from PySide.QtGui import QPalette, QColor, QCompleter, QStringListModel
from PySide.QtGui import QLineEdit

class RuleTextEdit(QLineEdit):
    _valid = True
    _rule = None
    completer = None

    def __init__(self, *args, **kwargs):
        super(RuleTextEdit, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        self.textChanged.connect(self.onTextChange)

        model = QStringListModel()
        model.setStringList(['<', '>', '=', 'vasya'])

        self.completer = QCompleter(model)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        self.setCompleter(self.completer)

    @property
    def rule(self):
        return self._rule

    @rule.setter
    def rule(self, value):
        self._rule = value
        self.gen_rule()

    def regen_rule(self):
        text = self.text()
        m = re.search('\\b(.)([<>=])(\d+)\\b', text)

        self._valid = False
        if m:
            shear = 1 if m.group(2) == '>' else -1 if m.group(2) == '<' else 0
            self._rule.new_symbol = str(m.group(1))
            self._rule.shear = shear
            self._rule.next_state = int(m.group(3))
            self._valid = True

        palette = self.palette()
        assert (isinstance(palette, QPalette))
        clr = QColor(255, 255, 128) if self._valid else QColor(255, 128, 128)
        palette.setColor(self.backgroundRole(), clr)
        self.setPalette(palette)

    def onTextChange(self):
        self.regen_rule()

    def gen_rule(self):
        if not self._rule:
            return

        self.setText('{0}{1}{2}'.format(
            self._rule.new_symbol,
            '<' if self._rule.shear == -1 else '>' if self._rule.shear == 1 else '=',
            self._rule.next_state)
        )
        self._valid = True