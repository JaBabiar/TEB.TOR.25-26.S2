import unittest
from Gracz import Gracz

class GraczTest(unittest.TestCase):
    def setUp(self):
        self.g = Gracz("Tester")

    def test_tworzenie_gracza(self):
        self.assertEqual(self.g.name, "Tester")
        self.assertEqual(self.g.points, 0)
    def test_dodaj_punkty(self):
        self.g.dodaj_punkty(10)
        self.assertEqual(self.g.points, 10)

    def test_podnoszenia_itemow(self):
        self.g.podnies_przedmiot("Miecz")
        self.assertIn("Miecz", self.g.ekwipunek)

    def test_blad_wartosci(self):
        with self.assertRaises(ValueError):
            self.g.dodaj_punkty(-5)

    def test_blad_typu(self):
        with self.assertRaises(TypeError):
            self.g.dodaj_punkty("5")
    def test_wyrzuc_item(self):
        self.g.podnies_przedmiot("Miecz")
        self.g.wyrzuc_item("Miecz")
        self.assertNotIn("Miecz", self.g.ekwipunek)
        
