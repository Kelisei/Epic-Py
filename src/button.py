import pygame as pg


def get_center(size: int, width: int) -> int:
    return (size - width) / 2


class Button:
    def __init__(
        self,
        font: pg.font.Font,
        text="default",
        text_color=(255, 255, 255, 255),
        bg_color=None,
        position=(0, 0),
        centered=True,
        screen_width=1300,
    ):
        if not bg_color:
            self.surface = font.render(text, True, text_color)
        else:
            self.surface = font.render(text, True, text_color, bg_color)
            
        if centered:
            self.position = (
                get_center(screen_width, self.surface.get_width()),
                position[1],
            )
        else:
            self.position = position
