from app.core.scene import BaseScene
from app.core.sprite import Sprite
from app.core.animation import AlphaAnimation  # Добавляем импорт
import math

class RoomScene(BaseScene):
    def __init__(self):
        super().__init__()  # Добавляем вызов родительского конструктора

    def initialize(self):
        """Initialize scene specific objects"""
        # Инициализируем список анимаций в начале initialize
        self.dancefloor_animations = []

        self.add_sprite('main_background', Sprite('assets/pender_party/room/main_background_stage.png', (0, 0), 0, 1/4))

        # party dancefloor
        self.add_sprite('g_o_background_dancefloor', Sprite('assets/pender_party/room/g_o_background_dancefloor.png', (0, 0), 0, 1/4))
        self.add_sprite('o_g_background_dancefloor', Sprite('assets/pender_party/room/o_g_background_dancefloor.png', (0, 0), 0, 1/4))

        self.add_sprite('g_p_background_dancefloor', Sprite('assets/pender_party/room/g_p_background_dancefloor.png', (0, 0), 0, 1/4))
        self.add_sprite('p_g_background_dancefloor', Sprite('assets/pender_party/room/p_g_background_dancefloor.png', (0, 0), 0, 1/4))

        self.add_sprite('g_v_background_dancefloor', Sprite('assets/pender_party/room/g_v_background_dancefloor.png', (0, 0), 0, 1/4))
        self.add_sprite('v_g_background_dancefloor', Sprite('assets/pender_party/room/v_g_background_dancefloor.png', (0, 0), 0, 1/4))

        self.add_sprite('o_p_background_dancefloor', Sprite('assets/pender_party/room/o_p_background_dancefloor.png', (0, 0), 0, 1/4))
        self.add_sprite('p_o_background_dancefloor', Sprite('assets/pender_party/room/p_o_background_dancefloor.png', (0, 0), 0, 1/4))

        self.add_sprite('p_v_background_dancefloor', Sprite('assets/pender_party/room/v_p_background_dancefloor.png', (0, 0), 0, 1/4))
        self.add_sprite('v_p_background_dancefloor', Sprite('assets/pender_party/room/p_v_background_dancefloor.png', (0, 0), 0, 1/4))

        self.add_sprite('dj', Sprite('assets/pender_party/room/dj_pender.svg', (340, 400), 0, 1/1.1))
        self.add_sprite('girls_backstage', Sprite('assets/pender_party/room/girls_backstage.png', (0, 0), 0, 1/4))
        self.add_sprite('dj_table', Sprite('assets/pender_party/room/dj_table.png', (0, 0), 0, 1/4))

        # Обновляем список пар для анимации, включая все спрайты танцпола
        dancefloor_pairs = [
            ('g_o_background_dancefloor', 'o_g_background_dancefloor'),
            ('g_p_background_dancefloor', 'p_g_background_dancefloor'),
            ('g_v_background_dancefloor', 'v_g_background_dancefloor'),
            ('o_p_background_dancefloor', 'p_o_background_dancefloor'),
            ('p_v_background_dancefloor', 'v_p_background_dancefloor')
        ]

        for i, (name1, name2) in enumerate(dancefloor_pairs):
            sprite1 = self.get_sprite(name1)
            sprite2 = self.get_sprite(name2)
            
            # Настраиваем разные скорости и фазы для каждой пары
            duration = 2.0 + (i * 0.5)  # Увеличиваем базовую длительность
            phase_shift_1 = i / 0.2  # Добавляем сдвиг фазы
            phase_shift_2 = i * 1.2
            # Создаем пару анимаций с противоположными альфа-переходами
            anim1 = AlphaAnimation(
                sprite1, 
                duration=duration, 
                phase_shift=phase_shift_1,  # Добавляем сдвиг фазы
                loop=True,
                start_alpha=0,   # Начинаем с прозрачного
                end_alpha=255    # Делаем непрозрачным
            )
            anim2 = AlphaAnimation(
                sprite2, 
                duration=duration, 
                phase_shift=phase_shift_2,  # Добавляем сдвиг фазы
                loop=True,
                start_alpha=255,  # Начинаем с непрозрачного
                end_alpha=0       # Делаем прозрачным
            )
            
            self.dancefloor_animations.extend([anim1, anim2])

    def update(self, dt):
        if not self.active:
            return
        # Обновляем все анимации
        for anim in self.dancefloor_animations:
            anim.update(dt)
        super().update(dt)

    def draw_dancefloor(self, screen):
        # Отрисовываем все спрайты танцпола
        dancefloor_sprites = [
            'g_o_background_dancefloor', 'o_g_background_dancefloor',
            'g_p_background_dancefloor', 'p_g_background_dancefloor',
            'g_v_background_dancefloor', 'v_g_background_dancefloor',
            'o_p_background_dancefloor', 'p_o_background_dancefloor',
            'p_v_background_dancefloor', 'v_p_background_dancefloor'
        ]
        
        for name in dancefloor_sprites:
            self.get_sprite(name).draw(screen)

    def draw(self, screen):
        self.draw_dancefloor(screen)  # Сначала рисуем анимированный dancefloor
        self.get_sprite('girls_backstage').draw(screen)
        self.get_sprite('dj').draw(screen)
        self.get_sprite('dj_table').draw(screen)

    def handle_input(self, event):
        """Handle input events"""
        pass
