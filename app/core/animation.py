import math  # Добавляем импорт в начало файла
from functools import lru_cache

class Animation:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed
        self.current_frame = 0
        self.timer = 0
        self.paused = False
        self.loop = True
    
    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
    
    def reset(self):
        self.current_frame = 0
        self.timer = 0
    
    def update(self, dt):
        if self.paused:
            return

        self.timer += dt
        if self.timer >= self.speed:
            if self.loop or self.current_frame < len(self.frames) - 1:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.timer = 0
        
    def get_current_frame(self):
        return self.frames[self.current_frame]

class SpriteAnimation:
    def __init__(self, sprite, duration=1.0, loop=True):
        self.sprite = sprite
        self.duration = duration
        self.loop = loop
        self.time = 0
        self.completed = False

    def update(self, dt):
        if self.completed and not self.loop:
            return

        self.time += dt
        if self.time >= self.duration:
            if self.loop:
                self.time = 0
            else:
                self.completed = True

    def reset(self):
        self.time = 0
        self.completed = False

class AlphaAnimation(SpriteAnimation):
    def __init__(self, sprite, start_alpha=0, end_alpha=255, phase_shift=0, **kwargs):
        super().__init__(sprite, **kwargs)
        self.start_alpha = start_alpha
        self.end_alpha = end_alpha
        self.phase_shift = phase_shift  # Добавляем сдвиг фазы
        self._last_update_time = 0
        self._update_interval = 1/30  # Обновляем анимацию 30 раз в секунду

    @lru_cache(maxsize=1000)
    def _calculate_progress(self, normalized_time):
        """Кэшируем расчеты прогресса анимации"""
        return (math.sin(normalized_time * math.pi * 2 + self.phase_shift) + 1) / 2

    def update(self, dt):
        self.time += dt
        
        # Обновляем альфа только если прошло достаточно времени
        current_time = self.time
        if current_time - self._last_update_time < self._update_interval:
            return

        self._last_update_time = current_time
        
        if self.completed and not self.loop:
            return

        progress = (self.time / self.duration) if self.duration > 0 else 1
        if self.loop:
            progress = self._calculate_progress(progress)
        
        current_alpha = int(self.start_alpha + (self.end_alpha - self.start_alpha) * progress)
        self.sprite.set_alpha(current_alpha)