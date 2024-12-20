import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_yritetaan_lisata_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo,10)
  
    def test_yritetaan_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(11)

        self.assertAlmostEqual(saatu_maara, 10)
    
    def test_negatiivisen_lisaaminen_varastoon(self):
        ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-10)
        jalkeen = self.varasto.saldo

        self.assertAlmostEqual(ennen, jalkeen)

    def test_otetaan_negatiivinen_maara(self):
        saatu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(saatu_maara, 0)


    def test_kuvaus_oikein(self):
        self.varasto = Varasto(10)
        varasto_str = self.varasto.__str__()
        kuvaus = "saldo = 0, vielä tilaa 10"

        self.assertAlmostEqual(varasto_str,kuvaus)

    def test_liika_alkusaldo(self):
        self.varasto = Varasto(10,11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_alkusaldo(self):
        self.varasto = Varasto(10,-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_negatiivinen_tilavuus(self):

        self.varasto = Varasto(-1)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

