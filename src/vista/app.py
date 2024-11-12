import tkinter as tk
from tkinter import ttk, messagebox
from src.logica.conversor import ConversorMoneda

class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")
        self.conversor = ConversorMoneda()

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Entrada de monto
        ttk.Label(self.frame, text="Monto:").grid(row=0, column=0, sticky=tk.W)
        self.monto_entry = ttk.Entry(self.frame, width=20)
        self.monto_entry.grid(row=0, column=1, sticky=tk.W)

        # Moneda de origen
        ttk.Label(self.frame, text="De:").grid(row=1, column=0, sticky=tk.W)
        self.origen_combo = ttk.Combobox(self.frame, values=['USD', 'EUR', 'JPY'], width=10)
        self.origen_combo.grid(row=1, column=1, sticky=tk.W)
        self.origen_combo.current(0)

        # Moneda de destino
        ttk.Label(self.frame, text="A:").grid(row=2, column=0, sticky=tk.W)
        self.destino_combo = ttk.Combobox(self.frame, values=['USD', 'EUR', 'JPY'], width=10)
        self.destino_combo.grid(row=2, column=1, sticky=tk.W)
        self.destino_combo.current(1)

        # Botón de conversión
        self.convertir_btn = ttk.Button(self.frame, text="Convertir", command=self.convertir)
        self.convertir_btn.grid(row=3, column=1, sticky=tk.W)

        # Resultado de la conversión
        self.resultado_label = ttk.Label(self.frame, text="Resultado: ")
        self.resultado_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)

    def convertir(self):
        try:
            monto = float(self.monto_entry.get())
            moneda_origen = self.origen_combo.get()
            moneda_destino = self.destino_combo.get()
            resultado = self.conversor.convertir(monto, moneda_origen, moneda_destino)
            self.resultado_label.config(text=f"Resultado: {resultado:.2f} {moneda_destino}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()
