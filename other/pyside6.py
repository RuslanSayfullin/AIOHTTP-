import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Example")

        # Create a label widget
        label = QLabel("Hello, PySide6!", self)
        label.selfAlignment(Qt.AlignCenter)

        # Set the central widget of the main window
        self.setCentralWidget(label)

# Create a QApplication instance
app = QApplication(sys.argv)

# Create and show the main window
window = MyWindow()
window.show()

# Start the event loop
sys.exit(app.exec())
