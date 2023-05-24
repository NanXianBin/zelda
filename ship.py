import pygame
 
from pygame.sprite import Sprite
 
class Ship(Sprite):
    """一个管理飞船的类."""
 
    def __init__(self, ai_game):
        """初始化船舶并设置其起始位置."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载船舶图像并获得其矩形.
        self.image = pygame.image.load('images/link.jpg')
        self.rect = self.image.get_rect()

        # 每艘新船在屏幕的底部中心开始.
        self.rect.midbottom = self.screen_rect.midbottom


        # 存储船舶的水平位置.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 状态
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 开火状态
        self.fire = False

    def update(self):
        """根据运动标志更新船舶的位置."""
        # 更新船舶的X，Y值，而不是矩形的值.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 更新.
        self.rect.x = self.x
        self.rect.y = self.y



    def blitme(self):
        """在当前位置绘制船舶."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """把船放在屏幕的中心."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
