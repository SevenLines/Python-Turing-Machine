import re
from PyQt4.QtCore import QModelIndex, Qt

from PyQt4.QtGui import QItemDelegate

from forms.ui.WidgetRule import Widget_Rule
from turing.turing import Rule


class Cell_Delegate(QItemDelegate):
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        widget = Widget_Rule(QWidget)
        return widget

    def setEditorData(self, wdg, index):
        assert (isinstance(index, QModelIndex))
        r = index.row()
        c = index.column()
        rule = str(index.data(Qt.EditRole).toString())

        assert (isinstance(rule, str))
        rule = filter(None, re.split('\s|,', rule))

        assert (isinstance(wdg, Widget_Rule))
        wdg.symbol = rule[0]
        wdg.shear = rule[1]
        wdg.state = rule[2]

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex):
        QItemDelegate.setModelData(self, QWidget, QAbstractItemModel, QModelIndex)

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QItemDelegate.updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex)





