from PIL import Image
from pathlib import Path
import glob


def pixelate_images(self):
    original_path = Path("original_images")
    pixelated_path = Path("pixelated_images")

    # pixelated_path.mkdir(exist_ok=True)

    for png_file in glob.glob('**/*.png'):
        full_file_path = str(png_file)
        image_file = Image.open(full_file_path)
        imgSmall = image_file.resize((6, 6), resample=Image.BILINEAR)

        result = imgSmall.resize(image_file.size, Image.NEAREST)

        new_file_name = Path(png_file).stem + '_pixelated.png'
        result.save(str(pixelated_path / new_file_name))


if __name__ == "__main__":
    print('main')
