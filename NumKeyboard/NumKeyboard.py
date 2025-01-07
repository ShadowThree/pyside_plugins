try:
    from .NumKeyboard_ui import Ui_NumKeyboard
except:
    from NumKeyboard_ui import Ui_NumKeyboard

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from typing import Final

__version__ = "1.0.0"

class NumKeyboard(QWidget, Ui_NumKeyboard):
    numKeyboard_clicked = Signal(int)

    NUM_KEYBOARD_DEL: Final = -1
    NUM_KEYBOARD_ABC: Final = -2
    NUM_KEYBOARD_ENTER: Final = -3
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.numBtn_0.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_0))
        self.numBtn_1.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_1))
        self.numBtn_2.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_2))
        self.numBtn_3.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_3))
        self.numBtn_4.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_4))
        self.numBtn_5.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_5))
        self.numBtn_6.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_6))
        self.numBtn_7.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_7))
        self.numBtn_8.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_8))
        self.numBtn_9.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_9))
        self.numBtn_ABC.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_ABC))
        self.numBtn_DEL.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_DEL))
        self.numBtn_Enter.clicked.connect(lambda: self.numBtn_clicked(self.numBtn_Enter))
    
    def numBtn_clicked(self, btn):
        if btn == self.numBtn_ABC:
            self.numKeyboard_clicked.emit(self.NUM_KEYBOARD_ABC)
        elif btn == self.numBtn_DEL:
            self.numKeyboard_clicked.emit(self.NUM_KEYBOARD_DEL)
        elif btn == self.numBtn_Enter:
            self.numKeyboard_clicked.emit(self.NUM_KEYBOARD_ENTER)
        else:
            self.numKeyboard_clicked.emit(int(btn.text()))

    TOOLTIP: Final = "number keyboard"
    DOM_XML: Final = """
    <ui language='c++'>
        <widget class='NumKeyboard' name='numKeyboard'>
            <property name='geometry'>
                <rect>
                    <x>0</x>
                    <y>0</y>
                    <width>400</width>
                    <height>200</height>
                </rect>
            </property>
        </widget>
    </ui>
    """

def registerToDesigner():
    from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection
    QPyDesignerCustomWidgetCollection.registerCustomWidget(NumKeyboard, module="NumKeyboard", tool_tip=NumKeyboard.TOOLTIP, xml=NumKeyboard.DOM_XML)