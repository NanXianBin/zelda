import pygame
from pygame.sprite import Sprite


class Alien3(Sprite):
    """一个代表舰队中单个外星人的类."""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外来图像并设置其矩形属性.
        self.image = pygame.image.load('images/alien1-3.png')
        self.rect = self.image.get_rect()

        # 在屏幕的左上方附近开始每个新的外星人.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置.
        self.y = float(self.rect.x)

    def check_edges(self):
        """如果外星人在屏幕的边缘，则返回True."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """将外星人向下移动."""
        self.y += self.settings.alien_speed
        self.rect.y = self.y
