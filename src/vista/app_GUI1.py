from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
import sys



# Clase ConversorMonedas
class ConversorMoneda:
    tasas_cambio = {
        ('USD', 'EUR'): 0.85,
        ('USD', 'JPY'): 110,
        ('EUR', 'JPY'): 130,
        ('EUR', 'USD'): 1 / 0.85,
        ('JPY', 'USD'): 1 / 110,
        ('JPY', 'EUR'): 1 / 130
    }

    def convertir(self, monto, moneda_origen, moneda_destino):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo")
        if moneda_origen == moneda_destino:
            return monto
        try:
            tasa = self.tasas_cambio[(moneda_origen, moneda_destino)]
        except KeyError:
            raise ValueError("Moneda no válida")
        return monto * tasa


# Ventana principal de la GUI
class ConversorMonedaGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conversor de Moneda")
        self.conversor = ConversorMoneda()

        # Configuración de los widgets
        self.monto_label = QLabel("Monto:")
        self.monto_entry = QLineEdit()

        self.moneda_origen_label = QLabel("Moneda de origen:")
        self.moneda_origen_combo = QComboBox()
        self.moneda_origen_combo.addItems(["USD", "EUR", "JPY"])

        self.moneda_destino_label = QLabel("Moneda de destino:")
        self.moneda_destino_combo = QComboBox()
        self.moneda_destino_combo.addItems(["USD", "EUR", "JPY"])

        self.convertir_btn = QPushButton("Convertir")
        self.convertir_btn.clicked.connect(self.convertir_monedas)

        self.resultado_label = QLabel("Resultado: ")

        # Diseño de la interfaz
        layout = QVBoxLayout()

        layout.addWidget(self.monto_label)
        layout.addWidget(self.monto_entry)

        layout.addWidget(self.moneda_origen_label)
        layout.addWidget(self.moneda_origen_combo)

        layout.addWidget(self.moneda_destino_label)
        layout.addWidget(self.moneda_destino_combo)

        layout.addWidget(self.convertir_btn)
        layout.addWidget(self.resultado_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def convertir_monedas(self):
        try:
            monto = float(self.monto_entry.text())
            moneda_origen = self.moneda_origen_combo.currentText()
            moneda_destino = self.moneda_destino_combo.currentText()

            resultado = self.conversor.convertir(monto, moneda_origen, moneda_destino)
            self.resultado_label.setText(f"Resultado: {resultado:.2f} {moneda_destino}")
        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))
        except Exception:
            QMessageBox.critical(self, "Error", "Entrada no válida")


# Código para ejecutar la interfaz gráfica
def main():
    app = QApplication(sys.argv)
    window = ConversorMonedaGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

