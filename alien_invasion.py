import datetime
import sys
from random import randint
from time import sleep

import pygame

import alien1
import alien2
import alien3
import alien4
import alien5
from role import Role
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien1 import Alien1
from alien2 import Alien2
from alien3 import Alien3
from alien4 import Alien4
from alien5 import Alien5



class AlienInvasion:
    """用于管理游戏内容和行为的总体类"""

    def __init__(self):
        """初始化游戏，并创建游戏资源."""
        pygame.init()
        self.settings = Settings()

        # 全屏
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 创建一个实例来存储游戏统计数据，并创建一个记分牌.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.role = Role(self)
        self.time1 = datetime.datetime.now()
        self.time2 = datetime.datetime.now()
        self.ships = pygame.sprite.Group()

        # 开始按钮.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """开始游戏的主循环."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                now_time = datetime.datetime.now()
                if (now_time - self.time1).seconds >= 2:
                    self._create_fleet()
                    self.time1 = now_time
                if self.ship.fire and (now_time - self.time2).microseconds >= 200 * 1000:
                    self._fire_bullet()
                    self.time2 = now_time

            self._update_screen()

    def _check_events(self):
        """对按键和鼠标事件做出反应."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """当玩家点击播放时，开始一个新游戏."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # 重置游戏统计数据.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 删除任何剩余的外星人和子弹.
            self.aliens.empty()
            self.bullets.empty()
            
            # 创建一个新的飞船，并把飞船放在底部中心位置.
            self._create_fleet()
            self.ship.center_ship()


    def _check_keydown_events(self, event):
        """对按键作出反应."""
        print("按下", event.key)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """对按键作出反应."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE:
            self.ship.fire = False

    def _fire_bullet(self):
        """创建一个新的子弹，并将其添加到子弹组."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并清除旧的子弹."""
        # 更新子弹的位置.
        self.bullets.update()

        # 清除旧的子弹.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """应对子弹和飞船与外星人的碰撞."""
        # 移除任何已经碰撞的子弹和外星人.
        collisions1 = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        collisions2 = pygame.sprite.groupcollide(self.ships, self.aliens, True, True)
        if collisions1:
            for aliens in collisions1.values():
                if type(aliens[0]) is alien1.Alien1:
                    self.stats.score += self.settings.alien1_points
                elif type(aliens[0]) is alien2.Alien2:
                    self.stats.score += self.settings.alien2_points
                elif type(aliens[0]) is alien3.Alien3:
                    self.stats.score += self.settings.alien3_points
                elif type(aliens[0]) is alien4.Alien4:
                    self.stats.score += self.settings.alien4_points
                elif type(aliens[0]) is alien5.Alien5:
                    self.stats.score += self.settings.alien5_points
            self.sb.prep_score()
            self.sb.check_high_score()
        if collisions2:
            for aliens in collisions2.values():
                if type(aliens[0]) is alien1.Alien1:
                    self.stats.score += self.settings.alien1_points
                elif type(aliens[0]) is alien2.Alien2:
                    self.stats.score += self.settings.alien2_points
                elif type(aliens[0]) is alien3.Alien3:
                    self.stats.score += self.settings.alien3_points
                elif type(aliens[0]) is alien4.Alien4:
                    self.stats.score += self.settings.alien4_points
                elif type(aliens[0]) is alien5.Alien5:
                    self.stats.score += self.settings.alien5_points
            self.sb.prep_score()
            self.sb.check_high_score()

        if  self.stats.score >1000 and self.stats.level == 1:
            self.settings.increase_speed()
            # 提高级别.
            self.stats.level += 1
            self.sb.prep_level()
            self.stats.ships_left += 1
            self.sb.prep_ships()
        elif  self.stats.score >3000 and self.stats.level == 2:
            self.settings.increase_speed()
            # 提高级别.
            self.stats.level += 1
            self.sb.prep_level()
            self.stats.ships_left += 1
            self.sb.prep_ships()
        elif  self.stats.score >7000 and self.stats.level == 3:
            self.settings.increase_speed()
            # 提高级别.
            self.stats.level += 1
            self.sb.prep_level()
            self.stats.ships_left += 1
            self.sb.prep_ships()
        elif  self.stats.score >15000 and self.stats.level == 4:
            self.settings.increase_speed()
            # 提高级别.
            self.stats.level += 1
            self.sb.prep_level()
            self.stats.ships_left += 1
            self.sb.prep_ships()
        elif  self.stats.score-(15000+self.stats.level*1000)>=5000 :
            self.settings.increase_speed()
            # 提高级别.
            self.stats.level += 1
            self.sb.prep_level()
            self.stats.ships_left += 1
            self.sb.prep_ships()

    def _update_aliens(self):
        """检查飞船是否在一个边缘，然后更新飞船中所有外星人的位置."""
        self.aliens.update()

        # 寻找外星飞船的碰撞.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 寻找打在屏幕底部的外星人.
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """检查是否有外星人到达屏幕底部."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 对待这一点，就像飞船被击中一样.
                self._ship_hit()
                self.aliens.remove(alien)

    def _ship_hit(self):
        """应对飞船被外星人击中的情况."""
        if self.stats.ships_left > 0:
            print(self.stats.ships_left)
            # 递减ships_left，并更新记分牌.
            self.ships.add(self.ship)
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self._check_bullet_alien_collisions()

            print(self.stats.ships_left)

        if self.stats.ships_left == 0:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """创建外星人舰队."""
        # 创建一个外星人，并找出一排的外星人数量.
        # 每个外星人之间的间距等于一个外星人的宽度.
        alien = Alien5(self)
        if self.stats.level == 1:
            alien = Alien1(self)
        elif self.stats.level == 2:
            alien = Alien2(self)
        elif self.stats.level == 3:
            alien = Alien3(self)
        elif self.stats.level == 4:
            alien = Alien4(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        x = []
        num=5
        # 创造随机数
        while num!=0:
            x1=randint(0, number_aliens_x)
            if x1 not in x:
                x.append(x1)
                num-=1
        # 创建外星人舰队.
        for alien_number in x:
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """创建一个外星人并把它放在行中."""
        alien = Alien5(self)
        if self.stats.level == 1:
            alien = Alien1(self)
        elif self.stats.level == 2:
            alien = Alien2(self)
        elif self.stats.level == 3:
            alien = Alien3(self)
        elif self.stats.level == 4:
            alien = Alien4(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height
        self.aliens.add(alien)


    def _update_screen(self):
        """更新屏幕上的图像，并翻转到新的屏幕上."""
        self.screen.fill(self.settings.bg_color)
        self.role.blitme()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 绘制分数信息.
        self.sb.show_score()

        # 如果游戏处于非活动状态，则绘制播放按钮.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # 制作一个游戏实例，并运行游戏.
    ai = AlienInvasion()
    ai.run_game()
