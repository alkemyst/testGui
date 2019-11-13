import sys
from MainWindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow

def quit_func():
    sys.exit(app.exec_())

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_a.clicked.connect(quit_func)

        # use self.ui here...


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())




