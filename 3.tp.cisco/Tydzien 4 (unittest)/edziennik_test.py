import unittest
from edziennik import edziennik
class TestEdziennik(unittest.TestCase):
    def setUp(self):
        uczniowie = [
            "Dawid M",
            "Jan K",
            "Adam A",
        ]
        self.k = edziennik('2TP', uczniowie, "Gustaw M")

    def test_initial_value(self):
        self.assertEqual(self.k.klasa, "2TP")
        self.assertEqual(self.k.wychowawca, "Gustaw M")

    def test_dodaj_ucznia(self):
        self.k.nowy_uczen("Benji N")
        self.assertIn("Benji N", self.k.uczniowie)

    def test_usun_ucznia(self):
        self.k.usun_ucznia("Jan K")
        self.assertNotIn("Jan K", self.k.uczniowie)
        self.


