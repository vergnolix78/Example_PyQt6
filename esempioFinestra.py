from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

finestra = QWidget()
finestra.setWindowTitle("La mia prima finestra")
finestra.show()

sys.exit(app.exec())