import pygame
from pygame.sprite import Sprite
 
class Bullet(Sprite):
    """一个管理从船上发射的子弹的类"""

    def __init__(self, ai_game):
        """在飞船的当前位置创建一个子弹对象."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/大师之剑.png')
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 将子弹的位置存储.
        self.y = float(self.rect.y)

    def update(self):
        """将子弹移到屏幕上."""
        # 更新子弹的小数点位置.
        self.y -= self.settings.bullet_speed
        # 更新矩形的位置.
        self.rect.y = self.y

    def draw_bullet(self):
        """将子弹画到屏幕上."""
        self.screen.blit(self.image, self.rect)
