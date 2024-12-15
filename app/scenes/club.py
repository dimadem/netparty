from app.core.sprite import Sprite
import math

class ClubScene:
    def __init__(self):
        self.discoball = Sprite('assets/pender_party/club/discoball.png', (1920 - 1920 / 2.8 , -120), 1.0)
        self.spot_1 = Sprite('assets/pender_party/club/spot_1.png', (0, 0), 1.0)
        self.spot_2 = Sprite('assets/pender_party/club/spot_2.png', (0, 0), 1.0)
        self.spot_3 = Sprite('assets/pender_party/club/spot_3.png', (0, 0), 1.0)
        self.spot_4 = Sprite('assets/pender_party/club/spot_4.png', (0, 0), 1.0)
        self.spots = [self.spot_1, self.spot_2, self.spot_3, self.spot_4]
        self.animation_time = 0
        self.base_alpha = 255

    def _discoball_animation(self, dt):
        self.animation_time += dt
        disco_pulse = 0.35 * math.sin(self.animation_time * math.pi) + 0.65
        disco_alpha = int(self.base_alpha * disco_pulse)
        self.discoball.set_alpha(disco_alpha)

    def _spot_animation(self, dt):
        for i, spot in enumerate(self.spots):
            phase_shift = i * math.pi / 2
            spot_pulse = 0.5 * math.sin(self.animation_time * math.pi * 2 + phase_shift) + 0.5
            spot_alpha = int(self.base_alpha * spot_pulse)
            spot.set_alpha(spot_alpha)
    
    def update(self, dt):
        self._discoball_animation(dt)
        self._spot_animation(dt)

    def draw(self, screen):
        for spot in self.spots:
            spot.draw(screen)
        self.discoball.draw(screen)