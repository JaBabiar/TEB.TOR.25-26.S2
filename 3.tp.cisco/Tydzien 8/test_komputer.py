from Komputer import *
import unittest

class KomputerTest(unittest.TestCase):
    def setUp(self):
        self.k = Komputer("mango", ["Myszka", "Monitor", "Klawiatura"])

    def test_zwiekszenia_glosnosci(self):
        self.k.zarzadzaj_dzwiekiem(20)
        self.assertEqual(self.k.glosnosc, 100)

    def test_zmniejszania_glosnosci(self):
        self.k.zarzadzaj_dzwiekiem(-30)
        self.assertEqual(self.k.glosnosc, 70)

    def test_podepnij_urzadzenie(self):
        self.k.podepnij_urzadzenie('Pendrive')
        self.assertIn('Pendrive', self.k.peryferia)

    def test_odepnij_urzadzenie(self):
        self.k.podepnij_urzadzenie("Pendrive")
        self.k.odepnij_urzadzenie('Pendrive')
        self.assertNotIn('Pendrive', self.k.peryferia)

    def test_zly_typ_urzadzenie(self):
        with self.assertRaises(TypeError):
            self.k.podepnij_urzadzenie('Pendrive')


