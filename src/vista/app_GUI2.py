from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QGridLayout
)
from PyQt6.QtCore import Qt
import sys
from src.logica.conversor import ConversorMoneda  # Importar la clase ConversorMoneda desde conversor.py

class ConversorMonedaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("$ Converter")
        self.setGeometry(100, 100, 300, 200)

        # Inicializar el conversor
        self.conversor = ConversorMoneda()

        # Crear los elementos de la interfaz
        self.monto_label = QLabel("Convert")
        self.monto_entry = QLineEdit()
        self.monto_entry.setText("0")  # Valor inicial

        self.resultado_label = QLabel("Result")
        self.resultado_display = QLabel("0")  # Display del resultado

        # Selección de moneda de origen
        self.from_label = QLabel("From")
        self.moneda_origen_combo = QComboBox()
        self.moneda_origen_combo.addItems(["USD", "EUR", "JPY"])  # Lista de monedas

        # Selección de moneda de destino
        self.to_label = QLabel("To")
        self.moneda_destino_combo = QComboBox()
        self.moneda_destino_combo.addItems(["USD", "EUR", "JPY"])  # Lista de monedas

        # Botón de conversión
        self.convertir_btn = QPushButton("Convert")
        self.convertir_btn.clicked.connect(self.convertir_monedas)

        # Layout principal
        main_layout = QVBoxLayout()

        # Layout para la entrada de monto
        monto_layout = QHBoxLayout()
        monto_layout.addWidget(self.monto_label)
        monto_layout.addWidget(self.monto_entry)
        main_layout.addLayout(monto_layout)

        # Layout para selección de monedas (From y To)
        from_to_layout = QGridLayout()
        from_group = QGroupBox("From")
        to_group = QGroupBox("To")

        from_layout = QVBoxLayout()
        from_layout.addWidget(self.moneda_origen_combo)
        from_group.setLayout(from_layout)

        to_layout = QVBoxLayout()
        to_layout.addWidget(self.moneda_destino_combo)
        to_group.setLayout(to_layout)

        from_to_layout.addWidget(from_group, 0, 0)
        from_to_layout.addWidget(to_group, 0, 1)
        main_layout.addLayout(from_to_layout)

        # Layout para el resultado
        result_layout = QHBoxLayout()
        result_layout.addWidget(self.resultado_label)
        result_layout.addWidget(self.resultado_display)
        main_layout.addLayout(result_layout)

        # Botón de conversión en la parte inferior
        main_layout.addWidget(self.convertir_btn, alignment=Qt.AlignmentFlag.AlignRight)

        # Establecer el layout principal en el widget central
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def convertir_monedas(self):
        try:
            monto = float(self.monto_entry.text())
            moneda_origen = self.moneda_origen_combo.currentText()
            moneda_destino = self.moneda_destino_combo.currentText()
            resultado = self.conversor.convertir(monto, moneda_origen, moneda_destino)
            self.resultado_display.setText(f"{resultado:.2f}")
        except ValueError as e:
            self.resultado_display.setText("Error")

# Código para ejecutar la interfaz gráfica
def main():
    app = QApplication(sys.argv)
    window = ConversorMonedaGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
