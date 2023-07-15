import pygame


class ImageManager:
    def __init__(self) -> None:
        self.images = {}

    def load_image(self, image_name: str, image_path: str):
        """Loads an image and turns it into a surface that can be accesed by the given name, also convertis it for performance"""
        self.images[image_name] = pygame.image.load(image_path).convert()

    def load_from_memory(self):
        pass
    
    def get_image(self, image_name:str):
        return self.images[image_name] 