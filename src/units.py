import pygame
from pygame.sprite import _Group


class UnitManager:
    """This class is suposed to draw a manage unit interaction with each other."""

    def __init__(self) -> None:
        pass


class Unit(pygame.sprite.Sprite):
    """Every single unit inherits of this, holds the data for it's health, hero or not, sprit, and collider"""

    def __init__(self, *groups: _Group, image, rect, is_hero=False, hp=100) -> None:
        super().__init__(*groups)
        self.image = image
        self.rect = rect
        self.alive = True
        self.is_hero = is_hero
        self.hp = hp


class Enemy(Unit):
    """Enemy units, that spawns regularly, should move to the left side of the screen always and can't be controlled"""

    def __init__(self, *groups: _Group, image, rect, is_hero=False, hp=100) -> None:
        super().__init__(*groups, image=image, rect=rect, is_hero=is_hero, hp=hp)


class Troop(Unit):
    """Allied units that can be controlled, can select and when selected can move them by pressing the mouse"""

    def __init__(self, *groups: _Group, image, rect, is_hero=False, hp=100) -> None:
        super().__init__(*groups, image=image, rect=rect, is_hero=is_hero, hp=hp)
