# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QListWidget, QLineEdit
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont 
from instr import *
from final_win import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        ''' окно в котором распологается приветствие '''
        super().__init__()
        
        #
        self.initUI()
        
        #
        self.connects()

        #
        self.show()

    def initUI(self):
        ''' создает графические элементы '''
        self.btn_text= QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_text.clicked.connect(self.next_click)

        ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()

main()