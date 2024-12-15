from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self):
        self.sprites = {}
        self.animations = {}
        self.active = False
        self.initialize()

    @abstractmethod
    def initialize(self):
        """Initialize scene specific objects"""
        pass

    def add_sprite(self, name, sprite):
        self.sprites[name] = sprite
        return sprite

    def get_sprite(self, name):
        return self.sprites.get(name)

    def add_animation(self, name, animation):
        self.animations[name] = animation
        return animation

    def on_enter(self):
        self.active = True

    def on_exit(self):
        self.active = False

    def update(self, dt):
        for animation in self.animations.values():
            animation.update(dt)

    def draw(self, screen):
        for sprite in self.sprites.values():
            sprite.draw(screen)

    @abstractmethod
    def handle_input(self, event):
        """Handle input events"""
        pass

    def cleanup(self):
        """Cleanup resources"""
        self.sprites.clear()
        self.animations.clear()
