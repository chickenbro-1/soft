import random
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
SPRAY_PARTICLES = 100
SPRAY_DIAMMETER = 10
class Canvas3(QLabel):
  def __init__(self,parent=None):
    super().__init__(parent)
    canvas = QPixmap(591,461)
    canvas.fill(QColor('white'))
    self.setPixmap(canvas)
    self.last_x, self.last_y = None, None
    self.pen_color = QColor('#000')
  def set_pen_color(self, c):
    self.pen_color = QColor(c)
  def mouseReleaseEvent(self, *args, **kwargs):
    self.last_x, self.last_y = None, None
  def mouseMoveEvent(self, e):
    if self.last_x is None:
      self.last_x = e.x()
      self.last_y = e.y()
      return
    painter = QPainter(self.pixmap())
    pen = painter.pen()
    pen.setWidth(4)
    pen.setColor(self.pen_color)
    painter.setPen(pen)
    painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
    painter.end()
    self.update()
    self.last_x = e.x()
    self.last_y = e.y()
