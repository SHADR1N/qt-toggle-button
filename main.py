import sys

from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checkbox = QtWidgets.QCheckBox(self)
        self.checkbox.show()
        self.checkbox.setCheckState(QtCore.Qt.CheckState.Unchecked)


class ToggleSwitch(QtWidgets.QWidget):
    def __init__(self,
                 parent=None,
                 scale=1,
                 background_toggle="#FFF",
                 checked_color="#4A8BE1",
                 unchecked_color="#A7A2A9"
                 ):
        super().__init__(parent=parent)
        self.checked = False
        self.scale = scale
        self.size_round = int(25 * self.scale)
        self.size_field = (60 * self.scale, int(self.size_round * 1.2))

        self.style = """
    * {
        background: black;
    }
    
    QCheckBox {
        border: 0px solid #A9ACA9;
        border-radius: {BR17}px;
        background: {QCB-};
    }
    
    QCheckBox:checked {
        border: 0px solid #A9ACA9;
        border-radius: {BR17}px;
        background: {QCB+};
    }
    
    QCheckBox::indicator {
        border: none;
        background: none;
        width: 0px;
        height: 0px;
    }
    
    QLabel#roundLabel {
        border: 0px solid #A9ACA9;
        border-radius: {BR12}px;
        background: {BGTGL};
    }

"""

        br12 = int(self.size_round / 2)
        br17 = int(self.size_field[1] / 2)

        updated_style = self.style.replace("{BR17}", str(br17))
        updated_style = updated_style.replace("{BR12}", str(br12))

        updated_style = updated_style.replace("{BGTGL}", str(background_toggle))
        updated_style = updated_style.replace("{QCB-}", str(unchecked_color))
        self.style = updated_style.replace("{QCB+}", str(checked_color))

        self.initUI()

    def setChecked(self, *args):
        self.checked = not self.checked
        self.field.checkbox.setChecked(self.checked)
        self.field.update()

        self.field_layer.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight if self.checked else QtCore.Qt.AlignmentFlag.AlignLeft)
        self.field_layer.update()

    def initUI(self):
        self.setStyleSheet(self.style)
        self.layer = QtWidgets.QVBoxLayout()
        self.layer.setSpacing(0)
        self.layer.setContentsMargins(*[0] * 4)

        self.field = MyWidget()
        self.field.setObjectName(u"fieldWidget")
        self.field.checkbox.setFixedSize(*self.size_field)
        self.field.setFixedSize(*self.size_field)
        self.field.mouseReleaseEvent = self.setChecked
        self.field.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.field_layer = QtWidgets.QHBoxLayout()
        self.field_layer.setSpacing(0)
        self.field_layer.setContentsMargins(*[0] * 4)

        self.round = QtWidgets.QLabel(self.field)
        self.round.setText("")
        self.round.setFixedSize(self.size_round, self.size_round)
        self.round.setObjectName(u"roundLabel")

        self.field_layer.addWidget(self.round, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.field.setLayout(self.field_layer)

        self.layer.addWidget(self.field, 0, QtCore.Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layer)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    window = ToggleSwitch(
        scale=1,
        checked_color="red",
        unchecked_color="#42BFDD",
        background_toggle="#F0F6F6"
    )
    window.setWindowTitle("QtToggleSwitch created by SHADRIN")
    window.setMinimumSize(300, 300)
    window.show()

    sys.exit(app.exec())
