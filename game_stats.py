class GameStats:
    """外星人入侵的轨迹统计."""
    
    def __init__(self, ai_game):
        """初始化统计数据."""
        self.settings = ai_game.settings
        self.reset_stats()

        # 在非活动状态下开始游戏.
        self.game_active = False

        # 高分不应该被重置.
        self.high_score = 0
        
    def reset_stats(self):
        """初始化游戏过程中可能发生变化的统计数据."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1