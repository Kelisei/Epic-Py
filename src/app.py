import pygame as pg
import numpy
from src.image_manager import ImageManager
from math import ceil
class App:
    def __init__(self) -> None:
        pg.init()
        self.size = (1300, 800)
        self.screen = pg.display.set_mode(self.size)
        pg.display.set_caption("EPIC WAR CLONE")
        self.clock = pg.time.Clock()
        self.manager = ImageManager()
        self.manager.load_from_memory('image_load')
        self.manager.load_image('bg', 'src/images/test_parallax.png')
        self.font = pg.font.Font('src/fonts/BebasNeue-Regular.ttf', 128)
        self.flag_exit = False
        self.current_screen = 0
        self.run()
    def run(self):
        while not self.flag_exit:
            match self.current_screen:
                case 0:
                    self.main_menu()
                case 1:
                    self.game_screen()
        
       
    def game_screen(self):
        left, right = (False, False)
        scroll = 0
        bg = self.manager.get_image('bg')
        tiles = ceil(self.size[0] / bg.get_width()) + 4 
        while not self.flag_exit and self.current_screen == 1:
            self.update()
            self.draw(bg, scroll, tiles)
            pg.display.update()
            self.clock.tick(60)
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.flag_exit= True
                    case pg.KEYDOWN:
                        match event.key:
                            case pg.K_LEFT:
                                left = True
                            case pg.K_RIGHT:
                                right = True
                            case pg.K_ESCAPE:
                                self.current_screen = 0
                    case pg.KEYUP:
                        match event.key:
                            case pg.K_LEFT:
                                left = False
                            case pg.K_RIGHT:
                                right = False

            if left:
                scroll += 10
            elif right:
                scroll -= 10
            if scroll > 0:
                scroll = 0
            elif scroll < -(bg.get_width() * 4):
                scroll =  -(bg.get_width() * 4)

    def update(self):
        """Here we update the game logic, like unit positions"""
        pass

    def draw(self, bg:pg.Surface, scroll:int, tiles:int):
        """Here we do the drawing of graphics"""
        for x in range(0, tiles):
           self.screen.blit(bg, (x* bg.get_width() + scroll,0))

    def main_menu(self):
        self.screen.fill((69, 63, 60))
        text = self.font.render('EPIC PY', True, (255, 255, 255))
        secondary = self.font.render('PRESS ANY KEY TO GAME', True, (0, 0, 0))
        self.screen.blit(text, (500,0))
        self.screen.blit(secondary, (150,600))
        while not self.flag_exit and self.current_screen == 0:
            pg.display.update()
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        self.flag_exit= True
                    case pg.KEYDOWN:
                        if pg.K_SPACE:
                            self.current_screen = 1
    @classmethod
    def start(cls):
        app = App()
