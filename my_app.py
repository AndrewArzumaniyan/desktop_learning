from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from instructions import *
from second_win import *

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def initUI(self):
    self.hello_txt = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)
    self.btn_next = QPushButton(txt_next)

    self.layout = QVBoxLayout()
    self.layout.addWidget(self.hello_txt, alignment=Qt.AlignLeft)
    self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
    self.layout.addWidget(self.btn_next, alignment=Qt.AlignCenter)

    self.setLayout(self.layout)

  def next_click(self):
    self.hide()
    self.tw = TestWin()

  def connects(self):
    self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
mw = MainWindow()

app.exec_()