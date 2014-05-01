from PySide.QtCore import QModelIndex, Qt
from PySide.QtGui import QItemDelegate

from forms.WidgetRule import Widget_Rule
from turing.turing import Rule


class Cell_Delegate(QItemDelegate):
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        widget = Widget_Rule(QWidget)
        return widget

    def setEditorData(self, wdg, index):
        assert (isinstance(index, QModelIndex))
        r = index.row()
        c = index.column()
        rule = index.data(Qt.EditRole)

        assert (isinstance(rule, Rule))
        assert (isinstance(wdg, Widget_Rule))
        wdg.rule = rule

    def setModelData(self, wdg, QAbstractItemModel, index):
        assert (isinstance(index, QModelIndex))
        index.model().reset()
        assert (isinstance(wdg, Widget_Rule))

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QItemDelegate.updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex)





