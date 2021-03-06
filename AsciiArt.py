from PIL import Image
import os.path


class Pixel:
    def __init__(self, rgb):
        self.rgb = rgb

    def get_intensity(self):
        return sum(self.rgb)/765.0


class AsciiArt:
    def __init__(self, img_file_path="JUST_FOR_TESTING"):
        if img_file_path != "JUST_FOR_TESTING":
            self._load_image(img_file_path)

    FINAL_WIDTH = 100

    def _load_image(self, img_file_path):
        self.img = Image.open(img_file_path)
        self.px = self.img.load()
        self.pixel_size = self._calculate_pixel_size()

    def _calculate_pixel_size(self):
        px_size =  self.img.width / self.FINAL_WIDTH
        return 1 if px_size < 1 else px_size

    def get_char(self, intensity):
        intensity_string = " .:-=+*#%@"[::-1]
        steps = len(intensity_string)-1
        return intensity_string[int(steps * intensity)]

    def draw(self):
        img_string = ""
        for y in range(self.img.height)[::self.pixel_size]:
            for x in range(self.img.width)[::self.pixel_size]:
                char_to_draw = self.get_char(Pixel(self.px[x, y]).get_intensity())
                img_string += char_to_draw
            img_string += "\n"
        return img_string


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--file')
    args = parser.parse_args()

    if args.file is None:
        print("Add image path to work with!")
        exit()
    elif not os.path.isfile(args.file):
        print("No Image "+args.file+" found!")
        exit()

    a = AsciiArt(args.file)
    print(a.draw())
