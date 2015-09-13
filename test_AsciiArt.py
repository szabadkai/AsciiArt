import unittest
from AsciiArt import AsciiArt, Pixel, PixelArray


class AsciiArtTests(unittest.TestCase):

    def test_object_creation(self):
        self.assertIsInstance(AsciiArt(), AsciiArt)

    def test_calculate_pixel_size(self):
        AsciiObj = AsciiArt("epam.png")
        ps = AsciiObj._calculate_pixel_size()
        self.assertAlmostEqual(ps, 288 / 100, 2)

    def test_draw_method(self):
        AsciiObj = AsciiArt("epam.png")
        img = AsciiObj.draw()
        self.assertGreater(len(img), 0)

    def test_pixel_object(self):
        px = Pixel((255,255,255))
        self.assertEqual(px.get_intensity(), 255*3)
