import arcade
from random import randint
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'STAR WARS'
LASERMOVESPEED = 6
TIESPEED = 1.61803398875
tierange = 0
METEORSPEED = 6.0000000000000000001
class TieFighter(arcade.Sprite):
    def __init__(self):
        super().__init__('TieFighter.png', 0.2)
        self.change_y = TIESPEED
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.kill()
class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__('laser.png', 0.8)
        self.center_x = window.falc.center_x
        self.bottom = window.falc.top - 20
        self.change_y = LASERMOVESPEED
        self.zzhh = arcade.load_sound('laser.wav')
    def update(self):
        self.center_y += self.change_y
        if self.center_y > SCREEN_HEIGHT:
            self.kill()
class Meteor(arcade.Sprite):
    def __init__(self):
        super().__init__('meteorit.png', 0.5)
        self.center_x = randint(50, SCREEN_WIDTH - 50)
        self.center_y = SCREEN_HEIGHT + randint(0, 250)
        self.change_y = METEORSPEED
    def update(self):
        self.center_y += self.change_y
        if self.top <= 0:
            self.center_y = SCREEN_HEIGHT + randint(0, 250)
class Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__('falcon.png', 0.3)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = 100
    def update(self):
        self.center_x += self.change_x
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture('background.jpg')
        self.winbg = arcade.load_texture('win.png')
        self.lostbg = arcade.load_texture('lost.jpg')
        self.falc = Falcon()
        self.set_mouse_visible(False)
        self.lasers = arcade.SpriteList()
        self.enemys = arcade.SpriteList()
        self.win = False
        self.score = 0
        self.lost = False
        self.meteor = Meteor()
        self.bg_music = arcade.load_sound('A New Hope.mp3')
    def on_mouse_motion(self, x, y, dx, dy):
        if self.lost == False and self.win == False:
            self.falc.center_x = x

    def on_mouse_press(self, x, y, btn, dy):
        if self.lost == False and self.win == False:
            if btn == arcade.MOUSE_BUTTON_LEFT:
                laser = Laser()
                self.lasers.append(laser)
                arcade.play_sound(laser.zzhh, 2)
    def setup(self):
        arcade.play_sound(self.bg_music, 0.2)
        for i in range(50):
            tiefighter = TieFighter()
            tiefighter.center_x = randint(0, SCREEN_WIDTH)
            tiefighter.center_y = SCREEN_HEIGHT + i * 75
            self.enemys.append(tiefighter)


    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.falc.draw()
        self.lasers.draw()
        self.enemys.draw()
        self.meteor.draw()
        arcade.draw_text(f'score: {self.score}', SCREEN_WIDTH - 800, SCREEN_HEIGHT - 25, (255, 255, 255), 25)
        if self.lost:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.lostbg)
        if self.win:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.winbg)
    def update(self, delta_time):
         if self.lost == False and self.win == False:
            hitlist = []
            self.falc.update()
            self.lasers.update()
            self.enemys.update()
            self.meteor.update()
            for lasr in self.lasers:
                hitlist = arcade.check_for_collision_with_list(lasr, self.enemys)
            lostdet = arcade.check_for_collision_with_list(self.falc, self.enemys)
            if len(lostdet) > 0:
                self.lost = True
            if hitlist:
                hitlist[-1].kill()
                lasr.kill()
                self.score += 1
            if self.score == 20:
                self.win = True
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
window.setup()
arcade.run()