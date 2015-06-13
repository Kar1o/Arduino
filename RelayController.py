__author__ = 'k'

import sys
import Arduino
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class WindowRelay(QWidget):

    def __init__(self):
        super(WindowRelay, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.setGeometry(100, 100, 420, 380)
        self.setWindowTitle('Relay Controller')
        self.set_buttons()

        self.show()

    def set_buttons(self):

        btn_switch1 = QPushButton('1', self)
        btn_switch1.setToolTip('Swith <b>1</b>')
        btn_switch1.clicked.connect(Arduino.switch1_on())
        btn_switch1.resize(btn_switch1.sizeHint())
        btn_switch1.move(100, 100)

        btn_switch2 = QPushButton('2', self)
        btn_switch2.setToolTip('Switch <b>2</b>')
        btn_switch2.clicked.connect(Arduino.switch2_on())
        btn_switch2.resize(btn_switch2.sizeHint())
        btn_switch2.move(100, 150)

        btn_switch3 = QPushButton('3', self)
        btn_switch3.setToolTip('Switch <b>3</b>')
        btn_switch3.clicked.connect(Arduino.switch3_on())
        btn_switch3.resize(btn_switch3.sizeHint())
        btn_switch3.move(100, 200)

        btn_switch4 = QPushButton('4', self)
        btn_switch4.setToolTip('Switch <b>4</b>')
        btn_switch4.clicked.connect(Arduino.switch4_on())
        btn_switch4.resize(btn_switch4.sizeHint())
        btn_switch4.move(100, 250)

        btn_all_off = QPushButton('ON', self)
        btn_all_off.setCheckable(True)
        btn_all_off.setToolTip('Switch <b>all on</b>')
        btn_all_off.clicked.connect(Arduino.switch_off())

        btn_all_off.resize(btn_all_off.sizeHint())
        btn_all_off.move(200, 125)

        btn_all_on = QPushButton('OFF', self)
        btn_all_on.setToolTip('Switch <b>all on</b>')
        btn_all_on.clicked.connect(Arduino.switch_on())
        btn_all_on.resize(btn_all_on.sizeHint())
        btn_all_on.move(200, 225)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(Arduino.close)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.move(190, 320)
        qbtn.setToolTip('Click to Quit')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = WindowRelay()
    sys.exit(app.exec_())
