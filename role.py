import pygame


class Role:
    """管理角色类"""

    def __init__(self, ai_game):
        """初始化角色并设置其初始设置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载角色图像并获取其外接矩形
        self.image = pygame.image.load('images/Zelda.jpg')
        self.rect = self.image.get_rect()

        # 将其放在屏幕的中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在指定位置绘制角色"""
        self.screen.blit(self.image, self.rect)
