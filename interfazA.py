import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interfaz de Usuario")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label_HS_01 = QLabel("HS-01: Desactivado", self)
        layout.addWidget(self.label_HS_01)

        self.label_HS_02 = QLabel("HS-02: Desactivado", self)
        layout.addWidget(self.label_HS_02)

        self.label_HS_03 = QLabel("HS-03: Desactivado", self)
        layout.addWidget(self.label_HS_03)

        self.label_PL_01 = QLabel("PL-01: Desactivado", self)
        layout.addWidget(self.label_PL_01)

        self.label_PL_02 = QLabel("PL-02: Desactivado", self)
        layout.addWidget(self.label_PL_02)

        self.button_HS_03 = QPushButton("Botón Mantenido (HS-03)", self)
        layout.addWidget(self.button_HS_03)

        self.button_HS_03.clicked.connect(self.toggle_HS_03)

        self.setLayout(layout)

        # Inicializar el estado de HS_03
        self.HS_03_state = False

        self.update_ui()

        # Crear un temporizador para actualizar la interfaz cada 100 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(100)

    def update_ui(self):
        # Simular el estado de los botones y las salidas
        self.update_label(self.label_HS_01, self.HS_03_state)
        self.update_label(self.label_HS_02, self.HS_03_state)
        self.update_label(self.label_HS_03, self.HS_03_state)
        self.update_label(self.label_PL_01, self.HS_03_state)
        self.update_label(self.label_PL_02, self.HS_03_state)

    def update_label(self, label, state):
        if state:
            label.setText(label.text().split(':')[0] + ": Activado")
            label.setStyleSheet("color: green")
        else:
            label.setText(label.text().split(':')[0] + ": Desactivado")
            label.setStyleSheet("color: red")

    def toggle_HS_03(self):
        self.HS_03_state = not self.HS_03_state

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


