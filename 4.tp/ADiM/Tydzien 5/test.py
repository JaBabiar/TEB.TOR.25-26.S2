from gry import mainClass
import unittest

class test_gry(unittest.TestCase):
    def setUp(self):
        self.mc = mainClass(["A", "b", "C"], 200)

    def test_dodaj_do_listy(self):
        self.mc.dodaj_do_listy("d")
        self.assertIn("d", self.mc.lista)

    def test_usun_z_listy(self):
        self.mc.dodaj_do_listy("d")
        self.mc.usun_z_listy("d")
        self.assertNotIn("d", self.mc.lista)

    def test_value_error_saldo(self):
        with self.assertRaises(ValueError):
            self.mc.dodaj_saldo(-100)

    def test_type_error_saldo(self):
        with self.assertRaises(TypeError):
            self.mc.dodaj_saldo("jbhasdjbhjabsdhjbhasd")
    def test_name_error(self):


