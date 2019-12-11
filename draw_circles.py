import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor

 
class Circles(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Случайные окружности')
        self.drawCircle = False
        self.Circles = []
        draw_button = QPushButton('Лел', self)
        draw_button.resize(100, 50)
        draw_button.move(self.height() // 2, self.width() // 2)
        draw_button.clicked.connect(self.let_draw)
        
    
    def let_draw(self):
        self.drawCircle = True
        self.update()
    
    def draw_crc(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        ox = random.randint(100, 400)
        oy = random.randint(100, 400)
        radius = random.randint(10, 90)
        self.Circles.append((ox, oy, radius, radius))
        for circles in self.Circles:
            qp.drawEllipse(*circles)
        
       
    def paintEvent(self, event):
        if self.drawCircle is True:
           qp = QPainter()
           qp.begin(self)
           self.draw_crc(qp)
           qp.end()
           self.drawCircle = False
        
                      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    crc = Circles()
    crc.show()
    sys.exit(app.exec())         
