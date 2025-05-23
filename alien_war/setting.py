class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 10

        # 子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 200
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        self.alien_speed = 1.0
        self.fleet_drop_speed = 20

        # 1右移 -1左移
        self.fleet_direction = 1
