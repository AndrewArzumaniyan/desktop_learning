from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instructions import *

class FinalWin(QWidget):
  def __init__(self, exp):
    super().__init__()
    self.exp = exp
    self.set_appear()
    self.initUI()
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
  
  def results(self):
    if self.exp.age < 7:
      self.index = 0
      return 'нет данных для этого возраста'
    
    self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10

    if self.exp.age == 7 or self.exp.age == 8:
      if self.index >= 21:
        return txt_res1
      #...

  def initUI(self):
    self.work_text = QLabel(txt_workheart + self.results())
    self.index_text = QLabel(txt_index + str(self.index))

    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
    self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
    self.setLayout(self.layout_line)