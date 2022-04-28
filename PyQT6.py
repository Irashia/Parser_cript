from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QSplitter
import sys
#https://habr.com/ru/company/skillfactory/blog/599599/

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Keep a reference to combobox on self, so we can access it in our methods.
        self.combobox = QComboBox()
        self.combobox.addItems(['One', 'Two', 'Three', 'Four'])
        self.combobox.setEditable(True)
        self.combobox.currentTextChanged.connect(self.current_text_changed)
#----------------------
        self.setFixedSize(QSize(500, 300))
#----------------------

        layout = QVBoxLayout()
        layout.addWidget(self.combobox)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        #-------------------------------------------------------------------------------------

        #self.button_is_checked = True

        self.setWindowTitle("My App")

        '''self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked, 'This')'''

    def current_text_changed(self, s):
        print("Current text: ", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


'''
self.setMinimumSize(QSize(500, 300))
self.setMaximumSize(QSize(1300, 800))
'''