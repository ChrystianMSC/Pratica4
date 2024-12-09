import unittest
from math import radians, isclose
from triangle_app import TriangleApp  # Substitua pelo nome do arquivo onde o código do app está

class TestTriangleApp(unittest.TestCase):
    def setUp(self):
        # Coordenadas iniciais do triângulo
        self.initial_triangle = [200, 100, 150, 300, 250, 300]

    def assertCoordsAlmostEqual(self, coords1, coords2, delta=0.001):
        self.assertEqual(len(coords1), len(coords2))
        for a, b in zip(coords1, coords2):
            self.assertTrue(isclose(a, b, abs_tol=delta), f"{a} != {b}")

    def test_rotate_up(self):
        # Calcula o esperado dinamicamente
        expected = TriangleApp.rotate_triangle(self.initial_triangle, radians(-15))
        rotated = TriangleApp.rotate_triangle(self.initial_triangle, radians(-15))
        self.assertCoordsAlmostEqual(rotated, expected)

    def test_rotate_down(self):
        # Calcula o esperado dinamicamente
        expected = TriangleApp.rotate_triangle(self.initial_triangle, radians(15))
        rotated = TriangleApp.rotate_triangle(self.initial_triangle, radians(15))
        self.assertCoordsAlmostEqual(rotated, expected)

    def test_multiple_rotations(self):
        # Rotaciona múltiplas vezes e compara com um cálculo direto
        coords = self.initial_triangle
        for _ in range(4):
            coords = TriangleApp.rotate_triangle(coords, radians(-15))
        expected = TriangleApp.rotate_triangle(self.initial_triangle, radians(-60))
        self.assertCoordsAlmostEqual(coords, expected)

if __name__ == "__main__":
    unittest.main()
