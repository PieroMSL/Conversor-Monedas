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
