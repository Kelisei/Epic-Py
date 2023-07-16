from pygame import image as img
from pygame import Surface
from os.path import normpath
import pandas as pd
# import time


class ImageManager:
    def __init__(self):
        self.images = {}

    def load_image(self, image_name: str, image_path: str):
        """Loads an image and turns it into a surface that can be accesed by the given name, also convertis it for performance"""
        self.images[image_name] = img.load(normpath(image_path)).convert()

    def load_from_memory(self, file_name: str):
        """Load images from a CSV file in memory."""
        # start = time.time()
        try:
            file_path = normpath(f"src/{file_name}.csv")
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            print("File not found, loading default.")
        else:
            self.images.update(
                {
                    row["name"]: img.load(normpath(row["path"])).convert()
                    for _, row in df.iterrows()
                }
            )
        # print(time.time() - start)

    def get_image(self, image_name: str) -> Surface:
        """Get the image associated with the given name."""
        return self.images[image_name]
