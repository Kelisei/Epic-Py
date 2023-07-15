import pygame as pg
from src.image_manager import ImageManager

class App:
    def __init__(self) -> None:
        pg.init()
        size = (1300, 800)
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption("EPIC WAR CLONE")
        self.clock = pg.time.Clock()
        self.manager = ImageManager()
        self.manager.load_image('bg', 'src/images/test_parallax.png')
        self.run()

    def run(self):
        flag_exit = False
        while not flag_exit:
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(60)
            for event in pg.event.get():
                flag_exit = event.type == pg.QUIT

    def update(self):
        """Here we update the game logic, like unit positions"""
        pass

    def draw(self):
        """Here we do the drawing of graphics"""
        self.screen.blit(self.manager.get_image('bg'), (0,0))

    @classmethod
    def start(cls):
        app = App()
