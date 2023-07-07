from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
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
    self.work_text = QLabel(txt_workheart + self.results())
    self.index_text = QLabel(txt_index + str(self.index))


    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
    self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
    self.setLayout(self.layout_line)