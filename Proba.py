import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
                             QSplitter, QTextEdit, QApplication)
from PyQt5.QtCore import Qt


class SplitterExample(QWidget):
    def __init__(self):
        super(SplitterExample, self).__init__()
        self.initUI()

    def initUI(self):

                 # Инициализировать элемент управления
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)
        textedit = QTextEdit()

                 # Установите первыйSplitterНаправление расположения
        splitter1 = QSplitter(Qt.Horizontal)
                 # Является первымSplitterДобавьте элементы управления и установите пространство, занимаемое двумя элементами управления
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

                 # Установите второеSplitterНаправление расположения, первоеSplitterВложенный во второй
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

                 # Установить глобальный макет
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle('QSplitter  пример')
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SplitterExample()
    demo.show()
    sys.exit(app.exec_())