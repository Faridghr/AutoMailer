import sys
from PyQt5.QtWidgets import QApplication
from ui import EmailSenderApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSenderApp()
    window.show()
    sys.exit(app.exec_())
