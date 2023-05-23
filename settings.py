class Settings:
    """所有设置的类."""

    def __init__(self):
        """初始化游戏的静态设置."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 255, 100)

        # 船舶设置
        self.ship_limit = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏加速的速度有多快
        self.speedup_scale = 1.15

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化设置，在整个游戏过程中发生变化."""
        self.ship_speed = 2
        self.bullet_speed = 0.8
        self.alien_speed = 0.1

        # 评分
        self.alien1_points = 50
        self.alien2_points = 100
        self.alien3_points = 150
        self.alien4_points = 200
        self.alien5_points = 250

    def increase_speed(self):
        """增加速度设置和外来点值."""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
