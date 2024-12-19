import pygame

class Sprite:
    def __init__(self, image_path, position, rotation=0, scale=1.0):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.alpha = 255
        self._update_image()
    
    def _scale_image(self):
        size = self.image.get_size()
        scaled_size = (int(size[0] * self.scale), int(size[1] * self.scale))
        return pygame.transform.scale(self.image, scaled_size)

    def _set_rotation(self, angle):
        self.rotation = angle
        self._update_image()
    
    def _update_image(self):
        # Сначала масштабируем, потом поворачиваем
        self.image = self._scale_image()
        self.image = pygame.transform.rotate(self.image, self.rotation)
        self.image.set_alpha(self.alpha)  # Восстанавливаем прозрачность после трансформаций
    
    def set_alpha(self, alpha):
        self.alpha = max(0, min(255, alpha))
        self.image.set_alpha(self.alpha)
    
    def get_alpha(self):
        return self.alpha

    def draw(self, surface):
        surface.blit(self.image, self.position)