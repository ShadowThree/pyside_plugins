import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PySide6.QtCore import Slot

try:
    from . import NumKeyboard
except:
    import NumKeyboard

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(480, 272)

        self.numkb = NumKeyboard.NumKeyboard()
        self.numkb.numKeyboard_clicked.connect(self.numkb_click_cb)

        self.lineEdit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.numkb)
        self.setLayout(layout)
    
    @Slot(int)
    def numkb_click_cb(self, key):
        print(f"press {key}")
        if key == self.numkb.NUM_KEYBOARD_ABC:
            pass
        elif key == self.numkb.NUM_KEYBOARD_DEL:
            self.lineEdit.setText(self.lineEdit.text()[:-1])
        elif key == self.numkb.NUM_KEYBOARD_ENTER:
            pass
        else:
            self.lineEdit.setText(self.lineEdit.text() + str(key))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
