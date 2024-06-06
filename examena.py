import sys
from gpiozero import Button, LED
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer

# Definir los pines GPIO conectados a los botones y las salidas
HS_01_PIN = 17
HS_02_PIN = 18
HS_03_PIN = 27
PL_01_PIN = 23
PL_02_PIN = 24

# Inicializar los botones y LEDs utilizando gpiozero
HS_01 = Button(HS_01_PIN)
HS_02 = Button(HS_02_PIN)
HS_03 = Button(HS_03_PIN)
PL_01 = LED(PL_01_PIN)
PL_02 = LED(PL_02_PIN)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de GPIO con PyQt5 y gpiozero")
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

        self.update_ui()

        # Crear un temporizador para actualizar el estado de las salidas cada 100 ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_output_state)
        self.timer.start(100)

        # Variable para controlar el estado de HS-03
        self.HS_03_state = False

    def update_ui(self):
        self.update_button_state(self.label_HS_01, HS_01.is_pressed)
        self.update_button_state(self.label_HS_02, HS_02.is_pressed)
        self.update_button_state(self.label_HS_03, self.HS_03_state)

    def update_button_state(self, label, state):
        if state:
            label.setText(label.text().split(':')[0] + ": Activado")
            label.setStyleSheet("color: green")
        else:
            label.setText(label.text().split(':')[0] + ": Desactivado")
            label.setStyleSheet("color: red")

    def update_output_state(self):
        # Lógica para el foco (PL-01)
        if not self.HS_03_state and HS_01.is_pressed:
            PL_01.blink(on_time=2, off_time=2)

        # Lógica para PL-02
        if not self.HS_03_state and HS_02.is_pressed:
            PL_02.on()
        else:
            PL_02.off()

    def toggle_HS_03(self):
        self.HS_03_state = not self.HS_03_state

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



