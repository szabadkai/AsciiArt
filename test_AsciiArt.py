import unittest
from AsciiArt import AsciiArt


class AsciiArtTests(unittest.TestCase):

    def test_object_creation(self):
        self.assertIsInstance(AsciiArt(), AsciiArt)

    def test_calculate_pixel_size(self):
        AsciiObj = AsciiArt("epam.png")
        ps = AsciiObj._calculate_pixel_size()
        self.assertAlmostEqual(ps, 288.0 / 100, 2)

    def test_draw_method(self):
        AsciiObj = AsciiArt("epam.png")
        img = AsciiObj.draw()
        self.assertGreater(len(img), 0)
