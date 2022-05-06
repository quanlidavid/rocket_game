class Settings():
    """储存设置"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (123, 234, 0)

        self.rocket_speed = 1.5

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 1.0
        self.bullet_color = (30, 30, 30)
        self.bullet_allowed = 10
