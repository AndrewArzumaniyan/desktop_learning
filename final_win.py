from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from instructions import *

class FinalWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def initUI(self):
    pass