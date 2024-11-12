import unittest
from src.logica.conversor import ConversorMoneda

class TestConversorMoneda(unittest.TestCase):
    def setUp(self):
        self.conversor = ConversorMoneda()

    def test_conversion_usd_to_eur(self):
        self.assertAlmostEqual(self.conversor.convertir(100, 'USD', 'EUR'), 85)

    def test_conversion_usd_to_jpy(self):
        self.assertAlmostEqual(self.conversor.convertir(100, 'USD', 'JPY'), 11000)

    def test_conversion_eur_to_jpy(self):
        self.assertAlmostEqual(self.conversor.convertir(100, 'EUR', 'JPY'), 13000)

    def test_misma_moneda(self):
        self.assertEqual(self.conversor.convertir(100, 'USD', 'USD'), 100)

    def test_moneda_invalida(self):
        with self.assertRaises(ValueError):
            self.conversor.convertir(100, 'USD', 'XYZ')

    def test_monto_invalido(self):
        with self.assertRaises(ValueError):
            self.conversor.convertir(-100, 'USD', 'EUR')

if __name__ == "__main__":
    unittest.main()
