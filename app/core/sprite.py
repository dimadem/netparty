import pygame

class Sprite:
    def __init__(self, image_path, position, scale=1.0):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.position = position
        self.scale = scale
        self._scale_image()
    
    def _scale_image(self):
        size = self.image.get_size()
        scaled_size = (int(size[0] * self.scale), int(size[1] * self.scale))
        self.image = pygame.transform.scale(self.image, scaled_size)
    
    def set_alpha(self, alpha):
        self.alpha = max(0, min(255, alpha))
        self.image.set_alpha(self.alpha)
    
    def get_alpha(self):
        return self.alpha

    def draw(self, surface):
        surface.blit(self.image, self.position)