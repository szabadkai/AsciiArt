from PIL import Image


class AsciiArt:
    def __init__(self, img_file_path="JUST_FOR_TESTING"):
        if img_file_path != "JUST_FOR_TESTING":
            self._load_image(img_file_path)

    FINAL_WIDTH = 100.0

    def _load_image(self, img_file_path):
        self.img = Image.open(img_file_path)
        self.px = self.img.load()

    def _calculate_pixel_size(self):
        return self.img.width / self.FINAL_WIDTH

    def draw(self):
        img_string = ""
        for y in range(self.img.height)[::2]:
            for x in range(self.img.width)[::2]:
                char_to_draw = " " if self.px[x, y][0] < 255 else "#"
                img_string += char_to_draw
            img_string += "\n"
        return img_string


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f', '--file', help='Specify an Ipython notebook if you only want to convert one. '
                                             '(This will overwrite default.)')
    args = parser.parse_args()

    if args.file is None:
        print("Add image path to work with!")
        exit()

    a = AsciiArt(args.file)
    print(a.draw())
