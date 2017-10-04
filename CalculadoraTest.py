import unittest
from calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_igual_a_cero(self):
        self.assertEqual(self.calc.obtener_resultado(), 0)

    # INICIA TEST SUMAR
    def test_sumar_2_mas_2_igual_4(self):
        self.calc.sumar(2, 2)
        self.assertEqual(self.calc.obtener_resultado(), 4)

    def test_sumar_3_mas_3_igual_6(self):
        self.calc.sumar(3, 3)
        self.assertEqual(self.calc.obtener_resultado(), 6)

    def test_sumar_1_negativo_mas_2_igual_1(self):
        self.calc.sumar(-1, 2)
        self.assertEqual(self.calc.obtener_resultado(), 1)

    def test_sumar_L_mas_2_igual_DatosIncorrectos(self):
        self.calc.sumar('L', 2)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    # INICIA TEST RESTAR
    def test_restar_2_menos_2_igual_0(self):
        self.calc.restar(2, 2)
        self.assertEqual(self.calc.obtener_resultado(), 0)

    def test_restar_3_menos_3_igual_0(self):
        self.calc.restar(3, 3)
        self.assertEqual(self.calc.obtener_resultado(), 0)

    def test_restar_1_negativo_menos_2_igual_3_negativo(self):
        self.calc.restar(-1, 2)
        self.assertEqual(self.calc.obtener_resultado(), -3)

    def test_restar_L_menos_2_igual_DatosIncorrectos(self):
        self.calc.restar('L', 2)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    # INICIA TEST MULTIPLICAR
    def test_mult_2_por_2_igual_4(self):
        self.calc.multiplicar(2, 2)
        self.assertEqual(self.calc.obtener_resultado(), 4)

    def test_mult_3_por_3_igual_9(self):
        self.calc.multiplicar(3, 3)
        self.assertEqual(self.calc.obtener_resultado(), 9)

    def test_mult_1_negativo_por_2_igual_2_negativo(self):
        self.calc.multiplicar(-1, 2)
        self.assertEqual(self.calc.obtener_resultado(), -2)

    def test_mult_L_por_2_igual_DatosIncorrectos(self):
        self.calc.multiplicar('L', 2)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    # INICIA TEST DIVIDIR
    def test_divide_2_entre_2_igual_1(self):
        self.calc.dividir(2, 2)
        self.assertEqual(self.calc.obtener_resultado(), 1)

    def test_divide_3_entre_3_igual_1(self):
        self.calc.dividir(3, 3)
        self.assertEqual(self.calc.obtener_resultado(), 1)

    def test_divide_1_negativo_entre_2_igual_0_5_negativo(self):
        self.calc.dividir(-1, 2)
        self.assertEqual(self.calc.obtener_resultado(), -0.5)

    def test_divide_L_entre_2_igual_DatosIncorrectos(self):
        self.calc.dividir('L', 2)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    def test_divide_0_entre_0_igual_Indeterminado(self):
        self.calc.dividir(0, 0)
        self.assertEqual(self.calc.obtener_resultado(), 'Indeterminado')

    def test_divide_3_entre_0_igual_Infinito(self):
        self.calc.dividir(3, 0)
        self.assertEqual(self.calc.obtener_resultado(), 'Infinito')

    def test_divide_0_entre_21_igual_0_0(self):
        self.calc.dividir(3, 0)
        self.assertEqual(self.calc.obtener_resultado(), 'Infinito')

    # INICIA TEST POTENCIA
    def test_potencia_2_a_2_igual_4(self):
        self.calc.potencia(2, 2)
        self.assertEqual(self.calc.obtener_resultado(), 4)

    def test_potencia_3_a_3_igual_27(self):
        self.calc.potencia(3, 3)
        self.assertEqual(self.calc.obtener_resultado(), 27)

    def test_potencia_1_negativo_a_2_igual_1(self):
        self.calc.potencia(-1, 2)
        self.assertEqual(self.calc.obtener_resultado(), 1)

    def test_potencia_2_a_1_negativo_igual_0_5(self):
        self.calc.potencia(2, -1)
        self.assertEqual(self.calc.obtener_resultado(), 0.5)

    def test_potencia_0_a_0_negativo_igual_1(self):
        self.calc.potencia(0, 0)
        self.assertEqual(self.calc.obtener_resultado(), 1)

    def test_potencia_L_a_2_igual_DatosIncorrectos(self):
        self.calc.potencia('L', 2)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    # INICIA TEST RAÍZ
    def test_raiz_9_a_2_igual_3(self):
        self.calc.raiz(9, 2)
        self.assertEqual(self.calc.obtener_resultado(), 3)

    def test_raiz_27_a_3_igual_3(self):
        self.calc.raiz(27, 3)
        self.assertEqual(self.calc.obtener_resultado(), 3)

    def test_raiz_1_negativo_a_2_igual_1(self):
        self.calc.raiz(-1, 2)
        self.assertEqual(self.calc.obtener_resultado(),
                         6.123233995736766e-17 + 1j)

    def test_raiz_2_a_0_igual_0_5(self):
        self.calc.raiz(2, 0)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    def test_raiz_L_a_2_igual_DatosIncorrectos(self):
        self.calc.raiz('L', 2)
        self.assertEqual(self.calc.obtener_resultado(), 'Datos Incorrectos')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
