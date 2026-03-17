import unittest
from Gracz import Gracz

class TestGracza(unittest.TestCase):
    def setUp(self):
        # Tworzymy obiekt, który będzie dostępny we wszystkich testach jako self.g
        self.g = Gracz("Tester")

    def test_poczatkowy_stan(self):
        self.assertEqual(self.g.punkty, 0)
        self.assertEqual(self.g.nazwa, "Tester")

    def test_dodawania_punktow(self):
        self.g.dodaj_punkty(10)
        self.assertEqual(self.g.punkty, 10)

    def test_ekwipunku(self):
        self.g.zbierz_przedmiot("Miecz")
        self.assertIn("Miecz", self.g.ekwipunek)

    def test_ujemne_punkty_error(self):
        with self.assertRaises(ValueError):
            self.g.dodaj_punkty(-5)