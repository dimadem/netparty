from app.core.scene import BaseScene
from app.core.sprite import Sprite
from app.core.animation import AlphaAnimation

class RoomScene(BaseScene):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.dancefloor_animations = []
        
        SCALE = 1/4
        
        self.add_sprite('main_background', Sprite('assets/pender_party/room/main_background_stage.png', (0, 0), 0, SCALE))

        dancefloor_configs = [
            ('g_o', 'o_g'), ('g_p', 'p_g'), ('g_v', 'v_g'),
            ('o_p', 'p_o'), ('p_v', 'v_p')
        ]

        for pair in dancefloor_configs:
            for name in pair:
                self.add_sprite(
                    f'{name}_background_dancefloor',
                    Sprite(f'assets/pender_party/room/{name}_background_dancefloor.png', (0, 0), 0, SCALE)
                )

        self.add_sprite('dj', Sprite('assets/pender_party/room/dj_pender.svg', (340, 400), 0, 1/1.1))
        self.add_sprite('girls_backstage', Sprite('assets/pender_party/room/girls_backstage.png', (0, 0), 0, SCALE))
        self.add_sprite('dj_table', Sprite('assets/pender_party/room/dj_table.png', (0, 0), 0, SCALE))

        self._setup_animations(dancefloor_configs)

    def _setup_animations(self, configs):
        for i, (name1_prefix, name2_prefix) in enumerate(configs):
            sprite1 = self.get_sprite(f'{name1_prefix}_background_dancefloor')
            sprite2 = self.get_sprite(f'{name2_prefix}_background_dancefloor')
            
            duration = 2.0 + (i * 0.5)
            self.dancefloor_animations.extend([
                AlphaAnimation(sprite1, duration=duration, phase_shift=i/0.2, 
                             loop=True, start_alpha=0, end_alpha=255),
                AlphaAnimation(sprite2, duration=duration, phase_shift=i*1.2, 
                             loop=True, start_alpha=255, end_alpha=0)
            ])

    def update(self, dt):
        if not self.active:
            return
        for anim in self.dancefloor_animations:
            anim.update(dt)
        super().update(dt)

    def draw_dancefloor(self, screen):
        dancefloor_sprites = [
            # 'g_o_background_dancefloor', 'o_g_background_dancefloor',
            'g_p_background_dancefloor', 'p_g_background_dancefloor',
            # 'g_v_background_dancefloor', 'v_g_background_dancefloor',
            # 'o_p_background_dancefloor', 'p_o_background_danceflo or',
            # 'p_v_background_dancefloor', 'v_p_background_dancefloor'
        ]
        
        for name in dancefloor_sprites:
            self.get_sprite(name).draw(screen)

    def draw(self, screen):
        self.get_sprite('main_background').draw(screen)
        self.draw_dancefloor(screen)
        self.get_sprite('girls_backstage').draw(screen)
        self.get_sprite('dj').draw(screen)
        self.get_sprite('dj_table').draw(screen)

    def handle_input(self, event):
        pass
