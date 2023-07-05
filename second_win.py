from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from instructions import *

class TestWin(QWidget):
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
    self.fio = QLabel(fio_txt)
    self.fio_area = QLineEdit('Ф.И.О.')
    self.time = QLabel('00:00:15')
    #...
    self.v_layout1 = QVBoxLayout()
    self.v_layout2 = QVBoxLayout()

    self.v_layout1.addWidget(self.fio)
    #...

    self.v_layout2.addWidget(self.timer)

    self.main_layout = QHBoxLayout()
    self.main_layout.addLayout(self.v_layout1)
    self.main_layout.addLayout(self.v_layout2)

    self.setLayout(self.main_layout)

  def connects(self):
    pass