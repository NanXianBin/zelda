import pygame

from pygame.sprite import Sprite


class Heart(Sprite):
    """一个管理心的类."""

    def __init__(self, ai_game):
        """初始化心并设置其起始位置."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载心图像并获得其矩形.
        self.image = pygame.image.load('images/心.png')
        self.rect = self.image.get_rect()


    def blitme(self):
        """在当前位置绘制心."""
        self.screen.blit(self.image, self.rect)