import tkinter as tk
from tkinter import messagebox

# Clase ConversorMoneda basada en el archivo conversor.py
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

# Clase para la GUI usando tkinter
class ConversorMonedaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moneda")
        self.conversor = ConversorMoneda()

        # Etiquetas y entradas
        tk.Label(root, text="Monto:").grid(row=0, column=0, padx=10, pady=10)
        self.monto_entry = tk.Entry(root)
        self.monto_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Moneda de origen:").grid(row=1, column=0, padx=10, pady=10)
        self.moneda_origen = tk.StringVar(root)
        self.moneda_origen.set("USD")  # valor por defecto
        self.origen_menu = tk.OptionMenu(root, self.moneda_origen, "USD", "EUR", "JPY")
        self.origen_menu.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Moneda de destino:").grid(row=2, column=0, padx=10, pady=10)
        self.moneda_destino = tk.StringVar(root)
        self.moneda_destino.set("EUR")  # valor por defecto
        self.destino_menu = tk.OptionMenu(root, self.moneda_destino, "USD", "EUR", "JPY")
        self.destino_menu.grid(row=2, column=1, padx=10, pady=10)

        # Botón de conversión
        self.convertir_btn = tk.Button(root, text="Convertir", command=self.convertir_monedas)
        self.convertir_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Resultado
        self.resultado_label = tk.Label(root, text="Resultado: ")
        self.resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

    def convertir_monedas(self):
        try:
            # Obtiene el monto e intenta convertirlo a float
            monto = float(self.monto_entry.get())
            moneda_origen = self.moneda_origen.get()
            moneda_destino = self.moneda_destino.get()
            # Realiza la conversión
            resultado = self.conversor.convertir(monto, moneda_origen, moneda_destino)
            # Muestra el resultado
            self.resultado_label.config(text=f"Resultado: {resultado:.2f} {moneda_destino}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception:
            messagebox.showerror("Error", "Entrada no válida")

# Código para ejecutar la interfaz gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorMonedaGUI(root)
    root.mainloop()
