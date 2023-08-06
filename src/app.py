import pygame as pg
import numpy
from src.image_manager import ImageManager
from src.button import Button

class App:
    def __init__(self) -> None:
        pg.init()
        self.size = (1300, 800)
        self.screen = pg.display.set_mode(self.size)
        pg.display.set_caption("EPIC WAR CLONE")
        self.clock = pg.time.Clock()
        self.manager = ImageManager()
        self.manager.load_from_memory("image_load")
        self.font = pg.font.Font("src/fonts/BebasNeue-Regular.ttf", 128)
        self.flag_exit = False
        self.current_screen = 0
        self.run()

    def run(self):
        """This method manages the game state is in a constant loop except when the game is closed, checks for what
        screen is it supossed to be in, and loads it"""
        while not self.flag_exit:
            match self.current_screen:
                case 0:
                    self.main_menu()
                case 1:
                    self.game_screen()

    def game_screen(self):
        """This method is the prototyping scene for where the main game loop will happen, it's supossed
        to let you move around a level, a let you control units"""

        def scroll_background(new_scroll: int) -> int:
            # Function to modify the current background offset
            if new_scroll > 0:
                new_scroll = 0
            elif new_scroll < -(bg_width * (MAX_TILES - 1)):
                new_scroll = -(bg_width * (MAX_TILES - 1))
            return new_scroll

        # Constant definition
        SCROLL_SPEED = 10
        MAX_TILES = 5

        # Variable initialization
        keys_pressed = {pg.K_LEFT: False, pg.K_RIGHT: False}
        scroll = 0
        bg = self.manager.get_image("bg_01")
        bg_width = bg.get_width()

        while not self.flag_exit and self.current_screen == 1:
            self.update()
            self.draw(bg, bg_width, scroll, MAX_TILES)
            pg.display.update()
            self.clock.tick(60)

            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.flag_exit = True
                    case pg.KEYDOWN:
                        if event.key in keys_pressed:
                            keys_pressed[event.key] = True
                        elif event.key == pg.K_ESCAPE:
                            self.current_screen = 0
                    case pg.KEYUP:
                        if event.key in keys_pressed:
                            keys_pressed[event.key] = False

            # Actualizar dependiendo de que llave esta presionadas
            if keys_pressed[pg.K_LEFT]:
                scroll = scroll_background(scroll + SCROLL_SPEED)
            elif keys_pressed[pg.K_RIGHT]:
                scroll = scroll_background(scroll - SCROLL_SPEED)

    def update(self):
        """Here we update the game logic, like unit positions"""
        pass

    def draw(self, bg: pg.Surface, bg_width: int, scroll: int, tiles: int):
        """Here we do the drawing of graphics"""
        for x in range(0, tiles):
            self.screen.blit(bg, (x * bg_width + scroll, 0))

    def main_menu(self):
        """The main menu, is loaded at the start o when pressed to go here, should show the game title
        options, and an exit button."""
        start_btn = Button(self.font, text='Start', position=(0, 500))
        bg = self.manager.get_image_resized("mbg_01", self.size)
        self.screen.blit(bg, (0, 0))
        self.screen.blit(
            start_btn.surface, start_btn.position
        )
        while not self.flag_exit and self.current_screen == 0:
            pg.display.update()
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.flag_exit = True
                    case pg.KEYDOWN if event.key == pg.K_SPACE:
                        self.current_screen = 1

    @classmethod
    def start(cls):
        """Creates an instance of this class and starts the application"""
        app = App()
